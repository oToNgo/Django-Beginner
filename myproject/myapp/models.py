from django.db import models

# Create your models here.
# ส่วนทีเก็บข้อมูลของฐานข้อมูลโดยตรง จะทำการเชื่อมต่อกับฐานข้อมูลโดยตรง
"""
charfield    เก็บข้อมูลอักขระ
lntegerfield เก็บตัวเลข
floatfield  เก็บทศนิยม
datefield เก็บวันเดือนปี
booleanfield เก็บข้อมูล True /False
"""
class Person(models.Model):
        name = models.CharField(max_length=100)
        age = models.IntegerField()
        date = models.DateField(auto_now_add=True)
        
        def __str__(self):
                return (f"ชื่อ {self.name}  อายุ {self.age}") 