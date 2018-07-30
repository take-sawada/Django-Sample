from django.shortcuts import render

# Create your views here.

# TemplateResponseクラスのインポート
from django.template.response import TemplateResponse

# hello()関数
def hello(request):

    # テンプレートに渡す辞書
    context = {'message': 'メッセージ'}
    return TemplateResponse(request, 'books/message.html', context=context)

