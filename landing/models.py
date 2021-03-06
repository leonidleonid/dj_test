from django.db import models
from django.utils.timezone import now


class MoneyMovement(models.Model):
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    date = models.DateField(default=now)
    purpose = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    direction = models.CharField(max_length=10)
    comment = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True)
    changed = models.DateField(auto_now=True)

    def __str__(self):
        if self.direction not in ('income', 'cost'):
            return 'Wrong direction!'
        dir_string = 'Поступление' if self.direction == 'income' else 'Расход'
        return '%s (%s) на %s руб. от %s' % (dir_string, self.purpose, self.amount, str(self.date))

    class Meta:
        ordering = ['date', 'id']


class MMPlan(models.Model):
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    purpose = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    direction = models.CharField(max_length=10)
    comment = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True)
    changed = models.DateField(auto_now=True)

    def __str__(self):
        if self.direction not in ('income', 'cost'):
            return 'Wrong direction!'
        dir_string = 'Поступление' if self.direction == 'income' else 'Расход'
        return '%s (%s) на %s руб.' % (
            dir_string, self.purpose, self.amount
        )

    class Meta:
        ordering = ['id']
