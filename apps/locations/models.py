from django.db import models
from django.utils import timezone
from django.core import validators
from django.core.exceptions import ValidationError
# Create your models here.



class Locations(models.Model):
    title = models.CharField(max_length=50,verbose_name="عنوان مکان")
    description = models.TextField(verbose_name="توضیحات")
    image_name = models.ImageField(upload_to='images/locations/',verbose_name="تصویر")
    visiting_days = models.CharField(max_length=20,verbose_name="روز بازدید")
    visiting_hours = models.CharField(max_length=20,verbose_name="ساعت بازدید")
    ruls = models.TextField(verbose_name="قوانین و مقررات")
    register_date = models.DateField(default=timezone.now,verbose_name=" تاریخ ثبت")

    def __str__(self):
        return self.title
    
    class Meta :
        verbose_name = 'مکان'
        verbose_name_plural = 'مکان ها'
# -------------------------------------------------------------------------------------------
class VisitorType(models.Model):
    name = models.CharField(max_length=20,verbose_name= "نام نوع بازدید کننده")

    def __str__(self):
        return self.name
    
    class Meta :
        verbose_name = 'نوع بازدید کننده'
        verbose_name_plural = 'نوع بازدید کننده ها'
# -------------------------------------------------------------------------------------------
class Ticket(models.Model) :
    visitortype = models.ForeignKey(VisitorType,on_delete=models.CASCADE,verbose_name="نوع بازدید کننده")
    location = models.ForeignKey(Locations,on_delete=models.CASCADE,verbose_name="مکان ")
    price = models.IntegerField(default=0,verbose_name="قیمت بلیط")

    def __str__(self):
        return f"{self.visitortype}\t{self.location}"
    
    class Meta :
        verbose_name = 'بلیط'
        verbose_name_plural = 'بلیط ها'
# -------------------------------------------------------------------------------------------
# def validate_subject(value):
#     if not value.isalpha() :
#         raise ValidationError("عنوان را درست وارد کنید")

class Contact(models.Model):
    full_name = models.CharField(max_length=20,verbose_name="نام و نام خانوادگی")
    email = models.CharField(max_length=30,
                              verbose_name="ایمیل",
                              validators=[validators.EmailValidator(message="آدرس ایمیلی که وارد کرده اید معتبر نیست")]
                              )
    subject = models.CharField(max_length=20,
                            #    validators=[validate_subject],
                               verbose_name="عنوان")
    message = models.TextField(max_length=300,verbose_name="متن پیام")
    is_seen = models.BooleanField(default=False,verbose_name="وضعیت مشاهده")
    register_date = models.DateField(default=timezone.now,verbose_name="تاریخ ثبت پیام")

    def __str__(self):
        return f"{self.full_name}\t{self.subject}"
    
    class Meta:
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام ها'
# -------------------------------------------------------------------------------------------
