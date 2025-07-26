from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

class Tale(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bedtime_stories")
    content = models.TextField()
    category = models.CharField(max_length=100, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    blurb = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.title} | written by {self.author}"

class Suggestion(models.Model):
    tale = models.ForeignKey(Tale, on_delete=models.CASCADE, related_name="suggestions")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="suggestor")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.body} | suggested by {self.author}"