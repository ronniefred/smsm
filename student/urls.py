from django.urls import path
from .import views

urlpatterns = [
    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    # path('<int:id>',views.ViewStudent, name='ViewStudent'),
#     path('update/<int:id>',views.update, name='update'),
#     path('delete/<int:id>', views.delete, name='delete'),
 ]

