import unittest
import pytest
import logging
from API_Project.deck_of_cards.infra.logger_setup import LoggingSetup
from API_Project.deck_of_cards.infra.config_provider import ConfigProvider
from API_Project.deck_of_cards.logic.deck_of_cards_web import APIDecksOfCards
from API_Project.deck_of_cards.infra.API_Wrapper import APIWrapper



class TestDeckOfCards(unittest.TestCase):

    def setUp(self):
        self._config = ConfigProvider().load_from_file("../cards_config.json")
        self._api = APIWrapper()


    def test_back_of_cards(self):
        logging.info("_______Test (test_back_of_cards) Began_______")
        deck_of_cards = APIDecksOfCards(self._api)
        self.assertTrue(deck_of_cards.get_back_of_card())
        self.assertGreaterEqual(200, deck_of_cards.get_back_of_card_get_status())

    def test_shuffle_the_cards(self):
        logging.info("_______Test (test_shuffle_the_cards) Began_______")
        deck_of_cards = APIDecksOfCards(self._api)
        self.assertTrue(deck_of_cards.shuffle_the_cards().ok)
        self.assertEqual(deck_of_cards.shuffle_the_cards_get_status(), 200)
        self.assertEqual(deck_of_cards.shuffle_the_cards_get_json(), 52)

    def test_draw_a_card(self):
        logging.info("_______Test (test_draw_a_card) Began_______")
        deck_of_cards = APIDecksOfCards(self._api)
        self.assertTrue(deck_of_cards.draw_a_card().ok)
        self.assertEqual(deck_of_cards.draw_a_card_get_status(), 200)
        self.assertEqual(deck_of_cards.draw_a_card_get_json(), 51)


    def test_a_partial_deck(self):
        logging.info("_______Test (test_a_partial_deck) Began_______")
        deck_of_cards = APIDecksOfCards(self._api)
        self.assertTrue(deck_of_cards.a_partial_deck().ok)
        self.assertEqual(deck_of_cards.a_partial_deck_get_status(), 200)
        self.assertEqual(deck_of_cards.a_partial_deck_get_json(), 8)




