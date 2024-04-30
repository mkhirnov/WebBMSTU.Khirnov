from django.contrib import admin
from .models import BugReport, FeatureReport

@admin.register(BugReport)
class BugAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'project', 'task', 'status', 'priority', 'created_at', 'updated_at') #Что отображается в админ панели
    list_filter = ('status', 'project', 'task', 'priority') #Фильтры справа - по статусу, проекту, задаче и приоритету
    search_fields = ('title', 'description') #В поиске ищем по этим колонкам
    list_editable = ('project', 'task','status', 'priority',) #Сразу менять приоритет или статус в админ панели или поменять к какому проекту и задаче относится
    ordering = ('created_at',)
    date_hierarchy = 'created_at'

@admin.register(FeatureReport)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'status', 'priority' ,'created_at', 'updated_at')
    list_filter = ('status', 'project', 'task')
    search_fields = ('title', 'description')
    list_editable = ('project', 'task', 'status', 'priority')
    readonly_fields = ('created_at', 'updated_at')
