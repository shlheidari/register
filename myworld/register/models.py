from django.db import models

class Members(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  user_name = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  phone = models.CharField(max_length=255)
  security_question = models.CharField(max_length=255)
  answer = models.CharField(max_length=255)
  ssn = models.CharField(max_length=255)
  password = models.CharField(max_length=255)
