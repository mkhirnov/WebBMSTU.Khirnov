from django.db import models
from tasks.models import Project, Task

class BugReport(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    task=models.ForeignKey(Task,on_delete=models.SET_NULL,null=True, blank=True)
    STATUS_CHOICES=[('New', 'Новая'),
            ('In Progress', 'В работе'),
            ('Done', 'Завершена')]
    PRIORITY_CHOICES = [(1,1), (2,2), (3,3), (4,4), (5,5)]
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='New')
    priority = models.IntegerField(choices=PRIORITY_CHOICES)

class FeatureReport(models.Model):
    title=models.CharField(max_length=200) #Название запроса на новую функцию. Короткое или нет - непонятно, поэтому 200 символов.
    description=models.TextField()
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    task=models.ForeignKey(Task,on_delete=models.SET_NULL,null=True, blank=True)
    STATUS_CHOICES = [('Рассмотрение', 'Рассмотрение'),
            ('Принято', 'Принято'),
            ('Отклонено', 'Отклонено')]
    PRIORITY_CHOICES = [(1,1), (2,2), (3,3), (4,4), (5,5)]
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='Рассмотрение')
    priority = models.IntegerField(choices=PRIORITY_CHOICES)