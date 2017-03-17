import datetime

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
#from django.shortcuts import render

from restapiapp.models import Movie, Keyword, Crew, Cast
from restapiapp.serializers import MovieSerializer, KeywordSerializer, CrewSerializer, CastSerializer, PaginatedMovieSerializer

#########
# Movie #
#########
  
@api_view(['GET', 'POST'])
# Handles /movies GET and POST
def movie_list(request):
  if request.method == 'GET':
    return get_movie_list(request)
  elif request.method == 'POST':
    return create_movie(request)

# GET /movies: vraag lijst op van alle films
def get_movie_list(request):
  movies = Movie.objects.all()
  serializer = PaginatedMovieSerializer(movies, request, 20)
  return Response(serializer.data)

# POST /movies: maak een nieuwe film
def create_movie(request):
  serializer = MovieSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  else:
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
# Handles /movie/{movie_id} GET, PUT and DELETE and calls methods accordingly
def movie_detail(request, movie_id):
  if request.method == 'GET':
    return get_movie(request, movie_id)
  elif request.method == 'PUT':
    return update_movie(request, movie_id)
  elif request.method == 'DELETE':
    return delete_movie(request, movie_id)

# movies/{movie_id}: vraag details op van een film
def get_movie(request, movie_id):
  movie = Movie.objects.get(id=movie_id)
  serializer = MovieSerializer(movie)
  return Response(serializer.data)

# movies/{movie_id}: Update details van film met id movie_id
def update_movie(request, movie_id):
  movie = Movie.objects.get(id=movie_id)
  serializer = MovieSerializer(movie, data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data)
  else:
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# movies/{movie_id}: Delete movie met id movie_id
def delete_movie(request, movie_id):
  movie = Movie.objects.get(id=movie_id)
  movie.delete()
  return Response(status=status.HTTP_204_NO_CONTENT)

########
# Cast #
########
  
@api_view(['GET', 'PUT', 'DELETE'])
# Handles /cast/{cast_id} GET, PUT and DELETE and calls methods accordingly
def cast_detail(request, id):
  if request.method == 'GET':
    return get_cast(request, id)
  elif request.method == 'PUT':
    return update_cast(request, id)
  elif request.method == 'DELETE':
    return delete_cast(request, id)

# cast/{movie_id}: vraag cast op van een film
def get_cast(request, movie_id):
  cast = Cast.objects.filter(movie=movie_id)
  serializer = CastSerializer(cast, many=True)
  return Response(serializer.data)

# cast/{cast_id}: Update cast met id cast_id
def update_cast(request, cast_id):
  cast = Cast.objects.get(id=cast_id)
  serializer = CastSerializer(cast, data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data)
  else:
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# cast/{cast_id}: Delete cast met id cast_id
def delete_cast(request, cast_id):
  cast = Cast.objects.get(id=cast_id)
  cast.delete()
  return Response(status=status.HTTP_204_NO_CONTENT)
  

########
# Crew #
########
  
@api_view(['GET', 'PUT', 'DELETE'])
# Handles /crew/{crew_id} GET, PUT and DELETE and calls methods accordingly
def crew_detail(request, id):
  if request.method == 'GET':
    return get_crew(request, id)
  elif request.method == 'PUT':
    return update_crew(request, id)
  elif request.method == 'DELETE':
    return delete_crew(request, id)

# crew/{crew_id}: vraag crew op van een film
def get_crew(request, movie_id):
  crew = Crew.objects.filter(movie=movie_id)
  serializer = CrewSerializer(crew, many=True)
  return Response(serializer.data)

# crew/{crew_id}: Update crew entry met id crew_id
def update_crew(request, crew_id):
  crew = Crew.objects.get(id=crew_id)
  serializer = CrewSerializer(crew, data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data)
  else:
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# crew/{crew_id}: Delete crew met id crew_id
def delete_crew(request, crew_id):
  crew = Crew.objects.get(id=crew_id)
  crew.delete()
  return Response(status=status.HTTP_204_NO_CONTENT)

########
# Crew #
########

@api_view(['GET'])
# crew/{crew_id}: vraag crew op van een film
def keyword_detail(request, movie_id):
  keywords = Keyword.objects.filter(movie=movie_id)
  serializer = KeywordSerializer(keywords, many=True)
  return Response(serializer.data)