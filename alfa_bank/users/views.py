from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from users.models import User
from users.serializers import UserRegisterSerializer, ProfileSerializer, LoginSerializer


class RegisterUserView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'internet_banking/profile_list.html'

    def get(self, request):
        queryset = User.objects.all()
        return Response({'profiles': queryset})

    def post(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = True
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)


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
        queryset = User.objects.filter(pk=pk)
        return Response({'profiles': queryset})


class LoginUser(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'internet_banking/login.html'

    def post(self, request):
        profile = User.objects.all()
        serializer = LoginSerializer(profile, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'profile': profile})
        serializer.save()
        return redirect('profile-list')

    def get_success_url(self):
        return reverse_lazy('home')
