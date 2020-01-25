from django.db import models


# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=32)
    text = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)


    class Meta:
        ordering = ['-created_at']


    def __str__(self):
        return f"{self.name} - {self.text} - {self.created_at}"


class Author(models.Model):
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=50)
    webpage = models.CharField(max_length=50)

    def __str__(self):
        return f"Author {self.name}"


class Subject(models.Model):
    name = models.CharField(max_length=32)
    bot_name = models.CharField(max_length=32)
    description = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    author = models.ForeignKey(Author, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


