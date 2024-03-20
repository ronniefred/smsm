from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse 
from .models import registration 
# from .models import Task
from .forms import Student_form
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# from .forms import Task_fo
from django.db.models import Q
# Create your views here.

def home(request):
    blog_search = request.GET.get('search')
    if blog_search:
        posts = registration.objects.filter(Q(FirstName__icontains = blog_search)|Q(LastName__icontains = blog_search)|Q(FirstName__LastName__icontains = blog_search))
        # if posts.exists():
        #     pass
        # else:
        #      msg = 'No post'
    else:
        posts=registration.objects.all().order_by('-FirstName')
    pages = Paginator(posts,2)
    posts=pages.page(1)
    getpage=request.GET.get('page')
        # posts=pages.page(getpage)
    # posts=BlogPost.objects.all() 
    try:
        posts=pages.page(getpage)
    except PageNotAnInteger:
        posts=pages.page(1)  
    except EmptyPage:
        posts = pages.page(pages.num_pages)
    return render(request,'student/home.html',{'posts':posts,'pages':pages})  


def about(request):
    if request.method == 'POST':
        form = Student_form(request.POST)
        if form.is_valid():
        #     new_number = form.cleaned_data['number']
        #     new_FirstName = form.cleaned_data['FirstName']
        #     new_LastName = form.cleaned_data['LastName']
        #     new_Course = form.cleaned_data['Course']
        #     new_Email = form.cleaned_data['Email']
        #     new_Date = form.cleaned_data['Date']
            
        # cleaned_student = Student(
        #     number = new_number,
        #     FirstName = new_FirstName,
        #     LastName = new_LastName,
        #     Course = new_Course,
        #     Email = new_Email,
        #     Date = new_Date,
        # )
        # cleaned_student.save()
            form.save()
            return redirect('home')
        
    
        return render(request,'student/about.html',{'forms':form})
    else:
        form = Student_form()
        return render(request,'student/about.html',{
            'form':Student_form()
        }) 
        
        
# def ViewStudent(request,id):
#     students = registration.objects.get(pk = id)
#     return HttpResponseRedirect(reverse('home'))
    
    
# def update(request,id):
#     if request.method == 'POST':
#         student = registration.objects.get(pk = id)
#         form = Student_form(request.POST, instance=student)
#         if form.is_valid():
#             form.save()
#             return render(request, 'student/update.html' , {
#                 'form':form,
#                 'success': True
#                 })   
#     else:
#         student = registration.objects.get(pk=id)  
#         form = Student_form(instance=student)
#         return render(request,'student/update.html', {'form':form})   
    
# def delete(request,id):
#     if request.method == 'POST':
#         delete_student = registration.objects.get(pk=id)
#         delete_student.delete()
#     return HttpResponseRedirect(reverse('home'))






