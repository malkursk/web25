from django.db import models

class News(models.Model):
    caption = models.CharField('заголовок', max_length=100)
    full_text = models.TextField('текст')
    last_name = models.CharField('фамилия', max_length=30)
    address = models.CharField('адрес', max_length=60)
    phone_number = models.CharField('телефон', max_length=12)
    is_public = models.BooleanField('секретно', default=False)
    updated_at = models.DateTimeField(auto_now=True)    
    class Meta:
        db_table = "news"
        ordering = ['-updated_at']
