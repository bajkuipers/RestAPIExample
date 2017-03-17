from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from rest_framework import serializers

from restapiapp.models import Movie, Keyword, Crew, Cast

# Serializer voor keywords <=> JSon
class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = '__all__'

# Serializer voor Crew <=> JSon
class CrewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crew
        fields = '__all__'

# Serializer voor Cast <=> JSon
class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cast
        fields = '__all__'

# Serializer voor Movie <=> JSon
class MovieSerializer(serializers.ModelSerializer):
  keywords = KeywordSerializer(read_only=True, required=False, many=True)
  cast = CastSerializer(read_only=True, required=False, many=True)
  crew = CrewSerializer(read_only=True, required=False, many=True)
  class Meta:
      model = Movie
      #fields = ('id', 'title', 'keywords', 'cast', 'crew')
      fields = '__all__'


# Serializer die wordt gebruikt voor het opleveren van gepagineerde lijsten films
class PaginatedMovieSerializer():
    def __init__(self, movies, request, num):
      # Gebruik paginator van Django
      paginator = Paginator(movies, num)
      page = request.query_params.get('page')

      # Test page get variabele
      try:
          movies = paginator.page(page)
      except PageNotAnInteger:
          movies = paginator.page(1)
      except EmptyPage:
          movies = paginator.page(paginator.num_pages)
      count = paginator.count

      # Bepaald vorige en volgende pagina's
      previous = None if not movies.has_previous() else movies.previous_page_number()
      next = None if not movies.has_next() else movies.next_page_number()
      serializer = MovieSerializer(movies, many=True)

      # Zet JSon resultaat in elkaar
      self.data = {'page':count,
                   'previous_page':previous,
                   'next_page':next,
                   'results':serializer.data
                  }