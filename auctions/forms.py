from django.forms import ModelForm

from .models import Listing

class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'image', 'description', 'category', 'starting_bid']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
        self.fields["category"].widget.attrs["class"] += " form-select"
        self.fields['description'].widget.attrs['rows'] = 3