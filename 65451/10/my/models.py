from django.db import models

class News(models.Model):
    caption = models.CharField('заголовок новости', max_length=100)
    is_public = models.BooleanField('для открытой печати', default=False)
    updated_at = models.DateTimeField(auto_now=True)
    text = models.TextField()    
    class Meta :
        db_table = "news"
        ordering = ['-updated_at']
