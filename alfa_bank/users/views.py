from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.urls import reverse_lazy

from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render, get_object_or_404, redirect

from alfa_bank.settings import DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL
from users.forms import LoginUserForm, RegisterUserForm
from users.models import User
from users.serializers import UserRegisterSerializer, ProfileSerializer
from alfa_bank.celery import app
from users.task import post_email

class ProfileList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'internet_banking/profile_list.html'

    def get(self, request):
        queryset = User.objects.all()
        return Response({'profiles': queryset})


class ProfileDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'internet_banking/profile_detail.html'

    def get(self, request, pk):
        profile = get_object_or_404(User, pk=pk)
        serializer = ProfileSerializer(profile)
        return Response({'serializer': serializer, 'profile': profile})

    def post(self, request, pk):
        profile = get_object_or_404(User, pk=pk)
        serializer = ProfileSerializer(profile, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'profile': profile})
        serializer.save()
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'internet_banking/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


# class RegisterUser(CreateView):
#     form_class = RegisterUserForm
#     template_name = 'internet_banking/register.html'
#
#     def form_valid(self, form):
#         # сохроняем форму в базу данных
#         user = form.save()
#         # login - функция джанго которая авторизовывает пользователя
#         login(self.request, user)
#         return redirect('home')

@app.task()
def contact_view(request):
    if request.method == 'GET':
        form = RegisterUserForm()
    elif request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            RECIPIENTS_EMAIL.append(email)
            print('email === '+email)
            print(type(email))
            try:
                post_email.delay(username, RECIPIENTS_EMAIL)
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
            return redirect('home')
    else:
        return HttpResponse('Неверный запрос. ')
    return render(request, "internet_banking/register.html", {'form': form})

# class LoginUserView(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'internet_banking/login.html'
#     serializer_class = LoginSerializer
#     permission_classes = (permissions.AllowAny,)
#
#     def get(self, request):
#         serializer = LoginSerializer(None)
#         return Response({'serializer': serializer})
#
#     def post(self, request):
#         data = request.data
#         print(data)
#
#         serializer = LoginSerializer(data=data)
#         if serializer.is_valid(raise_exception=True):
#             print("НОРМАЛЬНОООООО")
#             User.objects.get(username=serializer.data['username'])
#             user_obj = authenticate(username=serializer.data['username'], password=data['password'])
#             login(request, user_obj)
#
#         return Response({'serializer': serializer})


# class RegistrationAPIView(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     permission_classes = (AllowAny, )
#     serializer_class = UserRegisterSerializer
#     template_name = 'internet_banking/register.html'
#
#     def get(self, request):
#         serializer = UserRegisterSerializer(None)
#         return Response({'serializer': serializer})
#
#
#     def post(self, request):
#         user = request.data
#
#         serializer = self.serializer_class(data=user)
#         # serializer.validate(user)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#
#         return Response({'serializer': serializer})
