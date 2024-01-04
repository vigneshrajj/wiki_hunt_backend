from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from api.consumers import handle_search

@api_view(['POST'])
def search(request):
    body = json.loads(request.body.decode("utf-8"))
    response = handle_search(body['query'], body['limit'], body['offset'])
    return Response(response)