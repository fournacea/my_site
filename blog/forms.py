from django import forms 

from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"]
        labels = {
            "user_name": "Enter Username",
            "user_email": "Enter Email",
            "text": "Enter Your Comment",
        }
    
