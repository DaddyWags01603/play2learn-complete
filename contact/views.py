import html
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from common.utils.email import send_email
from .forms import ContactForm

# Create your views here.
class ContactUsView(FormView):
    template_name = "contact/contact-us.html"
    form_class = ContactForm
    success_url = reverse_lazy('contact:thanks')

    def form_valid(self, form):
        data = form.cleaned_data
        to = 'scott.wagner.276@gmail.com'
        subject = 'Contact Form Submission'
        content = f'''<p>Hey Site Owner!</p>
            <p>Contact Form received:</p>
            <ol>'''
        for key, value in data.items():
            label = key.replace('_', ' ').title()
            entry = html.escape(str(value), quote=False)
            content += f'<li>{label}: {entry}</li>'
        
        content += '</ol>'

        send_email(to, subject, content)
        return super().form_valid(form)

class ContactThanksView(TemplateView):
    template_name = "contact/thanks.html"