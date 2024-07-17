from API_Project.deck_of_cards.infra.API_Wrapper import APIWrapper
from API_Project.deck_of_cards.infra.config_provider import ConfigProvider


class APIDecksOfCards:

    def __init__(self, request: APIWrapper):
        self._request = request
        self._api = APIWrapper()
        self._config = ConfigProvider().load_from_file("../cards_config.json")


    def get_back_of_card(self, url):
        return self._request.get_request(
            f'{url}/static/img/back.png')

    def get_back_of_card_get_status(self, url):
        get_back_of_card_status = self.get_back_of_card(url).status_code
        return get_back_of_card_status

    #--------------------------------------------------------------------------------------

    def shuffle_the_cards(self, url, count=1):
        return self._request.get_request(
            f'{url}/api/deck/new/shuffle/?deck_count={count}')

    def shuffle_the_cards_get_json(self, url, i):
        shuffle_the_cards_json = self.shuffle_the_cards(
            f'{url}/api/deck/new/shuffle/?deck_count={i}').json()
        return shuffle_the_cards_json

    def shuffle_the_cards_get_status(self, url, i):
        shuffle_the_cards_status = self.shuffle_the_cards(
            f'{url}/api/deck/new/shuffle/?deck_count={i}').status_code
        return shuffle_the_cards_status
    #--------------------------------------------------------------------------------------
    def draw_a_card(self, url):
        return self._request.post_request(
            f'{url}/api/deck/new/draw/?count=2')

    def draw_a_card_get_json(self, url):
        draw_a_card_json = self.draw_a_card(
            f'{url}/api/deck/new/draw/?count=2').json()
        return draw_a_card_json

    def draw_a_card_get_status(self, url):
        draw_a_card_status = self.draw_a_card(
            f'{url}/api/deck/new/draw/?count=2').status_code
        return draw_a_card_status
    #--------------------------------------------------------------------------------------


    def a_partial_deck(self, url):
        return self._request.get_request(
            f'{url}/api/deck/new/shuffle/?cards={self._config["cards"]}')

    def a_partial_deck_get_json(self, url):
        a_partial_deck_json = self.a_partial_deck(
            f'{url}/api/deck/new/shuffle/?cards={self._config["cards"]}').json()
        return a_partial_deck_json['remaining']


    def a_partial_deck_get_status(self, url):
        a_partial_deck_status = self.a_partial_deck(
            f'{url}/api/deck/new/shuffle/?cards={self._config["cards"]}').status_code
        return a_partial_deck_status


