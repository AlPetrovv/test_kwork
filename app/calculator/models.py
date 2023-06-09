
from django.db import models
from django.utils.text import gettext_lazy as _


class Problem(models.Model):
    amount = models.BigIntegerField(_("Сумма"), null=True)
    is_active = models.BooleanField(_("Активна"), default=True)

    def __str__(self):
        return f"Задача № {self.id}"

    class Meta:
        verbose_name = "Задачи"
        verbose_name_plural = 'Задач'
