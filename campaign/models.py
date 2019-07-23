from django.db import models

# Create your models here.
class UserType(models.Model):
	type = models.CharField(max_length=200)
	created_at = models.DateTimeField('date published')
	updated_at= models.DateTimeField(' date updated')
	
    
    

class User(models.Model):
    type_id = models.ForeignKey(UserType, on_delete=models.CASCADE)
    email_id = models.CharField(max_length=200)
    name= models.CharField(max_length=100)
    phone_no=models.CharField(max_length=100)
    votes = models.IntegerField(default=0)


