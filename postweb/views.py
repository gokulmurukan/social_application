from django.shortcuts import render,redirect
from api.models import Posts,UserProfile,Comments
from django.contrib.auth.models import User
from postweb.forms import SignUpForm,LogInForm,UserProfileForm,PostForm
from django.views.generic import View,CreateView,FormView,ListView,TemplateView,UpdateView,DetailView
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy

# Create your views here.

class SignUpView(CreateView):
    model=User
    form_class=SignUpForm
    template_name="signup.html"
    success_url=reverse_lazy('signin')

class LogInView(FormView):
    form_class=LogInForm
    template_name="login.html"

    def post(self,request,*args,**kwargs):
        form=LogInForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                return redirect("index")
            else:
                return render(request,"login.html",{"form":form})

class HomeView(CreateView,ListView):
    model=Posts
    form_class=PostForm
    template_name="index.html"
    success_url=reverse_lazy('index')
    context_object_name="posts"

    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)

class ProfileCreateView(CreateView):
    model=UserProfile
    form_class=UserProfileForm
    template_name="profile_create.html"
    success_url=reverse_lazy('index')

    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)

class ProfileView(DetailView):
    model=UserProfile
    template_name="profile.html"
    context_object_name="profile"
    pk_url_kwarg="id"

class ProfileEditView(UpdateView):
    model=UserProfile
    form_class=UserProfileForm
    template_name="profile_edit.html"
    success_url=reverse_lazy('index')
    pk_url_kwarg="id"

class AddCommentsView(View):
    def post(self,request,*args,**kwargs):
        usr=request.user
        qid=kwargs.get("id")
        pst=Posts.objects.get(id=qid)
        cmt=request.POST.get("comments")
        Comments.objects.create(user=usr,comment=cmt,post_name=pst)
        return redirect("index")

class UserProfileDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        UserProfile.objects.get(id=id).delete()
        return redirect('profile_detail')

class PostDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        Posts.objects.get(id=id).delete()
        return redirect('index')

class CommentsDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        Comments.objects.get(id=id).delete()
        return redirect('index')

class LogOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")

class CommentUpvoteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        cmt=Comments.objects.get(id=id)
        cmt.upvote.add(request.user)
        return redirect('index')

class CommentUpvoteRemoveView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        cmt=Comments.objects.get(id=id)
        cmt.upvote.remove(request.user)
        return redirect('index')

class PostUpvoteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        cmt=Posts.objects.get(id=id)
        cmt.like.add(request.user)
        return redirect('index')

class PostUpvoteRemoveView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        cmt=Posts.objects.get(id=id)
        cmt.like.remove(request.user)
        return redirect('index')