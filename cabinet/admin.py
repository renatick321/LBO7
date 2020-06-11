from django.contrib import admin
from .models import User, Post
# Register your models here.
admin.site.register(User)
admin.site.register(Post)


#==============================
from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from .models import Test

admin.site.register(Test)