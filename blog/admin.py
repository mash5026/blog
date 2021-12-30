from django.contrib import admin
from django.contrib.admin import decorators, filters
from django.contrib.auth.models import update_last_login
from django.db import models
from .models import Post, Comment, Tag, Category
from django.contrib import messages
from .utils import ACCEPT, REJECT

# Register your models here.

@admin.action(description="منتشر کردن پست ها")
def make_publish(modeladmin,request, queryset):
    updated = queryset.update(status=True)
    messages.success("{}پست منتشر گردید.".format(updated))

@admin.action(description="حذف پست ها از سایت")
def make_unpublish(modeladmin,request,queryset):
    updated = queryset.update(status=False)
    messages.success("{} پست از سایت خارج گردید".format(updated))


@admin.action(description="نمایش کاربر کامنت ها")
def make_unshow_user_comments(modeladmin,request,queryset):
    updated = queryset.update(is_hidden=False)
    messages.success("{} کاربر مخفی گردید".format(updated))


@admin.action(description="عدم نمایش کاربر کامنت ها")
def make_show_user_comments(modeladmin,request,queryset):
    updated = queryset.update(is_hidden=True)
    messages.success("{} کاربر نمایش داده شد".format(updated))

@admin.action(description="نمایش دسته ی کامنت ها")
def make_accept_comments(modeladmin,request,queryset):
    updated = queryset.update(status=ACCEPT)
    messages.success("{} کامنت منتشر شد".format(updated))

@admin.action(description="رد کردن کامنت ها")
def make_reject_comments(modeladmin,request,queryset):
    updated = queryset.update(status=REJECT)
    messages.success("{} کامنت رد گردید".format(updated))
    

class CommentPostInlineblock(admin.TabularInline):
    model = Comment
    extra = 2


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('get_image','title','get_date','author','category','status')
    list_filter = ('status','created','author')
    search_fields = ('title','author__username','author__firstname','body')
    list_editable = ('category','status')
    list_display_links = ('title','author')
    list_per_page = 2
    sortable_by = ('title','author')
    actions = [make_publish,make_unpublish]
    inlines = (CommentPostInlineblock,)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_dislay = ('title',)
    list_filter = ('title',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_dislay = ('title',)
    list_filter = ('title',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=('body','post','user','is_hidden','status')
    list_filter = ('post','user','status')
    search_fields = ('post','user','body')
    readonly_fields = ('post','user','body')
    actions = [make_unshow_user_comments,make_show_user_comments,make_accept_comments,make_reject_comments]

