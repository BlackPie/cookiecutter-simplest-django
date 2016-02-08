
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import logout, login
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import View, FormView

from project.apps.index.views import LoginRequiredMixin
from project.apps.users.forms import SignupForm


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")


class SigninView(FormView):
    form_class = AuthenticationForm
    template_name = "apps/users/signin.html"
    success_url = reverse_lazy('index')

    def get(self, response, *args, **kwargs):
        if self.request.user.is_authenticated():
            return redirect("index")
        return super(SigninView, self).get(response)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return HttpResponseRedirect(reverse_lazy("index"))

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class SignupView(FormView):
    form_class = SignupForm
    template_name = "apps/users/auth.html"
    success_url = reverse_lazy('index')
