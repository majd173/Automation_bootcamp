import unittest

from API_Project.deck_of_cards.infra.config_provider import ConfigProvider
# from API_Project.deck_of_cards.infra.config_provider import ConfigProvider
from API_Project.deck_of_cards.logic.deck_of_cards_web import APIDecksOfCards
from API_Project.deck_of_cards.infra.API_Wrapper import APIWrapper


class TestDeckOfCards(unittest.TestCase):

    def setUp(self):
        self._config = ConfigProvider().load_from_file("../cards_config.json")
        self._api = APIWrapper()

    def test_back_of_cards(self):
        deck_of_cards = APIDecksOfCards(self._api)
        self.assertTrue(deck_of_cards.get_back_of_card(self._config['base_url']))
        self.assertGreaterEqual(200, deck_of_cards.get_back_of_card_get_status(
            self._config['base_url']))

    def test_shuffle_the_cards(self):
        deck_of_cards = APIDecksOfCards(self._api)
        self.assertTrue(deck_of_cards.shuffle_the_cards(self._config['base_url']).ok)
        self.assertEqual(deck_of_cards.shuffle_the_cards_get_status(
            self._config['base_url'], 2), 200)

    def test_draw_a_card(self):
        deck_of_cards = APIDecksOfCards(self._api)
        self.assertTrue(deck_of_cards.draw_a_card(self._config['base_url']).ok)
        self.assertEqual(deck_of_cards.draw_a_card_get_status(
            self._config['base_url']), 200)
        self.assertEqual(deck_of_cards.draw_a_card_get_json(
            self._config['base_url'])["success"], True)


    def test_a_partial_deck(self):
        deck_of_cards = APIDecksOfCards(self._api)
        self.assertTrue(deck_of_cards.a_partial_deck(self._config['base_url']).ok)
        # self.assertEqual(deck_of_cards.a_partial_deck_get_json(
        #     self._config['base_url']), 8)
        self.assertEqual(deck_of_cards.a_partial_deck_get_status(
            self._config['base_url']), 200)






