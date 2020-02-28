from django import forms

from .models import Form

from captcha.fields import ReCaptchaField


class ContactForm(forms.ModelForm):
    captcha = ReCaptchaField()

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
