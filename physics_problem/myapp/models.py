from django.db import models

class Mechanics(models.Model):
    number = models.AutoField(primary_key = True)
    condition = models.TextField()
    answer = models.CharField(max_length=300)
    comment = models.CharField(max_length=300)
    def __str__(self):
        return self.condition

class Thermodynamics(models.Model):
    number = models.AutoField(primary_key = True)
    condition = models.TextField()
    answer = models.CharField(max_length=300)
    comment = models.CharField(max_length=300)

    def __str__(self):
        return self.condition


class Answer(models.Model):
    number_of_problems = models.IntegerField()
    answer = models.IntegerField(default=0)
    type_of_problem = models.CharField(max_length=2, default='m')
    user_id = models.IntegerField(default = 0)

    def __str__(self):
        return self.number_of_problems

class Results(models.Model):
    number_of_problems = models.IntegerField()
    condition = models.TextField()
    answer = models.CharField(max_length=300)
    user_answer = models.CharField(max_length=300)

    def __str__(self):
        return self.number_of_problems

class User(models.Model):
    user_id = models.AutoField(primary_key = True)
    user_name = models.CharField(max_length=20)
    flag = models.IntegerField(default=0)

    def __str__(self):
        return self.number_of_problems
