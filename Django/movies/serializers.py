from movies.models import Person, Movie
from rest_framework import serializers



class PersonSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Person
        fields = ("id", "name")


class MovieSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "director", "actors", "year")














