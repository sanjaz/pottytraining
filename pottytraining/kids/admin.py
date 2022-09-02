from django.contrib import admin

from pottytraining.kids.models import Kid, PeeOrPoo


@admin.register(Kid)
class KidAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gender', 'birth_date')


@admin.register(PeeOrPoo)
class PeeOrPooAdmin(admin.ModelAdmin):
    list_display = ('kid', 'time', 'is_poo')
