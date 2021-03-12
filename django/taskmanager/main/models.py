from django.db import models

class Sushi(models.Model):
    title = models.CharField('Суши', max_length=50)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title
# менять название
    class Meta:
        verbose_name = 'Суши'
        verbose_name_plural = 'Суши'