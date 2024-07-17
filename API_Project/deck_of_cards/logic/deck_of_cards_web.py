from API_Project.deck_of_cards.infra.API_Wrapper import APIWrapper


class APIDecksOfCards:

    def __init__(self, request: APIWrapper):
        self._request = request


    def get_back_of_card(self, url):
        return self._request.get_request(f'{url}/static/img/back.png')

    def shuffle_the_cards(self, url, count=1):
        return self._request.get_request(f'{url}/api/deck/new/shuffle/?deck_count={count}')

    # def shuffle_cards_get_json(self, url, i):
    #     return self.shuffle_the_cards(f'{url}/api/deck/new/shuffle/?deck_count={i}').json()

    def draw_a_card(self, url, i):
        return self._request.post_request(f'{url}/api/deck/{i}/draw/?count=2')

    # def draw_a_card_get_json(self, url, i):
    #     return self.draw_a_card(f'{url}/api/deck/{i}/draw/?count=2').json()
    #
    #
    # def draw_a_card_get_status(self, url, i):
    #     return self.draw_a_card(f'{url}/api/deck/{i}/draw/?count=2').status_code



