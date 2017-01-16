from django.db import models


class Person (models.Model):
    name = models.CharField(max_length=64)


    def __str__(self):
        return self.name


class Movie (models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    director = models.ForeignKey(Person, related_name = 'movie_director')
    actors = models.ManyToManyField(Person, through='Role', related_name = 'movie_actor')
    year = models.IntegerField()

    def __str__(self):
        return self.title





class Role(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='person_movie')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_movie', null=True)
    role = models.CharField(max_length=64, null = True)


    def __str__(self):
        return self.role



