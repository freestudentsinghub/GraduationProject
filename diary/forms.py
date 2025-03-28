from django.forms import ModelForm

from diary.models import Record


class RecordForm(ModelForm):
    class Meta:
        model = Record
        fields = "__all__"
