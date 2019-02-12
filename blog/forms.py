from django.forms import ModelForm
from blog.models import Post
from django import forms
from django.core.exceptions import ValidationError
import datetime

class PostForm(ModelForm):
    
    class Meta:
        model = Post
        exclude = ['rev1_status', 'rev2_status', 'rev3_status']

    def clean(self):
        print(self.cleaned_data)
        start_date = self.cleaned_data['start_date']
        end_date = self.cleaned_data['end_date']
        if start_date < datetime.date.today() or end_date <  datetime.date.today():
            raise forms.ValidationError("End date and Start Date must be after Todays date")
        if start_date > end_date:
            raise forms.ValidationError("End Date must be after the Start date")

        amount_per_day = self.cleaned_data['amount_per_day']
        amount_per_month = self.cleaned_data['amount_per_month']
        if amount_per_day < 0 or amount_per_month < 0:
            raise forms.ValidationError("Amount Cannot be negative")
