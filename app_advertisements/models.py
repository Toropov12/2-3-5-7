from django.db import models
class Advertisements(models.Model):
    title = models.CharField("Заголовок", max_length=128)
    discription = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits= 10, decimal_places=2)
    auction = models.BooleanField("Торг")
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    update_at = models.DateTimeField("Дата обнавления", auto_now=True)
# Create your models here.
