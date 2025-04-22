from django.contrib.auth import authenticate, login, logout
from django.contrib import messages  # Import the messages module
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, RedirectView, CreateView
from user.models import CustomUser
from user.forms import LoginForm, RegisterForm


# Create your views here.


def user_test(request):
    return render(request, '')


class LoginView(FormView):
    success_url = reverse_lazy('course:index')
    template_name = 'user/simple/login.html'
    form_class = LoginForm
    users = CustomUser.objects.all()
    def form_valid(self, form):
        user = authenticate(self.request, email=form.cleaned_data['email'], password=form.cleaned_data['password'])
        if user is not None:
            if user.is_active:
                login(self.request, user)
                messages.success(self.request, "Login successful!")
                return super().form_valid(form)
            else:
                messages.error(self.request, "Please verify your email first.")
        else:
            messages.error(self.request, "Invalid email or password")
        return self.form_invalid(form)


# def register_view(request):
#     if request.method == "POST":
#         next_thing = request.GET.get('next_thing')
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             password = form.cleaned_data.get('password')
#             user.set_password(password)
#             #avtomatik save qiladi verification link borgan payti
#             user.save()
#             user.is_active = True
#             new_user = authenticate(email=user.email, password=password)
#             login(request, new_user)
#             user.save()
#             if next_thing:
#                 return redirect(next_thing)
#             else:
#                 return redirect('users:verify_email')
#     else:
#         form = RegisterForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'user/simple/register.html', context)
class RegisterView(CreateView):
    form_class = RegisterForm  # Use your RegisterForm
    template_name = 'user/simple/register.html'  # Your template path
    success_url = reverse_lazy('course:index')  # Redirect to login after successful registration

    def form_valid(self, form):
        user = form.save()  # Save the user
        # No need to set password, it's in the form, and no need to set is_active
        # user.is_active = True
        # user.save() # No need to save again, form.save() does this.

        # Log the user in immediately after registration.  Important for usability.
        #  authenticate is not required here, because the user object is directly from form.save()
        login(self.request, user)
        messages.success(self.request, "Registration successful!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Registration failed. Please correct the errors below.")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class
        return context


class LogoutView(RedirectView):
    """For logging out user"""
    url = reverse_lazy('course:index')

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, "You have successfully logged out.")
        return super().dispatch(request, *args, **kwargs)