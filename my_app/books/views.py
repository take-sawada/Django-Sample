from django.shortcuts import render

# Create your views here.
from django.template.response import TemplateResponse

def hello(request):

    context = {
        'headers': {
            'scheme': request.scheme,
            'path': request.path,
            'method': request.method,
            'content_length': request.META['CONTENT_LENGTH'],
            'http_accept': request.META['HTTP_ACCEPT'],
            'http_accept_language': request.META['HTTP_ACCEPT_LANGUAGE'],
            'user_agent': request.META['HTTP_USER_AGENT'],
            'remote_addr': request.META['REMOTE_ADDR'],
        }
    }

    return TemplateResponse(request, 'books/header.html', context)
