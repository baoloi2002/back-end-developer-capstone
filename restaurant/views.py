from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Menu
from .serializers import MenuSerializer


def index(request):
    return render(request, "index.html", {})


class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(
    generics.RetrieveUpdateDestroyAPIView, generics.DestroyAPIView
):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
