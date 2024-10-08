from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Comment, Tag, Post

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3})
        }



class TagWidget(forms.TextInput):
    def render(self, name, value, attrs=None, renderer=None):
        # Custom rendering logic for tag input
        if value is None:
            value = ''
        return super().render(name, value, attrs)
    

class PostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=TagWidget(),  # Use your custom TagWidget
        required=False
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

