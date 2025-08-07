from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import Person
from django.contrib import messages


# การเขียนฟังก์ชั่ง เพิ่มสำหรับการเรียกใช้งาน
def index(request):
    all_person = Person.objects.all() #เป็นการดึงข้อมูลมาทั้งหมด
    # all_person = Person.objects.filter(age=25) #เป็นการดึงข้อมูลแบบมีเงื่อนไข
    return render(request,"index.html",{"all_person":all_person}) 

def about(request):
    return render(request,"about.html")

def form(request):
    if request.method == "POST":
        # รับข้อมูล
        name = request.POST["name"]
        age = request.POST["age"]
        print(name , age)
        #บันทึกข้อมูล 
        person = Person.objects.create( #objects.create คือการสร้าง objects ชึ้นมา  เเละ บันทึก
            name = name,
            age = age
        )
        # แสดงข้อความ
        messages.success(request,"บันทึกข้อมูลเรียบร้อย")
        # เปลี่ยนเส้นทาง
        return redirect("/")
    return render(request,"form.html")

def edit(request,person_id):
    if request.method == "POST":
        person = Person.objects.get(id=person_id)
        person.name = request.POST["name"]
        person.age = request.POST["age"]
        person.save()
        messages.success(request,"อัพเดตข้อมูลเรียบร้อย")
        # เปลี่ยนเส้นทาง
        return redirect("/")
    
    # ดึงข้อมูลประชากรที่ต้องการแก้ไข
    person = Person.objects.get(id=person_id)
    return render(request,"edit.html",{"person": person})

def delete(request,person_id):
    person = Person.objects.get(id=person_id)
    person.delete()
    messages.success(request,"ลบข้อมูลเรียบร้อย")
    return redirect("/")