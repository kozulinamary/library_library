from django.db import models
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    alias = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    birth_year = models.DateField()

    def __str__(self):
        return f"{self.pk} - {self.first_name} - {self.alias} - {self.last_name}  - {self.birth_year}"


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.pk} - {self.title}  {self.price}. Author id = {self.author}"


