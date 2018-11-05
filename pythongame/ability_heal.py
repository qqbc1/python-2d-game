import pygame

from pythongame.abilities import register_ability_effect
from pythongame.buffs import AbstractBuff, register_buff_effect
from pythongame.common import BuffType, Millis, AbilityType
from pythongame.game_data import register_ability_data, AbilityData, UiIconSprite, register_ui_icon_sprite_path, \
    register_buff_text
from pythongame.game_state import GameState
from pythongame.visual_effects import create_visual_healing_text, VisualCircle


def _apply_heal(game_state: GameState):
    game_state.player_state.gain_buff(BuffType.HEALING_OVER_TIME, Millis(3500))


class HealingOverTime(AbstractBuff):
    def __init__(self):
        self._time_since_graphics = 0

    def apply_middle_effect(self, game_state: GameState, time_passed: Millis):
        self._time_since_graphics += time_passed
        healing_amount = 0.04
        game_state.player_state.gain_health(healing_amount * time_passed)
        if self._time_since_graphics > 500:
            estimate_health_gained = int(self._time_since_graphics * healing_amount)
            game_state.visual_effects.append(
                create_visual_healing_text(game_state.player_entity, estimate_health_gained))
            game_state.visual_effects.append(
                VisualCircle((200, 200, 50), game_state.player_entity.get_center_position(),
                             10, Millis(100), 0))
            self._time_since_graphics = 0


def register_heal_ability():
    register_ability_effect(AbilityType.HEAL, _apply_heal)
    register_ability_data(AbilityType.HEAL, AbilityData(UiIconSprite.HEAL_ABILITY, 10, "W", pygame.K_w, Millis(15000)))
    register_ui_icon_sprite_path(UiIconSprite.HEAL_ABILITY, "resources/heal_ability.png")
    register_buff_effect(BuffType.HEALING_OVER_TIME, HealingOverTime())
    register_buff_text(BuffType.HEALING_OVER_TIME, "Healing")
