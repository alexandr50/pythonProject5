from django.contrib import auth
from django.core.cache import cache
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView

from .forms import CustomUserRegisterForm, UserProfileForm
from .models import CustomUser
from .utils import generate_code, generate_invite_code


def login_user(request):
    form = CustomUserRegisterForm()
    if request.method == 'POST':
        form = CustomUserRegisterForm(data=request.POST)
        if form.is_valid():
            cache.set('verify_code', generate_code())
            v = cache.get('verify_code')

            return HttpResponseRedirect(
                reverse('users:confirm_code', kwargs={'phone_number': request.POST.get('phone_number')}))
    context = {
        'title': 'Авторизация',
        'form': form
    }
    return render(request, 'users/login.html', context)


def confirm_code(request, phone_number):
    user_verify_code = cache.get('verify_code')
    if request.method == 'POST':
        verify_code = request.POST.get('verify_code')
        user_verify_code = cache.get('verify_code')
        if verify_code == user_verify_code:
            user = CustomUser.objects.create_user(phone_number=phone_number,
                                                  verify_code=verify_code,
                                                  invaite_code=generate_invite_code())
            user.is_active = True
            user.save()
            auth.login(request, user)
            cache.delete('verify_code')
            return redirect(reverse_lazy('users:profile', kwargs={'pk': user.pk}))
    context = {'title': 'Code confirm'}

    return render(request, 'users/confirm_code.html', context)


class UserProfileView(UpdateView):
    model = CustomUser
    template_name = 'users/profile.html'
    form_class = UserProfileForm

    def get_success_url(self):
        return reverse_lazy('users:profile', kwargs={'pk': self.kwargs['pk']})
