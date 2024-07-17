import logging
from API_Project.deck_of_cards.infra.API_Wrapper import APIWrapper
from API_Project.deck_of_cards.infra.config_provider import ConfigProvider
from API_Project.deck_of_cards.infra.logger_setup import LoggingSetup


class APIDecksOfCards:

    def __init__(self, request: APIWrapper):
        try:
            self._request = request
            self._api = APIWrapper()
            self._config = ConfigProvider().load_from_file("../cards_config.json")
            self._url = self._config['base_url']
        except ImportError:
            logging.error("Can not open card_config.json file.")



    # --------------------------------------------------------------------------------------
    # GET REQUEST
    def get_back_of_card(self):
        try:
            return self._request.get_request(
                f'{self._url}/static/img/back.png')
        except Exception:
            logging.error("Can not get a request.")

    def get_back_of_card_get_status(self):
        get_back_of_card_status = self.get_back_of_card().status_code
        return get_back_of_card_status

    #--------------------------------------------------------------------------------------
    # GET REQUEST
    def shuffle_the_cards(self):
        return self._request.get_request(
            f'{self._url}/api/deck/new/shuffle/?deck_count=1')

    def shuffle_the_cards_get_json(self):
        shuffle_the_cards_json = self.shuffle_the_cards().json()
        data = shuffle_the_cards_json
        return data['remaining']

    def shuffle_the_cards_get_status(self):
        shuffle_the_cards_status = self.shuffle_the_cards().status_code
        return shuffle_the_cards_status

    #--------------------------------------------------------------------------------------
    # POST REQUEST
    def draw_a_card(self):
        return self._request.post_request(
            f'{self._url}/api/deck/new/draw/?count=2')

    def draw_a_card_get_json(self):
        draw_a_card_json = self.draw_a_card().json()
        data = draw_a_card_json
        return data['remaining']

    def draw_a_card_get_status(self):
        draw_a_card_status = self.draw_a_card().status_code
        return draw_a_card_status

    #--------------------------------------------------------------------------------------
    # GET REQUEST
    def a_partial_deck(self):
        return self._request.get_request(
            f'{self._url}/api/deck/new/shuffle/?cards={self._config["cards"]}')

    def a_partial_deck_get_json(self):
        a_partial_deck_json = self.a_partial_deck().json()
        data = a_partial_deck_json
        return data['remaining']

    def a_partial_deck_get_status(self):
        a_partial_deck_status = self.a_partial_deck().status_code
        return a_partial_deck_status
    #--------------------------------------------------------------------------------------
