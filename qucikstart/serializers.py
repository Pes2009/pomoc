from rest_framework import serializers

from qucikstart.models import Ziom, Ziomka, Words, Categories


class ZiomkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ziomka
        fields = ('album', 'title', 'duration', 'id')


class ZiomSerializer(serializers.ModelSerializer):
    zioms = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
     )

    class Meta:
        model = Ziom
        fields = ('album_name', 'zioms', 'artist', 'id')


class WordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Words
        fields = ( 'value', 'id')


class CategoriesSerializer(serializers.ModelSerializer):
    words = serializers.SlugRelatedField(
        many=True,
        queryset= Words.objects.all(),
        slug_field='value'
     )
    class Meta:
        model = Categories
        fields = ('name', 'words','id')
