from ast import arg
from pickle import TRUE
from django.forms import fields
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from .models import Category, Comment, Post
from .forms import CommentForm, PostForm,UpdateForm,AddCategoryForm
# Create your views here.
# def home(request):
#     return render(request,'home.html',{})

class HomeView(ListView):
    model= Post
    template_name='home.html'
    ordering=['-post_date']
    # ordering=['-id']

    def get_context_data(self,*args,**kwargs):
        catg_menu=Category.objects.all()
        context=super(HomeView,self).get_context_data(*args,**kwargs)
        context["catg_menu"]=catg_menu
        return context


def CategoryView(request,catgs):
    category_posts=Post.objects.filter(category=catgs.replace('-',' '))
    return render(request,'categories.html', {'catgs':catgs.title().replace('-',' '),'category_posts':category_posts})

def CategoryListView(request):
    catg_menu_list=Category.objects.all()
    return render(request,'category_list.html', {'catg_menu_list':catg_menu_list})


class ArticlesDetailView(DetailView):
    model=Post
    template_name='articles_details.html'

    def get_context_data(self,*args,**kwargs):
        catg_menu=Category.objects.all()
        context=super(ArticlesDetailView,self).get_context_data(*args,**kwargs)
        stuff=get_object_or_404(Post,id=self.kwargs["pk"])
        total_likes=stuff.total_likes()
        liked=False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked=True
        context["catg_menu"]=catg_menu
        context["total_likes"]=total_likes
        context["liked"]=liked
        return context

class AddPostView(CreateView):
    model=Post
    form_class=PostForm
    template_name='add_post.html'
    
    def get_context_data(self,*args,**kwargs):
        catg_menu=Category.objects.all()
        context=super(AddPostView,self).get_context_data(*args,**kwargs)
        context["catg_menu"]=catg_menu
        return context


class UpdatePostView(UpdateView):
    model=Post
    template_name='update_post.html'
    form_class=UpdateForm

class DeletePostView(DeleteView):
    model=Post
    template_name='delete_post.html'
    success_url=reverse_lazy('home')

class AddCategoryView(CreateView):
    model=Category
    form_class=AddCategoryForm
    template_name='add_category.html'
    # fields='__all__'


def LikeView(request,pk):
    post=get_object_or_404(Post,id=request.POST.get('post_id'))
    liked=False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked=False
    else:
        post.likes.add(request.user)
        liked=True
    return HttpResponseRedirect(reverse('article-detail',args=[str(pk)]))

class AddCommentView(CreateView):
    model=Comment
    form_class=CommentForm
    template_name='add_comment.html'
    # fields='__all__'

    def form_valid(self,form):
        form.instance.post_id=self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('article-detail',kwargs={'pk':self.kwargs['pk']})

