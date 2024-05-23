from django.db import models

# Create your models here.
class ckdModel(models.Model):
    no_of_dependents = models.IntegerField()
    loan_amount = models.FloatField()
    loan_term = models.IntegerField()
    cibil_score = models.IntegerField()
