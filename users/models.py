from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    first_name = models.CharField(
        max_length=30, blank=True, null=True, verbose_name="Имя"
    )
    last_name = models.CharField(
        max_length=30, blank=True, null=True, verbose_name="Фамилия"
    )
    snils = models.CharField(max_length=30, blank=True, null=True, verbose_name="Снилс")

    email = models.EmailField(
        unique=True,
        verbose_name="Email",
    )
    avatar = models.ImageField(
        upload_to="users/",
        blank=True,
        null=True,
        verbose_name="Аватар",
    )
    phone = models.CharField(
        max_length=11,
        blank=True,
        null=True,
        verbose_name="Номер телефона",
    )
    city = models.CharField(max_length=50, blank=True, null=True, verbose_name="Город")
    token = models.CharField(
        max_length=150, verbose_name="Токен", blank=True, null=True
    )
    is_active = models.BooleanField(blank=True, null=True)
    tg_id = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Telegram ID"
    )
    country = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Гражданство"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Feedback(models.Model):
    phone_number = models.CharField(max_length=20, verbose_name="Ваш номер телефона")
    question = models.TextField(verbose_name="Ваш вопрос")
    contact_time = models.CharField(
        max_length=50, verbose_name="Когда с вами связаться?"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.phone_number} at {self.created_at}"
