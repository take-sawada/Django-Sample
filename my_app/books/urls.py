# url関数()のインポート
from django.conf.urls import url
from . import views

# ルーティングの設定
urlpatterns = [

    # bookの一覧
    url(r'^$', views.index, name='book_index'),

    # bookの登録
    url(r'^(?P<book_id>[0-9]+)/add$', views.add, name='book_add'),

    # bookの更新
    url(r'^(?P<book_id>[0-9]+)/edit$', views.edit, name='book_edit'),

    # bookの削除
    url(r'^(?P<book_id>[0-9]+)/delete/$', views.delete, name='book_delete'),

]
