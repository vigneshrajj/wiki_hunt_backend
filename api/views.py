from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from consumers import handle_search

@api_view(['GET'])
def search_article(request):
    try:
        query = request.GET.get('query')
        url = f"https://www.mediawiki.org/w/api.php?action=query&format=json&prop=info&iwurl=1&continue=&generator=search&formatversion=2&inprop=url&gsrsearch={query}&gsrlimit=10&gsroffset=0&gsrinfo=totalhits%7Csuggestion%7Crewrittenquery&gsrprop=snippet"
        res = requests.get(url)
        data = res.json()
        has_more = "continue" in data
        total_results = data["query"]["searchinfo"]["totalhits"]
        articles = data["query"]["pages"]
        return Response({ 'has_more': has_more, 'total_results': total_results, 'articles': articles })
    except requests.exceptions.RequestException as e:
        return e

@api_view(['POST'])
def search(request):
    print(request.body)
    return Response({ 'message': 'works' })