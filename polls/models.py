from django.db import models

# Create your models here.
class Student(models.Model):
	name = models.CharField(max_length=30)
	age = models.IntegerField()
	address = models.TextField()
	image = models.ImageField(upload_to="studentimages",blank=True,null=True)

	def __str__(self):
		return self.name
		
class Book(models.Model):
	student = models.ForeignKey(Student,on_delete=models.CASCADE)
	book_name = models.CharField(max_length=50)
	date = models.DateTimeField()