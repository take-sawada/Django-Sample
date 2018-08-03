from django.db import models

# Create your models here.
class Book(models.Model):
    """
    書籍を表すモデル
    """
    name = models.CharField('名前', max_length=255)
    image_url = models.URLField('画像URL', blank=True)
    price = models.FloatField('価格', default=0)
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)    
    

class Review(models.Model):
    """
    書籍のレビューを表すモデル
    """
    user = models.ForeignKey(User)
    book = models.ForeignKey(Book)
    rating = models.integerField('レーティング')
    comment = models.TextField('コメント')
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)

