from django.contrib import admin
from diary.models import Record

# Register your models here.
@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner', 'note', 'created_date')
    list_filter = ('name', 'note',)
    search_fields = ('name', 'note')
