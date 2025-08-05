from django.shortcuts import render
from django.http import HttpResponse

# การเขียนฟังก์ชั่ง เพิ่มสำหรับการเรียกใช้งาน
def index(request):
    fname = "Channarong"
    age = 40
    return render(request,"index.html",{"fname":fname,"age":age}) 

def about(request):
    return render(request,"about.html")

def form(request):
    return render(request,"form.html")