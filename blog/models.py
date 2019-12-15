from django.conf import settings
from django.db import models

class FB(models.Model):
    email = models.CharField(verbose_name="Электронный адрес", max_length=50)
    text = models.TextField(verbose_name="Текст отзыва")
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
    def __str__(self):
        return self.email