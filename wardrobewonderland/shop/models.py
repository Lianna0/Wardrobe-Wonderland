from django.contrib.auth.models import AbstractUser
from django.db import models


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Category(TimeStampModel):
    name = models.CharField(max_length=20, unique=True)
    image = models.ImageField(upload_to='category_img/')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class SubCategory(TimeStampModel):
    name = models.CharField(max_length=40, unique=True)
    image = models.ImageField(upload_to='subcategory_img/')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'SubCategory'
        verbose_name_plural = 'SubCategories'


class Item(TimeStampModel):
    name = models.CharField(max_length=40, unique=True)
    image = models.ImageField(upload_to='item_img/')
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='sub_category')

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def __str__(self):
        return self.name


# class User(AbstractUser):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     email = models.EmailField('Email address',
#                               max_length=50,
#                               unique=True,
#                               null=True,
#                               blank=False)
#
#     email_is_verified = models.BooleanField(default=False)
#     password = models.CharField(max_length=15)
#     is_active = models.BooleanField(default=False)
#
#     stripe_customer_id = models.CharField(null=True,
#                                           blank=True,
#                                           max_length=255)
#
#     stripe_account_id = models.CharField(blank=True,
#                                          null=True,
#                                          max_length=256)
#
#     created_at = models.DateTimeField(auto_now=True)
#     updated_at = models.DateTimeField(auto_now_add=True)
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ''
#
#     objects = UserManager()
