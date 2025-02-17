from django.db import models

class News(models.Model):
    caption = models.CharField('заголовок новости', max_length=100)
    full_text = models.TextField('полный текст новости', default=1)
    last_name = models.CharField('фамилия', max_length=50)
    address = models.CharField('адрес', max_length=70)
    phone_namber  = models.CharField('номер телефона', max_length=27)
    is_public = models.BooleanField('для открытой печати', default=False)
    updated_at = models.DateTimeField(auto_now=True)    
    class Meta :
        db_table = "news"
        ordering = ['-updated_at']
