from django.db import models
from testpage.models import Question, Answer
# Create your models here.

class User(models.Model):
    class Meta():
        db_table = "user"
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    password = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    city = models.CharField(max_length=150)

    def __str__(self):
        return "%s" % self.name

class Author(models.Model):
    class Meta():
        db_table = "author"
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    # id_test = models.ForeignKey('test.id')
    date_create = models.DateField()


class Result(models.Model):
    class Meta():
        db_table = "result"
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    id_answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    date_answer = models.DateField()
