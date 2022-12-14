from django import forms

from .models import Search


class SearchForm(forms.ModelForm):

    class Meta:
        model = Search
        fields = ('url',)

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['url'].label = ""
        self.fields['url']
