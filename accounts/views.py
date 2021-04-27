from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from allauth.account.views import PasswordChangeView
from django.views.generic.edit import DeleteView, UpdateView

User = get_user_model()

class CustomPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('account_login') 

class UserDelete(DeleteView):
    model = User
    success_url = reverse_lazy('home')
    template_name = 'account/user_confirm_delete.html'

class UserUpdate(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email',]
    success_url = reverse_lazy('home')
    template_name = 'account/user_update.html'