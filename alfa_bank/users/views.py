from django.contrib.auth import login, authenticate

from rest_framework import status, generics, permissions, serializers
from rest_framework.permissions import AllowAny
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render, get_object_or_404, redirect


from users.models import User
from users.serializers import UserRegisterSerializer, ProfileSerializer, LoginSerializer



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


class LoginUserView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'internet_banking/login.html'
    serializer_class = LoginSerializer
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        serializer = LoginSerializer(None)
        return Response({'serializer': serializer})

    def post(self, request):
        data = request.data
        print(data)

        serializer = LoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            print("НОРМАЛЬНОООООО")
            User.objects.get(username=serializer.data['username'])
            user_obj = authenticate(username=serializer.data['username'], password=data['password'])
            login(request, user_obj)

        return Response({'serializer': serializer})



class RegistrationAPIView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = (AllowAny, )
    serializer_class = UserRegisterSerializer
    template_name = 'internet_banking/register.html'

    def get(self, request):
        serializer = UserRegisterSerializer(None)
        return Response({'serializer': serializer})


    def post(self, request):
        user = request.data

        serializer = self.serializer_class(data=user)
        # serializer.validate(user)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response({'serializer': serializer})