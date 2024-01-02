import json
from channels.generic.websocket import WebsocketConsumer
import requests

def handle_search(query, limit, offset):
    try:
        url = f"https://www.mediawiki.org/w/api.php?action=query&format=json&prop=info&iwurl=1&continue=&generator=search&formatversion=2&inprop=url&gsrsearch={query}&gsrlimit={limit}&gsroffset={offset}&gsrinfo=totalhits%7Csuggestion%7Crewrittenquery&gsrprop=snippet"
        res = requests.get(url)
        data = res.json()

        has_more = "continue" in data
        total_results = data["query"]["searchinfo"]["totalhits"]
        articles = []

        if "query" in data and "pages" in data["query"]:
            articles = data["query"]["pages"]

        return { 'has_more': has_more, 'total_results': total_results, 'articles': articles }
    except requests.exceptions.RequestException as e:
        return e

class Consumer(WebsocketConsumer):
    def connect(self):
        self.accept()
    def disconnect(self, close_code):
        pass
    def receive(self, text_data):
        data_json = json.loads(text_data)

        if data_json['type'] == 'search' and data_json['query']:
            data = handle_search(data_json['query'], data_json['limit'], data_json['offset'])
            self.send(text_data=json.dumps(data))