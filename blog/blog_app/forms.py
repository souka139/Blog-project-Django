from django import forms
from django.forms import fields, widgets
from .models import Comment, Post,Category


# catg=[('coding','coding'),('sports','sports'),('nature','nature')]
catg=Category.objects.all().values_list('name','name')

choice_list=[]

for item in catg:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','title_tag','author','category','body','header_img')

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the blog title'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the blog title_tag'}),
            'author':forms.TextInput(attrs={'class':'form-control','value':'','id':'author_input','type':'hidden'}),
            # 'author':forms.Select(attrs={'class':'form-control'}),
            'category':forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter the blog body'}),
            'header_img':forms.FileInput(attrs={'class':'form-control'}),
        }

class UpdateForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','title_tag','body','category')

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the blog title'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the blog title_tag'}),
            'body':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter the blog body'}),
            'category':forms.Select(choices=choice_list, attrs={'class':'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('name','body')

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your name'}),
            'body':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter your comment'}),
        }

class AddCategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=('name',)

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter a category'}),
        }
