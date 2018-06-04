from django import forms
from . import models


class FileForm(forms.ModelForm):
    class Meta:
        model = models.File
        fields = ('user', )


    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
