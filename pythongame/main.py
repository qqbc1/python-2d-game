from typing import Optional

import pygame

from pythongame.core.buff_effects import get_buff_effect
from pythongame.core.common import SceneId, Millis, HeroId, ItemType, ConsumableType, Sprite, BuffType, get_random_hint
from pythongame.core.consumable_inventory import ConsumableInventory
from pythongame.core.game_data import allocate_input_keys_for_abilities
from pythongame.core.game_engine import GameEngine
from pythongame.core.player_environment_interactions import PlayerInteractionsState
from pythongame.core.sound_player import init_sound_player
from pythongame.core.view import View
from pythongame.core.view_state import ViewState
from pythongame.map_file import create_game_state_from_json_file
from pythongame.player_file import SavedPlayerState, load_player_state_from_json_file
from pythongame.register_game_data import register_all_game_data
from pythongame.scene_paused import PausedScene
from pythongame.scene_picking_hero.scene_picking_hero import PickingHeroScene
from pythongame.scene_playing import PlayingScene

SCREEN_SIZE = (700, 700)
CAMERA_SIZE = (700, 530)

register_all_game_data()


class Main:
    def __init__(self, map_file_name: Optional[str], chosen_hero_id: Optional[str], hero_start_level: Optional[int],
                 start_money: Optional[int], load_from_file: Optional[str]):

        map_file_name = map_file_name or "map1.json"
        self.map_file_path = "resources/maps/" + map_file_name

        pygame.init()

        self.view = View(CAMERA_SIZE, SCREEN_SIZE)
        init_sound_player()
        self.clock = pygame.time.Clock()

        self.picking_hero_scene = PickingHeroScene(self.view)
        # These are initialized after hero has been picked
        self.playing_scene = None
        self.paused_scene = None
        self.game_state = None
        self.view_state = None
        self.game_engine = None
        self.player_interactions_state = None

        start_immediately_and_skip_hero_selection = (
                chosen_hero_id is not None
                or hero_start_level is not None
                or start_money is not None
                or load_from_file is not None)
        if start_immediately_and_skip_hero_selection:
            saved_player_state = load_player_state_from_json_file(
                "savefiles/" + load_from_file) if load_from_file else None
            if saved_player_state:
                picked_hero = HeroId[saved_player_state.hero_id]
            elif chosen_hero_id:
                picked_hero = HeroId[chosen_hero_id]
            else:
                picked_hero = HeroId.MAGE
            hero_start_level = int(hero_start_level) if hero_start_level else 1
            start_money = int(start_money) if start_money else 0
            self.setup_game(picked_hero, hero_start_level, start_money, saved_player_state)
            self.scene_id: SceneId = SceneId.PLAYING
        else:
            self.scene_id: SceneId = SceneId.PICKING_HERO

    def main_loop(self):
        while True:
            self.clock.tick()
            time_passed = Millis(self.clock.get_time())

            if self.scene_id == SceneId.PICKING_HERO:
                picked_hero = self.picking_hero_scene.run_one_frame()
                if picked_hero is not None:
                    self.setup_game(picked_hero, 1, 0, None)
                    self.scene_id = SceneId.PLAYING

            elif self.scene_id == SceneId.PLAYING:
                transition_to_pause = self.playing_scene.run_one_frame(time_passed, str(int(self.clock.get_fps())))
                if transition_to_pause:
                    self.scene_id = SceneId.PAUSED

            elif self.scene_id == SceneId.PAUSED:
                transition_to_playing = self.paused_scene.run_one_frame()
                if transition_to_playing:
                    self.scene_id = SceneId.PLAYING

            else:
                raise Exception("Unhandled scene: " + str(self.scene_id))

    def setup_game(self, picked_hero: HeroId, hero_start_level: int, start_money: int,
                   saved_player_state: Optional[SavedPlayerState]):
        self.game_state = create_game_state_from_json_file(CAMERA_SIZE, self.map_file_path, picked_hero)
        self.view_state = ViewState(self.game_state.entire_world_area)
        self.game_engine = GameEngine(self.game_state, self.view_state)
        self.player_interactions_state = PlayerInteractionsState()
        self.playing_scene = PlayingScene(
            self.game_state,
            self.game_engine,
            self.view,
            self.view_state)
        self.paused_scene = PausedScene(self.game_state, self.view, self.view_state)
        self.view_state.set_message("Hint: " + get_random_hint())

        if saved_player_state:
            self.game_state.player_state.gain_exp_worth_n_levels(saved_player_state.level - 1)
            self.game_state.player_state.gain_exp(saved_player_state.exp)
            self.game_engine.set_item_inventory([ItemType[item] if item else None for item in saved_player_state.items])
            self.game_state.player_state.consumable_inventory = ConsumableInventory(
                {int(slot_number): [ConsumableType[c] for c in consumables] for (slot_number, consumables)
                 in saved_player_state.consumables_in_slots.items()}
            )
            self.game_state.player_state.money += saved_player_state.money
            for portal in self.game_state.portals:
                if portal.portal_id.name in saved_player_state.enabled_portals:
                    sprite = saved_player_state.enabled_portals[portal.portal_id.name]
                    portal.activate(Sprite[sprite])
        else:
            if hero_start_level > 1:
                self.game_state.player_state.gain_exp_worth_n_levels(hero_start_level - 1)
            if start_money > 0:
                self.game_state.player_state.money += start_money

        allocate_input_keys_for_abilities(self.game_state.player_state.abilities)

        self.game_state.player_state.gain_buff_effect(get_buff_effect(BuffType.BEING_SPAWNED), Millis(1000))


def start(map_file_name: Optional[str], chosen_hero_id: Optional[str], hero_start_level: Optional[int],
          start_money: Optional[int], load_from_file: Optional[str]):
    main = Main(map_file_name, chosen_hero_id, hero_start_level, start_money, load_from_file)
    main.main_loop()
