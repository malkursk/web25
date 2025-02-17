from django import forms  
from my.models import *  


class NewsForm(forms.ModelForm):  
    class Meta:  
        model = News
        fields = "__all__"        