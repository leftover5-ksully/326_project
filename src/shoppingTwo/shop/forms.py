from django import forms

class AddItemForm(forms.Form):
    new_item = forms.CharField(label='New Item', max_length=100)
    def clean_new_item(self):
        return self.cleaned_data['new_item']