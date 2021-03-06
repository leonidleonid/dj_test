from django.contrib import admin
from .models import *


class MoneyMovementAdmin(admin.ModelAdmin):
    list_display = [field.name for field in MoneyMovement._meta.fields]
    list_filter = ['date', 'direction', 'category']

    class Meta:
        model = MoneyMovement


class MMPlanAdmin(admin.ModelAdmin):
    list_display = [field.name for field in MMPlan._meta.fields]
    list_filter = ['direction']

    class Meta:
        model = MMPlan


admin.site.register(MoneyMovement, MoneyMovementAdmin)
admin.site.register(MMPlan, MMPlanAdmin)
