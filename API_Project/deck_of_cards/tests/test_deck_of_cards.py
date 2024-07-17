import unittest
from API_Project.deck_of_cards.infra.config_provider import ConfigProvider
from API_Project.deck_of_cards.logic.deck_of_cards_web import APIDecksOfCards
from API_Project.deck_of_cards.infra.API_Wrapper import APIWrapper


class TestDeckOfCards(unittest.TestCase):


    config = ConfigProvider().load_from_file("../cards_config.json")

    def test_back_of_cards(self):
        api_request = APIWrapper()
        api_deck_of_cards = APIDecksOfCards(api_request)
        result = api_deck_of_cards.get_back_of_card(self.config['base_url'])
        self.assertEqual(result.status_code, 200)
        self.assertTrue(result.ok)


    def test_shuffle_the_cards(self):
        api_request = APIWrapper()
        api_deck_of_cards = APIDecksOfCards(api_request)
        self.assertEqual(api_deck_of_cards.shuffle_the_cards(self.config['base_url'], 1).json()["remaining"], 52)
        self.assertTrue(api_deck_of_cards.shuffle_the_cards(self.config['base_url']).ok)


    def test_draw_a_card(self):
        api_request = APIWrapper()
        api_deck_of_cards = APIDecksOfCards(api_request)
        self.assertTrue(api_deck_of_cards.draw_a_card(self.config['base_url'], "new").ok)
        self.assertNotEqual(api_deck_of_cards.draw_a_card(self.config['base_url'], "50").status_code, 200)



