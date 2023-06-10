from django.db import models
import datetime

class Articles(models.Model):
    title = models.CharField('ФИО', max_length=50)
    anons = models.CharField('Level', max_length=50)
    full_text = models.TextField('Сообщение')
    date = models.DateField('Время', default=datetime.datetime.now, blank=True)
    year = models.TextField('Возраст')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.title




