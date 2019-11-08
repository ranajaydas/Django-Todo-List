from django.db import models
from django.shortcuts import reverse


class Todo(models.Model):
    title = models.CharField(max_length=63)
    pub_date = models.DateField('date published', auto_now_add=True)

    class Meta:
        verbose_name = 'todo list'
        ordering = ['-pub_date']
        get_latest_by = 'pub_date'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('todo_detail', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('todo_update',
                       kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('todo_delete',
                       kwargs={'pk': self.pk})


class Item(models.Model):
    name = models.CharField(max_length=63)
    completion_date = models.DateField('complete by date', blank=True, null=True)
    completed = models.BooleanField(default=False)
    notes = models.CharField(max_length=255, blank=True)
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('todo_detail', kwargs={'pk': self.todo.pk})

    def get_update_url(self):
        return reverse('item_update',
                       kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('item_delete',
                       kwargs={'pk': self.pk})
