from django.db import models


class Task(models.Model):
    class TaskStatus(models.IntegerChoices):
        ADDED = 10
        DOING = 20
        PENDING = 30
        DONE = 100

    title = models.CharField('Title', max_length=50)
    detail = models.TextField('Detail', max_length=500, null=True, blank=True)
    deadline = models.DateField('Deadline', null=True, blank=True)
    status = models.IntegerField('Status', choices=TaskStatus.choices, default=TaskStatus.ADDED)

    def __str__(self):
        return self.title
