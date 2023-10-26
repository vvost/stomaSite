from django.contrib import admin
from .models import Application
from django.contrib.auth.models import User, Group


admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.site_header = 'Сайт Стоматологии'
admin.site.site_title = 'Сайт Стоматологии'



@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'appointment_date', 'start_time', 'end_time', 'service']
    list_filter = ('appointment_date', 'service')
    search_fields = ('first_name__startswith', 'last_name__startswith', 'appointment_date')
    list_per_page = 10



