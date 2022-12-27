from django.db import models
from tinymce import models as tiny_models


class Sweat(models.Model):
    title = models.CharField(max_length=5000)
    text = tiny_models.HTMLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'...{self.title}  |  {self.text[:15]}'


class About(models.Model):
    text = tiny_models.HTMLField()
    """
     the latest object of this model will be showed in the template,
     so every time creating a new one will be the last update.
    """
    last_update = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'...{self.last_update}  |  {self.text[:15]}'
    