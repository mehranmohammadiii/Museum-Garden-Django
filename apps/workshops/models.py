from django.db import models
from django.utils import timezone


class WorkshopStatus(models.Model):
    status_name = models.CharField(max_length=20,verbose_name='وضعیت کارگاه')
    def __str__(self):
        return self.status_name
    
    class Meta :
        verbose_name = 'وضصعیت'
        verbose_name_plural = 'وضعیت ها'
# ----------------------------------------------------------------------------
class Workshop(models.Model):
    status = models.ForeignKey(WorkshopStatus,on_delete=models.CASCADE,verbose_name='وضعیت')
    title = models.CharField(max_length=50,verbose_name='عنوان')
    image_name = models.ImageField(upload_to='images/workshop',verbose_name='تصویر')
    datetime_holding = models.DateTimeField(verbose_name='تازیخ و زمان برگزاری')
    place = models.CharField(max_length=50,verbose_name='مکان برگزاری')
    teacher = models.CharField(max_length=20,verbose_name='نام مدرس')
    information = models.TextField(max_length=400,verbose_name='اطلاعات')
    registration = models.TextField(max_length=400,verbose_name='شرایط ثبت نام')
    report_text = models.TextField(max_length=400,null=True,blank=True,verbose_name='متن گزارش')
    view_number = models.PositiveSmallIntegerField(default=0,verbose_name='تعداد بازدید')
    register_date = models.DateField(default=timezone.now,verbose_name='تاریخ ثبت')
    is_active = models.BooleanField(default=False,verbose_name='وضعیت')

    def __str__(self):
        return self.title

    class Meta :
        verbose_name = 'کارگاه'
        verbose_name_plural = 'کارگاه ها'
# ----------------------------------------------------------------------------
class WorkshopGallery(models.Model):
    workshop = models.ForeignKey(Workshop,related_name='gallery_images',on_delete=models.CASCADE,verbose_name='کارگاه')
    image = models.ImageField(upload_to='images/workshop',verbose_name='تصویر')

    def __str__(self):
        return self.image.name

    class Meta :
        verbose_name = 'تصویر'
        verbose_name_plural = 'تصویر ها'  