from django.db import models


class PriceCard(models.Model):
    pc_value = models.CharField(max_length=10, verbose_name='Ціна')
    pc_description = models.CharField(max_length=200, verbose_name='Опис')

    def __str__(self):
        return self.pc_value

    class Meta:
        verbose_name = 'Ціну'
        verbose_name_plural = 'Ціни'


class PriceTable(models.Model):
    pt_title = models.CharField(max_length=200, verbose_name='Послуга')
    pt_old_price = models.CharField(max_length=10, verbose_name='Стара ціна')
    pt_new_price = models.CharField(max_length=10, verbose_name='Нова ціна')

    def __str__(self):
        return self.pt_title

    class Meta:
        verbose_name = 'Послугу'
        verbose_name_plural = 'Послуги'
