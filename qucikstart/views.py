from django.shortcuts import render

# Create your views here.

from rest_framework import generics

from qucikstart.models import Ziom, Ziomka, Categories, Words
from qucikstart.serializers import ZiomSerializer, ZiomkaSerializer, CategoriesSerializer, WordsSerializer


class ZiomList(generics.ListCreateAPIView):
    queryset = Ziom.objects.all()
    serializer_class = ZiomSerializer


class ZiomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ziom.objects.all()
    serializer_class = ZiomSerializer


class ZiomkaList(generics.ListCreateAPIView):
    queryset = Ziomka.objects.all()
    serializer_class = ZiomkaSerializer


class ZiomkaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ziomka.objects.all()
    serializer_class = ZiomkaSerializer


class CategoriesList(generics.ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class CategoriesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class WordsList(generics.ListCreateAPIView):
    queryset = Words.objects.all()
    serializer_class = WordsSerializer


class WordsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Words.objects.all()
    serializer_class = WordsSerializer
