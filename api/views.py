from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import json

def handle_search(query, limit, offset):
    try:
        url = f"https://en.wikipedia.org/w/api.php?action=query&format=json&prop=info&iwurl=1&continue=&generator=search&formatversion=2&inprop=url&gsrsearch={query}&gsrlimit={limit}&gsroffset={offset}&gsrinfo=totalhits%7Csuggestion%7Crewrittenquery&gsrprop=snippet"
        res = requests.get(url)
        data = res.json()

        has_more = "continue" in data
        total_results = data["query"]["searchinfo"]["totalhits"]
        articles = []

        if "query" in data and "pages" in data["query"]:
            articles = data["query"]["pages"]

        return { 'has_more': has_more, 'total_results': total_results, 'articles': articles }
    except requests.exceptions.RequestException as e:
        return { 'error': e }

@api_view(['POST'])
def search(request):
    body = json.loads(request.body.decode("utf-8"))
    response = handle_search(body['query'], body['limit'], body['offset'])
    return Response(response)