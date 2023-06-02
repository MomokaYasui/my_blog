from django.http import HttpResponse
from random import choice

def index(request):

    omikuji=["凶","吉","大吉","中吉"]

    result=choice(omikuji)

    responseobject=HttpResponse(result)
    return responseobject