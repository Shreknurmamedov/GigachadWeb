from django.db import models



class State(models.Model):
    team1 = models.CharField('1team', max_length=50, default='')
    team2 = models.CharField('2team', max_length=50, default='')
    score1 = models.CharField('score1', max_length=50, default='')
    score2 = models.CharField('score2', max_length=50, default='')
    map = models.TextField('map', default='')
    date = models.DateTimeField('Время')


    class Meta:
        verbose_name = 'Матч'
        verbose_name_plural = 'Матчи'

    def __str__(self):
        return self.team1
