from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Product,Category,AllItems


class RegForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder':'Enter Username',
            'class':'flow-label',
        }
    ))
    email=forms.EmailField(widget=forms.EmailInput(
        attrs={
            'placeholder':'Enter Email Address'
        }
    ))
    
    first_name=forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder':'Enter First Name'
        }
    ))          

    last_name=forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder':'Enter Last Name'
        }
    ))          

    password1=forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder':'Enter Password'
        }
    ))
    
    password2=forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder':'Enter Password Again'
        }
    ))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
  
class Up_category(forms.ModelForm):
    class Meta:
        model=Category
        fields = '__all__'
        
class Up_product(forms.ModelForm):
    class Meta:
        model=Product
        fields = '__all__'
 
class Up_items(forms.ModelForm):
    class Meta:
        model=AllItems
        fields = '__all__'
 
        
# class OrderForm(forms.ModelForm):
#     name= forms.CharField(widget=forms.TextInput(
#         attrs={
#             'placeholder':'Enter name',
#             'class':'flow-label',
#         }
#     ))
    
#     email=forms.EmailField(widget=forms.EmailInput(
#         attrs={
#             'placeholder':'Enter Email'
#         }
#     )) 
    
#     phone=forms.CharField(widget=forms.NumberInput(
#         attrs={
#             'placeholder':'Enter phone number'
#         }
#     )) 
    
#     address=forms.CharField(widget=forms.Textarea(
#         attrs={
#             'placeholder':'Enter address'
#         }
#     )) 
    
#     total=forms.CharField(widget=forms.NumberInput(
#         attrs={
#             'placeholder':'Enter Email'
#         }
#     )) 
    
#     credit_number=forms.CharField(widget=forms.NumberInput(
#         attrs={
#             'placeholder':'enter credit card number'}
#     ))     


