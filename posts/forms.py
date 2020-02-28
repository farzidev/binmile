from django import forms

from .models import Form


class ContactForm(forms.ModelForm):
    class Meta:
        model = Form
        fields = "__all__"
        # exclude = ()

    def __init__(self, *args, **kwargs):
        page = kwargs.pop("page")
        super().__init__(*args, **kwargs)
        if page == "contact":
            self.fields["company"].required = False
            del self.fields["company"]
        elif page == "microsoft":
            self.fields["message"].required = False
            del self.fields["message"]

    def send_mail(self):
        print("SEND MAIL")
