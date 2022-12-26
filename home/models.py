from django.db import models


class Sweat(models.Model):
    title = models.CharField(max_length=5000)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'...{self.title} | {self.text[:15]}'
