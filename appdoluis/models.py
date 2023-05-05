from django.db import models

class Task(models.Model):
  title = models.CharField(max_length = 50)
  description = models.TextField()
  due_date = models.DateField()
  done = models.BooleanField()