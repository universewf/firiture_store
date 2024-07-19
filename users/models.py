from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to="users_images", blank=True, null=True, verbose_name="Аватар")

    class Meta:
        db_table = "user"  # как отображать модель в БД
    verbose_name = "Пользователя"  # название категории в ед.числе
    verbose_name_plural = "Пользователи"  # название категории в мн.числе


    def __str__(self):
        return self.username  # отображение названия queryseta
