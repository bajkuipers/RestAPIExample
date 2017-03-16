from django.core.management.base import BaseCommand

import requests
from restapiapp.serializers import MovieSerializer, KeywordSerializer, CrewSerializer, CastSerializer

class Command(BaseCommand):
    help = 'Populates the example movie database'

    def handle(self, *args, **options):
      self.populate_database();

    def populate_database(self):
      # TMDb API call om alle films die nu draaien op te halen
      response_json = self.do_tmdb_call('/movie/now_playing', {'region': 'NL'})

      # Uitlezen van het aantal pagina's en de resultaten van pagina 1
      total_pages = response_json['total_pages']
      results = response_json['results']

      print("Total number of movies: " + str(response_json['total_results']))
      print("Total number of pages: " + str(response_json['total_pages']))

      # Loop over alle pagina's uit de resultaatset
      for page in range(total_pages):
        print("Processing page " + str(page + 1))

        # Loop over alle films en haal de details (crew, cast en keywords) op.
        for result in results:
          # Serializeer het JSon resultaat
          serializer = MovieSerializer(data=result)

          # Controleer of alle verplichte velden aanwezig zijn
          if serializer.is_valid():
            # Sla de film op in de database
            new_movie = serializer.save()
            # Haal de details van de film op
            self.populate_related_tables(new_movie, result['id'])

        # Als er een volgende pagina is, haal daarvan dan de resultaten op
        if page + 1 < total_pages:
          response_json = self.do_tmdb_call('/movie/now_playing', {'region': 'NL', 'page': page + 1})
          results = response_json['results']

    def populate_related_tables(self, related_movie, original_movie_id):
      #url = "append_to_response=keywords,credits&language=nl-NL&api_key=fc2ace46c0d0b40befd3c275bc7b404d".format(original_movie_id);
      # Haal details op van 'related_movie' op basis van zijn originele id
      response_json = self.do_tmdb_call("/movie/{}".format(original_movie_id), {'append_to_response': 'keywords,credits'})


      #print('response_json')
      #print(response_json)
      keywords = response_json['keywords']['keywords']
      #print('keywords')
      #print(keywords)
      for result in keywords:
        #result['last_update'] = time.strftime("%Y-%m-%d")
        result['movie'] = related_movie.id
        #print('keywords_result')
        #print(result)
        serializer = KeywordSerializer(data=result)
        #print('keyword_serializer.is_valid()')
        #print(serializer.is_valid())
        if serializer.is_valid():
          new_keyword = serializer.save()

      crew = response_json['credits']['crew']
      for result in crew:
        #result['last_update'] = time.strftime("%Y-%m-%d")
        result['movie'] = related_movie.id
        serializer = CrewSerializer(data=result)
        if serializer.is_valid():
          new_crew = serializer.save()

      cast = response_json['credits']['cast']
      for result in cast:
        #result['last_update'] = time.strftime("%Y-%m-%d")
        result['movie'] = related_movie.id
        serializer = CastSerializer(data=result)
        if serializer.is_valid():
          new_cast = serializer.save()

    def do_tmdb_call(self, url, params):
      # Voeg default parameters toe
      if not params: params = {}
      params['api_key'] = 'fc2ace46c0d0b40befd3c275bc7b404d'
      params['language'] = 'NL-nl'

      # Maak de API call
      response = requests.get('https://api.themoviedb.org/3' + url, params=params)

      # Check de HTTP status.
      if response.status_code == 200:
        response_json = response.json()
        return response_json
      # Als de HTTP status 429 is betekent dat dat de rate limit bereikt is en wacht je het aantal seconden dat in de header 'Retry After' wordt teruggegeven
      elif response.status_code == 429:
        if response.headers['Retry-After']: 
          time.sleep(response.headers['Retry-After'])
          return do_tmdb_call(self, url)
      else: 
        # Als er een andere status terugkomt raise de bijbehorende foutmelding
        response.raise_for_status()
      