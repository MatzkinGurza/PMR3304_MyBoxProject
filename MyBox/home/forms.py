from django import forms
from .models import Comment, Rating



class CommentForm(forms.ModelForm):
   
    class Meta:
        model = Comment
        fields = ('name', 'body')
        labels = {
            'name': 'Nome',
            'body': 'Comentário',	
            }
        widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'Comment_authorID', 'type': 'hidden'}), 
        'body': forms.Textarea(attrs={'class': 'form-control'}), 
        }

class RatingForm(forms.ModelForm):

    class Meta:
        model = Rating
        fields = ['rating']