from django.contrib import admin
from movies.models import Person, Movie, Role


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Movie)
class MoviesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'director', 'year', 'actors_list')

    def actors_list(self, movies):
        return ','.join([str(t) for t in movies.actors.all()])

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('person', 'movie','role')
