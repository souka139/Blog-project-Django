from pyexpat import model
from django.forms import fields, models
from blog_app.models import Profile
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from .forms import ProfilePageForm, SignUpForm,EditProfileForm,PasswordChangingForm,EditProfilePageForm
from django.views.generic import DetailView, CreateView
# Create your views here.

class PasswordsChangeView(PasswordChangeView):
    # form_class=PasswordChangeForm
    form_class=PasswordChangingForm
    success_url=reverse_lazy('password_success')

class UserRegisterView(generic.CreateView):
    form_class=SignUpForm
    template_name='registration/register.html'
    success_url=reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class=EditProfileForm
    template_name='registration/editProfile.html'
    success_url=reverse_lazy('home')

    def  get_object(self):
        return self.request.user

def password_success(request):
    return render(request,'registration/password_success.html',{})

class ShowProfilPageView(DetailView):
    model=Profile
    template_name='registration/user_profile.html'

    def get_context_data(self,*args,**kwargs):
        # users=Profile.objects.all()
        context=super(ShowProfilPageView,self).get_context_data(*args,**kwargs)

        page_user=get_object_or_404(Profile,id=self.kwargs['pk'])
        context["page_user"]=page_user
        return context

class EditProfilPageView(generic.UpdateView):
    model=Profile
    template_name='registration/edit_profile_page.html'
    form_class=EditProfilePageForm
    success_url=reverse_lazy('home')

class CreateProfilePageView(CreateView):
    model=Profile
    template_name='registration/create_profile.html'
    form_class=ProfilePageForm

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)
