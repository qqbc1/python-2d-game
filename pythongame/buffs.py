from pythongame.common import *
from pythongame.game_data import MAGIC_MISSILE_PROJECTILE_SIZE
from pythongame.game_state import GameState, WorldEntity, Projectile
from pythongame.projectiles import create_projectile_controller
from pythongame.visual_effects import VisualCircle, VisualRect


class AbstractBuff:
    def apply_start_effect(self, game_state: GameState):
        pass

    def apply_middle_effect(self, game_state: GameState, time_passed: Millis):
        pass

    def apply_end_effect(self, game_state: GameState):
        pass


class HealingOverTime(AbstractBuff):
    def __init__(self):
        self._time_since_graphics = 0

    def apply_middle_effect(self, game_state: GameState, time_passed: Millis):
        self._time_since_graphics += time_passed
        game_state.player_state.gain_health(0.04 * time_passed)
        if self._time_since_graphics > 500:
            game_state.visual_effects.append(
                VisualCircle((200, 200, 50), game_state.player_entity.get_center_position(),
                             10, Millis(100)))
            self._time_since_graphics = 0


class DamageOverTime(AbstractBuff):
    def __init__(self):
        self._time_since_graphics = 0

    def apply_middle_effect(self, game_state: GameState, time_passed: Millis):
        self._time_since_graphics += time_passed
        game_state.player_state.lose_health(0.02 * time_passed)
        if self._time_since_graphics > 300:
            game_state.visual_effects.append(VisualCircle((50, 180, 50), game_state.player_entity.get_center_position(),
                                                          20, Millis(50)))
            self._time_since_graphics = 0


class IncreasedMoveSpeed(AbstractBuff):
    def __init__(self):
        self._time_since_graphics = 0

    def apply_start_effect(self, game_state: GameState):
        game_state.player_entity.add_to_speed_multiplier(1)

    def apply_middle_effect(self, game_state: GameState, time_passed: Millis):
        self._time_since_graphics += time_passed
        if self._time_since_graphics > 100:
            game_state.visual_effects.append(
                VisualCircle((150, 200, 250), game_state.player_entity.get_center_position(), 10, Millis(200)))
            self._time_since_graphics = 0

    def apply_end_effect(self, game_state: GameState):
        game_state.player_entity.add_to_speed_multiplier(-1)


class Invisibility(AbstractBuff):
    def __init__(self):
        self._time_since_graphics = 0

    def apply_start_effect(self, game_state: GameState):
        game_state.player_state.is_invisible = True

    def apply_middle_effect(self, game_state: GameState, time_passed: Millis):
        self._time_since_graphics += time_passed
        if self._time_since_graphics > 80:
            self._time_since_graphics = 0
            game_state.visual_effects.append(
                VisualRect((0, 0, 250), game_state.player_entity.get_center_position(), 40, 80))

    def apply_end_effect(self, game_state: GameState):
        game_state.player_state.is_invisible = False


class ChannelingMagicMissiles(AbstractBuff):
    def __init__(self):
        self._time_since_firing = 0

    def apply_start_effect(self, game_state: GameState):
        game_state.player_state.is_stunned = True
        game_state.player_entity.set_not_moving()

    def apply_middle_effect(self, game_state: GameState, time_passed: Millis):
        self._time_since_firing += time_passed
        if self._time_since_firing > 150:
            self._time_since_firing = 0
            player_center_position = game_state.player_entity.get_center_position()
            projectile_pos = (player_center_position[0] - MAGIC_MISSILE_PROJECTILE_SIZE[0] / 2,
                              player_center_position[1] - MAGIC_MISSILE_PROJECTILE_SIZE[1] / 2)
            entity = WorldEntity(projectile_pos, MAGIC_MISSILE_PROJECTILE_SIZE, Sprite.MAGIC_MISSILE,
                                 game_state.player_entity.direction, 0.5)
            projectile = Projectile(entity, create_projectile_controller(ProjectileType.PLAYER_MAGIC_MISSILE))
            game_state.projectile_entities.append(projectile)
            game_state.visual_effects.append(VisualRect((250, 0, 250), player_center_position, 60, 250))

    def apply_end_effect(self, game_state: GameState):
        game_state.player_state.is_stunned = False


BUFF_EFFECTS = {
    BuffType.HEALING_OVER_TIME: HealingOverTime(),
    BuffType.DAMAGE_OVER_TIME: DamageOverTime(),
    BuffType.INCREASED_MOVE_SPEED: IncreasedMoveSpeed(),
    BuffType.INVISIBILITY: Invisibility(),
    BuffType.CHANNELING_MAGIC_MISSILES: ChannelingMagicMissiles()
}