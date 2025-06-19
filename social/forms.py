from django import forms
from .models import Post, Comment, Profile

class PostForm(forms.ModelForm):
    # We explicitly define the 'content' field to customize its widget.
    content = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 3,
        'placeholder': "What's on your mind?",
        'class': 'form-control'
    }), label="")

    # The 'image' field will be created automatically by the ModelForm,
    # so we just need to include it in the 'fields' list below.

    class Meta:
        model = Post
        # This list determines which fields from the Post model show up in the form.
        # We added 'image' to allow users to upload a picture.
        fields = ['content', 'image']


class CommentForm(forms.ModelForm):
    # Customizing the text input for comments to make it a single line.
    text = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Add a comment...',
        'class': 'form-control'
    }), label="")

    class Meta:
        model = Comment
        fields = ['text']


class ProfileForm(forms.ModelForm):
    # For this form, the default widgets for a TextField (bio) and
    # ImageField (profile_picture) are fine, so we don't need to
    # customize them like in the other forms.
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture']
        # You can add custom Bootstrap classes to the fields here if needed
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control'}),
        }