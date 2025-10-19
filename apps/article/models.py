from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=15,verbose_name="نام")
    family = models.CharField(max_length=15,verbose_name="نام خانوادگی")
    email = models.EmailField(max_length=50,null=True,blank=True,verbose_name="ایمیل")
    mobile = models.CharField(max_length=11,verbose_name="موبایل")
    is_active = models.BooleanField(default=False,verbose_name="وضعیت")
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return f"{self.name}\t{self.family}"
    
    class Meta :
        verbose_name = 'نویسنده'
        verbose_name_plural = 'نویسنده ها'
# --------------------------------------------------------------------------------------------------
class ArticleType(models.Model):
    name = models.CharField(max_length=20,verbose_name='نام نوع مقاله')

    def __str__(self):
        return self.name
    
    class Meta :
        verbose_name = 'نوع مقاله'
        verbose_name_plural = 'نوع مقاله ها'
# --------------------------------------------------------------------------------------------------
class Article(models.Model):
    author = models.ManyToManyField(Author,verbose_name="نوسینده")
    articletype = models.ForeignKey(ArticleType,on_delete=models.CASCADE,verbose_name="نوع مقاله")
    subject = models.CharField(max_length=100,verbose_name="عنوان")
    image_name = models.CharField(max_length=200,verbose_name="تصویر")
    short_text = models.TextField(max_length=400,verbose_name="متن خلاصه")
    text = models.TextField(verbose_name="متن")   
    key_words = models.CharField(max_length=100,verbose_name="کلمات کلیدی")
    register_date = models.DateField(auto_now_add=timezone.now,verbose_name="تاریخ ثبت")
    publication_date =models.DateField(default=timezone.now,verbose_name="تاریخ انتشار")
    update_date =models.DateField(auto_now=timezone.now,verbose_name="تاریخ آخرین ویرایش")
    is_active = models.BooleanField(default=False,verbose_name="وضعیت")
    view_number = models.PositiveSmallIntegerField(default=0,verbose_name="تعداد بازدید")
    slug = models.SlugField(max_length=50)
    pdf_file = models.CharField(max_length=200,verbose_name="فایل pdf مقاله")
    likes = models.PositiveSmallIntegerField(verbose_name='تعداد لایک',null=True)

    def __str__(self):
        return self.subject
    
    class Meta :
        verbose_name = 'مقاله '
        verbose_name_plural = ' مقاله ها'
# --------------------------------------------------------------------------------------------------
class ArticleGallery(models.Model):
    name = models.CharField(max_length=100,verbose_name="تصویر")
    article = models.ForeignKey(Article,related_name='gallery_images',on_delete=models.CASCADE,verbose_name="مقاله")

    def __str__(self):
        return self.name
    
    class Meta :
        verbose_name = 'تصویر '
        verbose_name_plural = ' تصویر ها'
# --------------------------------------------------------------------------------------------------
class ArticleLike(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='کاربر')
    article = models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name='مقاله')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}/t{self.article}'

    class Meta :
        verbose_name = 'لایک '
        verbose_name_plural = ' لایک ها'
        unique_together = ('user','article')