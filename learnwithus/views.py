from json import load
from pdb import post_mortem
from pipes import Template
import profile
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.views.generic import (TemplateView,DetailView,ListView,FormView)
from django.views.generic.edit import (CreateView,UpdateView,DeleteView)
from django.contrib.auth.forms import UserCreationForm
from .forms import NewUserForm
from django.contrib.auth import authenticate, login 
from .models import *
from .forms import *


# from .models import Task
#Search method
class PostIndexView(ListView):
    model=Courses
    template_name= 'index.html'
    queryset=Courses.objects.all()
    context_object_name= 'courses'

class SearchView(ListView):
    model=Courses
    template_name= 'index.html'
    context_object_name= 'courses'

    def get_queryset(self):
        query=self.request.GET.get('q')
        return Courses.objects.filter(title__icontains=query).order_by('-title')

   

#Search method end


# detail_page



#course list in courses page
def list_page(request):
    obj=Courses.objects.all()
    return render(request,'courses.html',{'obj':obj})


def detail_page(request, pk):
     obj=get_object_or_404(Courses,pk)
     return render(request,'coursedetail.html',{'obj':obj})

# comment
class CourseDetail(DetailView):
    template_name= 'coursedetail.html'
    model= Courses

    def get_context_data(self , **kwargs):
        data = super().get_context_data(**kwargs)
        connected_comments = Comment.objects.filter(CommentPost=self.get_object())
        number_of_comments = connected_comments.count()
        courseItem = Courses.objects.get(cid=self.kwargs['pk'])

        if self.request.user.is_authenticated:
            new_joinedcourse = JoinedCourses(courseName= courseItem.title, profileid = self.request.user.id, courseid=courseItem.cid)
            new_joinedcourse.save()

        data['comments'] = connected_comments
        data['no_of_comments'] = number_of_comments
        data['comment_form'] = CommentForm()

        data['course'] = courseItem
       

        return data       

    def post(self , request , *args , **kwargs):
        if self.request.method == 'POST':
            print('-------------------------------------------------------------------------------Reached here')
            comment_form = CommentForm(self.request.POST)
            if comment_form.is_valid():
                content = comment_form.cleaned_data['content']
                try:
                    parent = comment_form.cleaned_data['parent']
                except:
                    parent=None

            

            new_comment = Comment(content=content , author = self.request.user , CommentPost=self.get_object() , parent=parent)
            new_comment.save()
            return redirect(self.request.path_info)
# comment end

#############
def index (request):
    print(request.user)
    return render(request,'index.html')

def courses (request):
    return render(request,'courses.html')

class RegisterPage(FormView):
    template_name = 'accounts/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('accounts/login')

    def form_valid(self, form):
        user=form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

def login (request, user):
    return render(request,'accounts/login.html')

def liveqa (request):
    return render(request, 'liveqa.html')

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name= 'accounts/profile.html'

    def get_context_data(self , **kwargs):
        data = super().get_context_data(**kwargs)

        joinedcourses=JoinedCourses.objects.filter(profileid=self.request.user.id)

        data['joinedcourses'] = joinedcourses
        return data



