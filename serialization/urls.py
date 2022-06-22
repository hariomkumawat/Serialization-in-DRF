
from app import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuinfo/<int:pk>',views.student_details),
    path('stuinfo/',views.student_list),

]
