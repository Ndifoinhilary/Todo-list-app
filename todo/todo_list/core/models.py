from django.db import models

# Create your models here.

priority = [
    ('N' , 'None'),
    ('L', 'Low'),
    ('M','Medium'),
    ('H', 'High')
    
]


class Todo(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    use_date = models.DateTimeField()
    priority_list = models.CharField(max_length= 1 , choices=priority)
    updated = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    