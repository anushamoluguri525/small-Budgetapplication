from django.db import models

class Budget(models.Model):
    code=models.CharField(max_length=50)
    amount=models.FloatField()
    month=models.DateField()
    class Meta:
        db_table="budget"