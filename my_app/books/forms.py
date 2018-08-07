# ModelFormのインポート
from django.forms import ModelForm

from .models import Book

# フォームの宣言
class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            'name', 'image_url', 'rating', 'piece_count',
            'minifig_count', 'us_price', 'owner_count', 'want_it_count'
        ]
