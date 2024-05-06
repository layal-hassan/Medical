from django.utils import timezone
from django.db import models

# Create your models here.

def image_upload(instance,filename):
    imagename , extension = filename.split(".")
    return "homes/%s.%s"%(instance,extension)



class Category(models.Model):
    name= models.CharField(max_length=50)

    def __str__(self):
        return self.name 
class Services(models.Model):
    name = models.CharField(max_length=50)
    descraption = models.TextField(max_length=1000)
    image = models.ImageField(upload_to=image_upload)


    def __str__(self):
        return self.name
    

 
    


class Doctor(models.Model):
    image = models.ImageField(upload_to=image_upload)
    name = models.CharField(max_length=50)
    specialization = models.CharField(max_length=100)
    descraption = models.TextField(max_length=1000)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    instagram = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name  


class Make_Order(models.Model):
    doctor = models.ForeignKey("Doctor", related_name=("doctor_list"), on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=100)
    comment = models.TextField(max_length=1000)
    available = models.DateTimeField(auto_now=True)
    more_descraption =  models.TextField(max_length=4000)
    def __str__(self):
        return self.name   
    





class Price(models.Model):
    service = models.ForeignKey(Services, related_name="prices", on_delete=models.CASCADE)
    area = models.ForeignKey(Category,on_delete=models.CASCADE)# مثل: جسم كامل، ابط، يدين، وجه، فم، إلخ.
    price = models.DecimalField(max_digits=10, decimal_places=2)



class Gallery(models.Model):
    image = models.ImageField(upload_to=image_upload)
    name = models.CharField(max_length=100)    
    def __str__(self):
        return self.name 