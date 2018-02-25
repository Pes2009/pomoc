from django.shortcuts import render

# Create your views here.

from rest_framework import generics, status
from rest_framework.response import Response

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

    # def post(self, request, format='json'):
    #     serializer = WordsSerializer(data=request.data)
    #     if serializer.is_valid():
    #         words = serializer.save()
    #         if words:
    #             return Response(serializer.data, status=status.HTTP_201_CREATED)
    #
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WordsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Words.objects.all()
    serializer_class = WordsSerializer
