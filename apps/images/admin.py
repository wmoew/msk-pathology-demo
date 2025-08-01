from django.contrib import admin
from .models import PathologyImage

@admin.register(PathologyImage)
class PathologyImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'case_id', 'stain_type', 'magnification', 'uploaded_by', 'upload_date']
    list_filter = ['stain_type', 'upload_date', 'uploaded_by']
    search_fields = ['title', 'case_id']
    readonly_fields = ['upload_date']
