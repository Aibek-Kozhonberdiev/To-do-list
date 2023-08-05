from django.db import models

class Task(models.Model):

    status_choices = [
        ('new', 'Новая'), 
        ('in_progress', 'Впроцессе'),  
        ('done', 'Сделано')
    ]

    description = models.TextField(max_length=5000, null=False)
    status = models.CharField(max_length=50, choices=status_choices, default='new')
    date_of_completion = models.DateField(null=True)

    def __str__(self) -> str:
        return f'{self.id}. Cтатус: {self.status}'

    class Meta:
        db_table = 'To-do list'
        verbose_name = 'список'
        verbose_name_plural = 'Список дел'