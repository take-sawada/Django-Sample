# url関数()のインポート
from django.conf.urls import url

from . import views

# ルーティングの設定
urlpatterns = [
    url(r'^hello/$', views.hello, name='hello'),
]
