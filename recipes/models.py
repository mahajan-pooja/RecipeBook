from __future__ import unicode_literals
from datetime import datetime

from django.db import models

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=200)
    recipe_items = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.recipe_name
