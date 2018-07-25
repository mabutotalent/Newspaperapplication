from django.views.generic import CreateView
from django.urls import reverse_lazy

from . forms import CustomUserCreationForm

# Create your views here.


class SignUp(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')
