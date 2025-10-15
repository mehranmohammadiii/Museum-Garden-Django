from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Memory(models.Model):
    title = models.CharField(max_length=50,verbose_name='عنوان')
    text = models.TextField(max_length=500,verbose_name='متن')
    register_date = models.DateField(default=timezone.now,verbose_name='تاریخ ثبت')
    is_active = models.BooleanField(default=False,verbose_name='وضعیت')
    user_register = models.ForeignKey(User,on_delete=models.CASCADE,null=True,verbose_name='کابر ثبت کننده')

    def __str__(self):
        return self.title
    
    class Meta :
        verbose_name = 'خاطره '
        verbose_name_plural = ' خاطره  ها'
# ------------------------------------------------------------------------------------

class MemoryGallery(models.Model):
    image_name = models.ImageField(upload_to='images/memories',verbose_name='تصویر')
    memory = models.ForeignKey(Memory,on_delete=models.CASCADE,verbose_name='خاطره',related_name='gallery_images')