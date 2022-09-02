from django.contrib import admin

from pottytraining.kids.models import Kid


@admin.register(Kid)
class KidAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gender', 'birth_date')
