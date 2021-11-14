from django.db import models

# Create your models here.
class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField(default='')
    create_date = models.DateTimeField(default=None)

    def __str__(self):
        return "{}번, {}".format(self.id, self.subject)

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default=None)
    content = models.TextField(default='')
    create_date = models.DateTimeField(default=None)