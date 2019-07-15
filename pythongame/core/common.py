from enum import Enum

from typing import NewType

Millis = NewType('Millis', int)


class Direction(Enum):
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4


def get_all_directions():
    return [Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT]


class ConsumableType(Enum):
    HEALTH_LESSER = 1
    HEALTH = 2
    MANA_LESSER = 11
    MANA = 12
    SPEED = 21
    INVISIBILITY = 22
    SCROLL_ABILITY_SUMMON = 101


class NpcType(Enum):
    CHEST = 1
    NECROMANCER = 3
    WARRIOR = 4
    RAT_1 = 5
    RAT_2 = 6
    DARK_REAPER = 7
    GOBLIN_WARLOCK = 8
    MUMMY = 9
    PLAYER_SUMMON = 10
    NEUTRAL_DWARF = 20
    NEUTRAL_NOMAD = 21
    NEUTRAL_NINJA = 22


class WallType(Enum):
    WALL = 1
    STATUE = 2
    WALL_DIRECTIONAL_N = 11
    WALL_DIRECTIONAL_NE = 12
    WALL_DIRECTIONAL_E = 13
    WALL_DIRECTIONAL_SE = 14
    WALL_DIRECTIONAL_S = 15
    WALL_DIRECTIONAL_SW = 16
    WALL_DIRECTIONAL_W = 17
    WALL_DIRECTIONAL_NW = 18
    WALL_DIRECTIONAL_POINTY_NE = 19
    WALL_DIRECTIONAL_POINTY_SE = 20
    WALL_DIRECTIONAL_POINTY_SW = 21
    WALL_DIRECTIONAL_POINTY_NW = 22
    WALL_CHAIR = 30
    ALTAR = 31


class AbilityType(Enum):
    HEAL = 1
    FIREBALL = 2
    CHANNEL_ATTACK = 4
    TELEPORT = 5
    FROST_NOVA = 6
    WHIRLWIND = 7
    ENTANGLING_ROOTS = 8
    SUMMON = 9
    SWORD_SLASH = 10
    BLOOD_LUST = 11
    CHARGE = 12
    STOMP = 13
    SHIV = 14
    SNEAK = 15


class Sprite(Enum):
    EFFECT_ABILITY_FROST_NOVA = 3
    PROJECTILE_PLAYER_FIREBALL = 11
    PROJECTILE_PLAYER_MAGIC_MISSILE = 12
    PROJECTILE_PLAYER_WHIRLWIND = 13
    PROJECTILE_ENEMY_GOBLIN_WARLOCK = 14
    PROJECTILE_PLAYER_ENTANGLING_ROOTS = 15
    POTION_HEALTH = 101
    POTION_HEALTH_LESSER = 102
    POTION_MANA = 103
    POTION_MANA_LESSER = 104
    POTION_SCROLL_ABILITY_SUMMON = 105
    ENEMY_NECROMANCER = 201
    ENEMY_RAT_1 = 202
    ENEMY_RAT_2 = 203
    ENEMY_DARK_REAPER = 204
    ENEMY_GOBLIN_WARLOCK = 205
    ENEMY_MUMMY = 206
    ENEMY_WARRIOR = 207
    ENEMY_CHEST = 208
    PLAYER_SUMMON = 250
    NEUTRAL_NPC_DWARF = 260
    NEUTRAL_NPC_NOMAD = 261
    NEUTRAL_NPC_NINJA = 262
    ITEM_AMULET_OF_MANA = 301
    ITEM_WINGED_BOOTS = 302
    ITEM_ROD_OF_LIGHTNING = 303
    ITEM_SWORD_OF_LEECHING = 304
    ITEM_SOLDIERS_HELMET = 305
    ITEM_BLESSED_SHIELD = 306
    ITEM_STAFF_OF_FIRE = 307
    ITEM_BLUE_ROBE = 308
    ITEM_ORB_OF_THE_MAGI = 309
    ITEM_WIZARDS_COWL = 310
    ITEM_ZULS_AEGIS = 311
    ITEM_KNIGHTS_ARMOR = 312
    ITEM_GOATS_RING = 313
    COINS_1 = 350
    COINS_2 = 351
    COINS_5 = 352
    DECORATION_GROUND_STONE = 401
    DECORATION_PLANT = 403
    DECORATION_ENTANGLING_ROOTS_EFFECT = 404
    WALL = 501
    WALL_STATUE = 502
    WALL_ALTAR = 503
    WALL_DIRECTIONAL_N = 511
    WALL_DIRECTIONAL_NE = 512
    WALL_DIRECTIONAL_E = 513
    WALL_DIRECTIONAL_SE = 514
    WALL_DIRECTIONAL_S = 515
    WALL_DIRECTIONAL_SW = 516
    WALL_DIRECTIONAL_W = 517
    WALL_DIRECTIONAL_NW = 518
    WALL_DIRECTIONAL_POINTY_NE = 519
    WALL_DIRECTIONAL_POINTY_SE = 520
    WALL_DIRECTIONAL_POINTY_SW = 521
    WALL_DIRECTIONAL_POINTY_NW = 522
    WALL_CHAIR = 530
    PORTAL_DISABLED = 600
    PORTAL_BLUE = 601
    PORTAL_GREEN = 602
    PORTAL_RED = 603
    PORTAL_DARK = 604
    HERO_MAGE = 700
    HERO_WARRIOR = 701
    HERO_ROGUE = 702


class BuffType(Enum):
    HEALING_OVER_TIME = 1
    INCREASED_MOVE_SPEED = 3
    INVISIBILITY = 4
    CHANNELING_MAGIC_MISSILES = 5
    REDUCED_MOVEMENT_SPEED = 6
    INVULNERABILITY = 7
    STUNNED_BY_WHIRLWIND = 8
    ENEMY_GOBLIN_WARLOCK_BURNT = 9
    ROOTED_BY_ENTANGLING_ROOTS = 10
    SUMMON_DIE_AFTER_DURATION = 11
    BLOOD_LUST = 13
    CHARGING = 14
    STUNNED_FROM_CHARGE_IMPACT = 15
    BEING_TELEPORTED = 16
    RECOVERING_AFTER_ABILITY = 17
    CHANNELING_STOMP = 18
    STUNNED_BY_STOMP = 19
    SNEAKING = 20
    AFTER_SNEAKING = 21
    STUNNED_BY_AEGIS_ITEM = 22
    DEBUFFED_BY_GOATS_RING = 23


class ItemType(Enum):
    WINGED_BOOTS = 1
    SWORD_OF_LEECHING = 3
    ROD_OF_LIGHTNING = 4
    STAFF_OF_FIRE = 7
    AMULET_OF_MANA_1 = 10
    AMULET_OF_MANA_2 = 11
    AMULET_OF_MANA_3 = 12
    BLESSED_SHIELD_1 = 20
    BLESSED_SHIELD_2 = 21
    BLESSED_SHIELD_3 = 22
    SOLDIERS_HELMET_1 = 30
    SOLDIERS_HELMET_2 = 31
    SOLDIERS_HELMET_3 = 32
    BLUE_ROBE_1 = 40
    BLUE_ROBE_2 = 41
    BLUE_ROBE_3 = 42
    ORB_OF_THE_MAGI_1 = 50
    ORB_OF_THE_MAGI_2 = 51
    ORB_OF_THE_MAGI_3 = 52
    WIZARDS_COWL = 60
    ZULS_AEGIS = 70
    KNIGHTS_ARMOR = 71
    GOATS_RING = 72


class ProjectileType(Enum):
    PLAYER_FIREBALL = 1
    PLAYER_MAGIC_MISSILE = 2
    PLAYER_WHIRLWIND = 3
    PLAYER_ENTANGLING_ROOTS = 4
    ENEMY_GOBLIN_WARLOCK = 101


class SoundId(Enum):
    ABILITY_FIREBALL = 1
    ABILITY_WHIRLWIND = 2
    ABILITY_TELEPORT = 3
    ABILITY_ENTANGLING_ROOTS = 4
    ABILITY_CHARGE = 5
    POTION = 50
    EVENT_PLAYER_LEVELED_UP = 100
    EVENT_PICKED_UP = 101
    EVENT_PLAYER_DIED = 102
    EVENT_ENEMY_DIED = 103
    EVENT_PICKED_UP_MONEY = 104
    WARNING = 200
    PLAYER_PAIN = 300
    ENEMY_ATTACK_GOBLIN_WARLOCK = 400


class PortalId(Enum):
    A_BASE = 1
    A_REMOTE = 2
    B_BASE = 3
    B_REMOTE = 4
    C_BASE = 5
    C_REMOTE = 6


class HeroId(Enum):
    MAGE = 1
    WARRIOR = 2
    ROGUE = 3


class UiIconSprite(Enum):
    POTION_HEALTH_LESSER = 1
    POTION_HEALTH = 2
    POTION_MANA_LESSER = 3
    POTION_MANA = 4
    POTION_SPEED = 11
    POTION_INVISIBILITY = 12
    POTION_SCROLL_ABILITY_SUMMON = 13
    ABILITY_FIREBALL = 101
    ABILITY_HEAL = 102
    ABILITY_MAGIC_MISSILE = 103
    ABILITY_TELEPORT = 104
    ABILITY_FROST_NOVA = 105
    ABILITY_WHIRLWIND = 106
    ABILITY_ENTANGLING_ROOTS = 107
    ABILITY_SUMMON = 108
    ABILITY_SWORD_SLASH = 109
    ABILITY_BLOODLUST = 110
    ABILITY_CHARGE = 111
    ABILITY_STOMP = 112
    ABILITY_SHIV = 113
    ABILITY_SNEAK = 114
    ITEM_WINGED_BOOTS = 201
    ITEM_AMULET_OF_MANA = 202
    ITEM_SWORD_OF_LEECHING = 203
    ITEM_ROD_OF_LIGHTNING = 204
    ITEM_SOLDIERS_HELMET = 205
    ITEM_BLESSED_SHIELD = 206
    ITEM_STAFF_OF_FIRE = 207
    ITEM_BLUE_ROBE = 208
    ITEM_ORB_OF_THE_MAGI = 209
    ITEM_WIZARDS_COWL = 210
    ITEM_ZULS_AEGIS = 211
    ITEM_KNIGHTS_ARMOR = 212
    ITEM_GOATS_RING = 213
    MAP_EDITOR_TRASHCAN = 301
    MAP_EDITOR_RECYCLING = 302


# Portraits that are shown in UI (player portrait and dialog portraits)
class PortraitIconSprite(Enum):
    VIKING = 2
    NOMAD = 3
    NINJA = 4
    HERO_MAGE = 10
    HERO_WARRIOR = 11
    HERO_ROGUE = 12
