from django.contrib import admin
from goods.models import Categories, Products


@admin.register(Categories) #регистрируем модели
class CategoriesAdmin(admin.ModelAdmin): #создание слага по названию
    prepopulated_fields = {"slug":("name",)}


@admin.register(Products)#регистрируем модели
class ProductsAdmin(admin.ModelAdmin): #создание слага по названию
    prepopulated_fields = {"slug":("name",)}