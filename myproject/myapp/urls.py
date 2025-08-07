from myapp import views
from django.urls import path
# การเพิ่มการเรียกหน้า ของ  Views
urlpatterns =[
    path('',views.index),
    path('about',views.about),
    path('form',views.form),
    path('edit/<person_id>',views.edit), #การออกแบบในส่วนของการแก้ไข
    path('delete/<person_id>',views.delete),
]