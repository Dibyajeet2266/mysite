from django.forms import ModelForm
from blog.models import Post
from django import forms



class PostForm(ModelForm):

    class Meta:
        model = Post
        fields='__all__'

    # def validate_date(self):
    #     start_date = self.cleaned_data['start_date']
    #     end_date = self.cleaned_data['end_date']
    #     if start_date < today date or end_date < :
    #         raise forms.ValidationError("End date and Start Date must be after todays date")
    #     if start_date > end_date:
    #         raise forms.ValidationError("End Date must be after the Start date")
    #
    # def validate_amount(self):
    #     amount_per_day = self.cleaned_data['amount_per_day']
    #     amount_per_month = self.cleaned_data['amount_per_month']
    #     if amount_per_day < 0 or amount_per_month < 0:
    #         raise forms.ValidationError("Amount Cannot be neagtive")
