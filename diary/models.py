from django.db import models

from users.models import CustomUser


# Create your models here.

class Record(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=150, verbose_name='Название заметки',
                                help_text='Введите название заметки', blank=True, null=True)
    note = models.TextField(verbose_name='Заметка о дне', help_text='Введите запись в дневник')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания',
                                      help_text='Введите дату создания', blank=True)

    def __str__(self):
        return f'{self.name} {self.created_date}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        ordering = ['name', 'note']