from django.db import models
from django.core.validators import MinValueValidator

class Food(models.Model):
    # 更新单位选择为您需要的单位
    UNIT_CHOICES = (
        ('kg', 'Kilogram'),  # 千克
        ('L', 'Liter'),      # 升
        ('枚', 'Pieces'),    # 枚，用于不规则计数的物品，如鸡蛋等
    )

    name = models.CharField(max_length=100)
    quantity = models.FloatField(validators=[MinValueValidator(0.01)])
    carbon_footprint = models.FloatField(validators=[MinValueValidator(0)])
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES, default='kg')

    def __str__(self):
        return f"{self.name} - {self.quantity} {self.unit}"


class WishList(models.Model):
    name = models.CharField(max_length=100)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name