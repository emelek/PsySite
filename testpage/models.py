from django.db import models

# Create your models here.

class Test(models.Model):
    class Meta():
        db_table = 'test'
    name = models.CharField(max_length=150)
    author = models.ForeignKey('user.Author', on_delete=models.CASCADE)
    instruction = models.TextField()

class Question(models.Model):
    class Meta():
        db_table = 'question'
    id_test = models.ForeignKey(Test, on_delete=models.CASCADE)
    nmb_in_test = models.IntegerField()
    text = models.TextField()


class Image(models.Model):
    class Meta():
        db_table = 'image'
    id_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    location = models.TextField()

class Answer(models.Model):
    class Meta():
        db_table = 'answer'
    id_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()
    type = models.ForeignKey('type', on_delete=models.CASCADE)

class Type(models.Model):
    class Meta():
        db_table = 'type'
    name = models.CharField(max_length=20)