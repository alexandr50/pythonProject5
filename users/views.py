from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from .forms import CustomUserRegisterForm, ConfirmCodeForm, UserProfileForm
from .models import CustomUser
from .utils import generate_code
from django.contrib.auth import login
from django.contrib import auth


class RegisterUserView(CreateView):
    model = CustomUser
    form_class = CustomUserRegisterForm
    template_name = 'users/register.html'
    extra_context = {
        'title': 'Регистрация'
    }

    def get_success_url(self):
        return reverse('users:confirm_code', kwargs={'phone_number': self.object.phone_number})

    def form_valid(self, form):
        if form.is_valid():
            new_user = form.save(commit=False)
            verify_code = generate_code()
            new_user.verify_code = verify_code
            new_user.save()
        return super().form_valid(form)


def confirm_code(request, phone_number):
    if request.method == 'POST':
        verify_code = request.POST.get('verify_code')
        user = CustomUser.objects.get(phone_number=phone_number)
        if verify_code == user.verify_code:
            user.is_active = True
            user.save()
            auth.login(request, user)
            return redirect(reverse_lazy('users:profile', kwargs={'id': user.pk}))
    context = {'title': 'Подтверждение почты'}

    return render(request, 'users/confirm_code.html', context)



class UserProfileView(UpdateView):
    model = CustomUser
    template_name = 'users/profile.html'
    form_class = UserProfileForm

    def get_success_url(self):
        return reverse_lazy('users:profile', kwargs={'pk': self.kwargs['pk']})