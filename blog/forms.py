from django import forms
from .models import BlogPost, Comment


class BlogPostForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={"rows": 4}))
    class Meta:
        model = BlogPost
        fields = ('title', 'content', 'category')
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
        }


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'content')

class AuthenticatedCommentForm(forms.ModelForm):
    content = forms.CharField(
        label='', widget=forms.TextInput(attrs={'placeholder': 'Add comment here....'}))    
    
    class Meta:
        model = Comment
        fields = ('content',)

class AnonymousCommentForm(forms.ModelForm):
    name = forms.CharField(
        label='', widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
    email = forms.CharField(
        label='', widget=forms.TextInput(attrs={'placeholder': 'Enter your email'}))
    content = forms.CharField(
        label='', widget=forms.TextInput(attrs={'placeholder': 'Add comment here....'}))    

    class Meta:
        model = Comment
        fields = ('name', 'email', 'content')

