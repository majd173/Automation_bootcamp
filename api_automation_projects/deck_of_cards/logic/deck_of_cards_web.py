import logging
from api_automation_projects.deck_of_cards.infra.API_Wrapper import APIWrapper
from api_automation_projects.deck_of_cards.infra.config_provider import ConfigProvider
from api_automation_projects.deck_of_cards.infra.logger_setup import LoggingSetup


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
        try:
            get_back_of_card_status = self.get_back_of_card().status_code
            logging.info("Status request have been got.")
            return get_back_of_card_status
        except Exception:
            logging.error("Can not get status request.")
    #--------------------------------------------------------------------------------------
    # GET REQUEST
    def shuffle_the_cards(self):
        try:
            return self._request.get_request(
                f'{self._url}/api/deck/new/shuffle/?deck_count=1')
        except Exception:
            logging.error("Can not get a request.")

    def shuffle_the_cards_get_json(self):
        try:
            shuffle_the_cards_json = self.shuffle_the_cards().json()
            data = shuffle_the_cards_json
            logging.info("json request have been got.")
            return data['remaining']
        except Exception:
            logging.error("Can not get json request.")

    def shuffle_the_cards_get_status(self):
        try:
            shuffle_the_cards_status = self.shuffle_the_cards().status_code
            logging.info("Status request have been got.")
            return shuffle_the_cards_status
        except Exception:
            logging.error("Can not get status request.")
    #--------------------------------------------------------------------------------------
    # POST REQUEST
    def draw_a_card(self):
        try:
            return self._request.post_request(
                f'{self._url}/api/deck/new/draw/?count=2')
        except Exception:
            logging.error("Can not post a request.")

    def draw_a_card_get_json(self):
        try:
            draw_a_card_json = self.draw_a_card().json()
            data = draw_a_card_json
            logging.info("json request have been got.")
            return data['remaining']
        except Exception:
            logging.error("Can not get json request.")

    def draw_a_card_get_status(self):
        try:
            draw_a_card_status = self.draw_a_card().status_code
            logging.info("Status request have been got.")
            return draw_a_card_status
        except Exception:
            logging.error("Can not get status request.")

    #--------------------------------------------------------------------------------------
    # GET REQUEST
    def a_partial_deck(self):
        try:
            return self._request.get_request(
                f'{self._url}/api/deck/new/shuffle/?cards={self._config["cards"]}')
        except Exception:
            logging.error("Can not get a request.")

    def a_partial_deck_get_json(self):
        try:
            a_partial_deck_json = self.a_partial_deck().json()
            data = a_partial_deck_json
            logging.info("json request have ben got.")
            return data['remaining']
        except Exception:
            logging.error("Can not get json request.")

    def a_partial_deck_get_status(self):
        try:
            a_partial_deck_status = self.a_partial_deck().status_code
            logging.info("Status request have ben got.")
            return a_partial_deck_status
        except Exception:
            logging.error("Can not get status request.")
    #--------------------------------------------------------------------------------------
