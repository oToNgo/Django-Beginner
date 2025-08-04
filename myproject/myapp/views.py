from django.shortcuts import render
from django.http import HttpResponse

# การเขียนฟังก์ชั่ง เพิ่มสำหรับการเรียกใช้งาน
def index(request):
    name = "Channarong"
    age = 38
    return render(request,"index.html",{"name":name,"age":age}) 

def about(request):
    return render(request,"about.html")

def form(request):
    return render(request,"form.html")