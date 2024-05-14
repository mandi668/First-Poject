from django.db import models

# Create your models here.

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=250, null=True, blank=True)
    category_image = models.ImageField(upload_to='category/', null=True, blank=True)
    
    def __str__(self):
        return f'{self.category_name}'
class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_title = models.CharField(max_length=250, null=True, blank=True)
    item_description = models.TextField(max_length=9000, null=True, blank=True)
    item_image = models.ImageField(upload_to='item/', null=True, blank=True)
    item_category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.item_title}'
    
class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    staff_name = models.CharField(max_length=60, null=True, blank=True)
    staff_mbiemri = models.CharField(max_length=60, null=True, blank=True)
    staff_image = models.ImageField(upload_to='staff/', null=True, blank=True)
    staff_description = models.TextField(max_length=9000, null=True, blank=True)
    staff_email = models.EmailField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.staff_name} {self.staff_mbiemri}'
    
    
class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    contact_name = models.CharField(max_length=50, null=True, blank=True)
    contact_surname = models.CharField(max_length=150, null=True, blank=True)
    contact_email = models.EmailField(null=True, blank=True)
    contact_comment = models.TextField(max_length=700, null=True, blank=True)
    
    def __str__(self):
        return f"{self.contact_name}"

class Reserve(models.Model):
    reserve_id = models.AutoField(primary_key=True)
    reserve_name = models.CharField(max_length=50, null=True, blank=True)
    reserve_surname = models.CharField(max_length=150, null=True, blank=True)
    reserve_email = models.EmailField(null=True, blank=True)
    reserve_number = models.CharField(max_length=20)
    reserve_comment = models.TextField(max_length=700, null=True, blank=True)
    
    def __str__(self):
        return f"{self.reserve_name}"