from django.contrib import admin
from .models import AnalysisResult

@admin.register(AnalysisResult)
class AnalysisResultAdmin(admin.ModelAdmin):
    list_display = ['image', 'analysis_type', 'status', 'confidence_score', 'created_at']
    list_filter = ['status', 'analysis_type', 'created_at']
    readonly_fields = ['created_at', 'completed_at']
