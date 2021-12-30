from django.contrib.auth.models import User, update_last_login
from django.db import models
from .utils import get_image_path,image_size,CHOICES_LIST, get_file_path
from django_jalali.db import models as jmodels

# Create your models here.

class Log(models.Model):
    created = jmodels.jDateTimeField(auto_now_add=True)
    description = models.TextField()

    class Meta:
        verbose_name='لاگ'
        verbose_name_plural='لاگ ها'

class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name="کاربر", on_delete=models.CASCADE, related_name='profile')
    age = models.PositiveSmallIntegerField(verbose_name='سن', null=True)
    bio = models.TextField(verbose_name="درباره من", null=True, blank=True)
    phone = models.CharField(verbose_name="شماره همراه", max_length=11, null=True, blank=True, help_text="شماره همراه با صفر وارد شود")
    avatar = models.ImageField(verbose_name="تصویر کاربر", upload_to=get_image_path, validators=[image_size])
    gender = models.CharField(verbose_name="جنسیت", max_length=10, choices=CHOICES_LIST)
    nc = models.CharField(verbose_name="کدملی", max_length=10, null=True)
    resume = models.FileField(verbose_name='رزومه', null=True, upload_to=get_file_path)
    is_author = models.BooleanField(verbose_name='نوسینده می باشد؟', default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name='کاربری'
        verbose_name_plural='کاربری ها'