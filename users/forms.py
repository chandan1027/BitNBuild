from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

from .models import Clothes, Accessories, Grooming, Category, Tag, Occasion
from .models import ToBuyItem
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content', 'image']  # Update this line
        widgets = {
            'content': forms.TextInput(attrs={'placeholder': 'Type your message here...', 'class': 'form-control'}),
        }

class ToBuyItemForm(forms.ModelForm):
    class Meta:
        model = ToBuyItem
        fields = ['name']

class ClothesForm(forms.ModelForm):
    class Meta:
        model = Clothes
        fields = ['photo', 'name', 'category', 'tags', 'location', 'occasion']

class AccessoriesForm(forms.ModelForm):
    class Meta:
        model = Accessories
        fields = ['photo', 'name', 'tags', 'location', 'occasion']

class GroomingForm(forms.ModelForm):
    class Meta:
        model = Grooming
        fields = ['photo', 'name', 'tags', 'location', 'occasion']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']

class OccasionForm(forms.ModelForm):
    class Meta:
        model = Occasion
        fields = ['name']

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'profile_picture']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            Profile.objects.create(user=user, profile_picture=self.cleaned_data['profile_picture'])
        return user
    



