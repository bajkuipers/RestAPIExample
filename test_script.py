import http.client
import json

'''
TODO:
- timeout van the movie database
- pages (zowel bij inladen als bij uitserveren)
- requests gebruiken
- pip freeze
-
'''

def test_api():
  # Vraag lijst van alle films op
  test_api_request("/movies")
  # Pagina 2 van de lijst
  test_api_request("/movies?page=2")
  # Vraag details van een film op
  test_api_request("/movies/1")
  # Voeg nieuwe film toe
  test_api_request("/movies", 'POST', request_body='{"title":"Nieuwe filmtitel","release_date":"2017-02-09","original_language":"en"}')
  # Pas details van een film aan
  test_api_request("/movies/1", 'PUT', '{"title":"Aangepaste filmtitel","release_date":"2017-4-1","original_language":"nl"}')

def test_api_request(url, method='GET', request_body=''):
  conn = http.client.HTTPConnection("localhost:8000")

  conn.request(method, url, body=request_body, headers={'content-type': 'application/json'} if request_body else {})

  data = conn.getresponse().read()
  result = json.loads(data.decode("utf-8"))

  print("Test API call: " + method + " '" + url + "'")
  print(json.dumps(result, indent=4))

test_api()