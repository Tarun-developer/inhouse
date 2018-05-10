

										# Search Models
	



from django.db import models
# Create your models here.

class Furnish(models.Model):
	fully = models.IntegerField(blank=True,null=True)
	partially= models.IntegerField(blank=True,null=True)
	
	def __str__(self):
		return str(self.id)



class Apartment(models.Model):
	apartment = models.IntegerField(blank=True,null=True)
	pg = models.IntegerField(blank=True,null=True)
	room=models.IntegerField(blank=True,null=True)
	
	def __str__(self):
		return str(self.id)



class BHK(models.Model):
	one = models.IntegerField(blank=True,null=True)
	two = models.IntegerField(blank=True,null=True)
	three=models.IntegerField(blank=True,null=True)
	
	def __str__(self):
		return str(self.id)



class Property(models.Model):
	location = models.CharField(max_length=1000)	
	status = models.IntegerField(blank=True,null=True,default=1)
	created_at = models.DateField(blank=True,null=True)
	budget=models.IntegerField(blank=True,null=True)
	apartment=models.ForeignKey(Apartment,on_delete=models.CASCADE,blank=True,null=True)
	furnish=models.ForeignKey(Furnish,on_delete=models.CASCADE,blank=True,null=True)
	bhk=models.ForeignKey(BHK,on_delete=models.CASCADE,blank=True,null=True)
	family_preferrable=models.IntegerField(blank=True,null=True)
		
	def __str__(self):
		return str(self.location)



class OwnerInfo(models.Model):
	name = models.CharField(max_length = 250)
	mobile = models.DateField()
	email = models.DateField()
	propertie=models.ForeignKey(Property,on_delete=models.CASCADE)

	def __str__(self):
		return str(self.name)




class Client(models.Model):
	name = models.CharField(max_length = 100)
	email = models.EmailField()
	mobile = models.CharField(max_length = 100)
	addhar = models.CharField(max_length = 15)
	def __str__(self):
		return str(self.name)

class ClientReivew(models.Model):
	client = models.ForeignKey(Client,on_delete=models.CASCADE)
	owner = models.ForeignKey(OwnerInfo,on_delete=models.CASCADE)
	review = models.IntegerField(null=True,blank=True)
	comment = models.CharField(max_length=200,null=True,blank=True)
	

	def __str__(self):
		return str(self.id)

