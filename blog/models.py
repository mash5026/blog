from re import T
from django.db import models
from django.utils.safestring import mark_safe
from django_jalali.db import models as jmodels
from .utils import get_image_path,image_size, CHOICES_LIST_COMMENT,PENDING
from accounts.models import Profile
from django.utils.text import slugify
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Post(models.Model):
    slug = models.SlugField(verbose_name="پیوند یکتا", allow_unicode=True, null=True, blank=True)
    title = models.CharField(verbose_name="موضوع", max_length=25, unique=True)
    body = RichTextUploadingField(verbose_name="متن اصلی", null=True, blank=True)
    created = jmodels.jDateTimeField(verbose_name="تاریخ ثبت", auto_now_add=True)
    updated = jmodels.jDateTimeField(verbose_name="تاریخ بروزرسانی", auto_now=True)
    author = models.ForeignKey(Profile, verbose_name="نویسنده", on_delete=models.SET_NULL, null=True, blank=True, related_name='posts')
    image = models.ImageField(verbose_name="تصویر",null=True, blank=True, upload_to=get_image_path, validators=[image_size])
    status = models.BooleanField(verbose_name="منتشر شده", default=True)
    category = models.ForeignKey('Category', verbose_name="دسته بندی", on_delete=models.CASCADE, related_name='posts')
    tag = models.ManyToManyField('Tag', verbose_name="تگ", blank=True, related_name='posts')


    class Meta:
        verbose_name = ' پست'
        verbose_name_plural = ' پست ها'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_image(self):
        if self.image:
            return mark_safe('<img src="{}" alt="{}" width="100" height="100">'.format(self.image.url, self.title))
        else:
            return mark_safe('<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/No-Image-Placeholder.svg/1665px-No-Image-Placeholder.svg.png" width="100" height="100">')
    get_image.short_description = "عکس مربوط به پست"

    def get_date(self):
        return self.created.strftime('در ساعت %H:%m و درتاریخ %Y/%m/%d')
    get_date.short_description = 'ثبت شده در'

    def get_absolute_url(self):
        return reverse("blog:details", kwargs={"slug": self.slug})
    
    def get_accept_comments_count(self):
        return self.comments.filter(status=0).count()


class Category(models.Model):
    title = models.CharField(verbose_name="دسته بندی", max_length=15, null=True, blank=True)


    class Meta:
        verbose_name = '  دسته بندی'
        verbose_name_plural= '  دسته بندی ها'

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(verbose_name="تگ", max_length=15, null=True, blank=True)


    class Meta:
        verbose_name = '   تگ'
        verbose_name_plural = '   تگ ها'

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(Profile, verbose_name="کاربر", on_delete=models.CASCADE, null=True, blank=True, related_name='comments')
    post = models.ForeignKey(Post, verbose_name="پست", on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    status = models.PositiveSmallIntegerField(verbose_name="وضعیت", choices=CHOICES_LIST_COMMENT, default=PENDING)
    is_hidden = models.BooleanField(verbose_name="عدم مشاهده", default=True)


    class Meta:
        verbose_name = '    کامنت'
        verbose_name_plural = '    کامنت ها'

    def __str__(self):
        return self.user.user.username + "<<<>>>" + self.body + "<<<>>>" + self.post.title