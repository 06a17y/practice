from django.db import models

# Create your models here.


class Members(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  last_modify_date = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True)
  
  class Meta:
    db_table = "members"