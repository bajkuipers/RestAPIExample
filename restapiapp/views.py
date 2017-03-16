import time

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
#from django.shortcuts import render

from restapiapp.models import Movie, Keyword, Crew, Cast
from restapiapp.serializers import MovieSerializer, KeywordSerializer, CrewSerializer, CastSerializer, PaginatedMovieSerializer

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

  
  

#/movies/1/credits
#
#
#
#/api/v3/
  #/movies
    #/1
      #title: Pietje Puk 2
      #director_id: 2
      #keywords: ['aa[', 'noot']
      #credits: {
        #director_id: 2,
        #cameraman_id: 8
      #}
  #/directors
    #/2
      #name: Hans Worst
      #birth_date: 1-1-2001
#
#Create  POST /movies    { json - data }
#Read    GET /movies/1
#Update  PUT /movies/1   { json - data, alle velden - flexibel zijn in de velden die er zijn. } 
#Delete  DELETE /movies/1


#import http.client
#import json
#
#def populate_database(request):
  #conn = http.client.HTTPSConnection("api.themoviedb.org")

  #payload = "{}"

  #url = "/3/movie/now_playing?api_key=fc2ace46c0d0b40befd3c275bc7b404d&region=NL"
  #url = "/3/movie/341174?append_to_response=keywords%2Ccredits&language=nl-NL&api_key=fc2ace46c0d0b40befd3c275bc7b404d"
  #url = "/3/movie/341174?api_key=fc2ace46c0d0b40befd3c275bc7b404d&language=nl-NL&append_to_response=keywords,credits"
  #conn.request("GET", url, payload)

  #data = conn.getresponse().read()
  #results = json.loads(data.decode("utf-8"))['results']
  #print(results)
  #for result in results:
    #print(result)
    #
    #serializer = MovieSerializer(data=result)
    #if serializer.is_valid():
      #new_movie = serializer.save()
