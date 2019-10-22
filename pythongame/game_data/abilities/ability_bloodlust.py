from typing import Optional

from pythongame.core.ability_effects import register_ability_effect, AbilityResult, AbilityWasUsedSuccessfully
from pythongame.core.buff_effects import AbstractBuffEffect, register_buff_effect, get_buff_effect
from pythongame.core.common import BuffType, Millis, AbilityType, UiIconSprite, SoundId, PeriodicTimer
from pythongame.core.game_data import register_ability_data, AbilityData, register_ui_icon_sprite_path, \
    register_buff_text
from pythongame.core.game_state import GameState, WorldEntity, NonPlayerCharacter, Event, BuffEventOutcome, \
    EnemyDiedEvent
from pythongame.core.visual_effects import VisualCircle

COOLDOWN = Millis(25000)
BUFF_DURATION = Millis(10000)
BUFF_TYPE = BuffType.BLOOD_LUST
LIFE_STEAL_BONUS_RATIO = 0.15
KILL_DURATION_INCREASE_BONUS = Millis(1000)


def _apply_ability(game_state: GameState) -> AbilityResult:
    game_state.player_state.gain_buff_effect(get_buff_effect(BUFF_TYPE), BUFF_DURATION)
    return AbilityWasUsedSuccessfully()


class BloodLust(AbstractBuffEffect):

    def __init__(self):
        self.timer = PeriodicTimer(Millis(250))

    def apply_start_effect(self, game_state: GameState, buffed_entity: WorldEntity, buffed_npc: NonPlayerCharacter):
        game_state.player_state.life_steal_ratio += LIFE_STEAL_BONUS_RATIO

    def apply_middle_effect(self, game_state: GameState, buffed_entity: WorldEntity, buffed_npc: NonPlayerCharacter,
                            time_passed: Millis):
        if self.timer.update_and_check_if_ready(time_passed):
            visual_effect = VisualCircle(
                (250, 0, 0,), buffed_entity.get_center_position(), 25, 30, Millis(350), 1, buffed_entity)
            game_state.visual_effects.append(visual_effect)

    def apply_end_effect(self, game_state: GameState, buffed_entity: WorldEntity, buffed_npc: NonPlayerCharacter):
        game_state.player_state.life_steal_ratio -= LIFE_STEAL_BONUS_RATIO

    def get_buff_type(self):
        return BUFF_TYPE

    def buff_handle_event(self, event: Event) -> Optional[BuffEventOutcome]:
        if isinstance(event, EnemyDiedEvent):
            return BuffEventOutcome.change_remaining_duration(KILL_DURATION_INCREASE_BONUS)


def register_bloodlust_ability():
    ability_type = AbilityType.BLOOD_LUST
    register_ability_effect(ability_type, _apply_ability)
    ui_icon_sprite = UiIconSprite.ABILITY_BLOODLUST
    description = "Gain +" + str(int(LIFE_STEAL_BONUS_RATIO * 100)) + "% lifesteal for " + \
                  "{:.0f}".format(BUFF_DURATION / 1000) + "s. Duration is increased by " + \
                  "{:.0f}".format(KILL_DURATION_INCREASE_BONUS / 1000) + "s for each enemy killed."
    register_ability_data(
        ability_type,
        AbilityData("Bloodlust", ui_icon_sprite, 25, COOLDOWN, description, SoundId.ABILITY_BLOODLUST))
    register_ui_icon_sprite_path(ui_icon_sprite, "resources/graphics/icon_bloodlust.png")
    register_buff_effect(BUFF_TYPE, BloodLust)
    register_buff_text(BUFF_TYPE, "Bloodlust")
