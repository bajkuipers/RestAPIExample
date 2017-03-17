import http.client
import json

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
  
  # Vraag cast van film 1 op
  test_api_request("/cast/1")
  # Pas cast entry van Jason Schwartzman aan
  test_api_request("/cast/1", 'PUT', '{"name":"Dakota Johnson","character":"Aangepast karakter","movie":1}')

  # Vraag crew van film 1 op
  test_api_request("/crew/1")
  # Pas crew entry van Jason Schwartzman aan
  test_api_request("/crew/54", 'PUT', '{"name":"John Schwartzman","job":"Aangepaste job","movie":1}')

  # Vraag keywords van film 1 op
  test_api_request("/keywords/1")

def test_api_request(url, method='GET', request_body=''):
  conn = http.client.HTTPConnection("localhost:8000")

  conn.request(method, url, body=request_body, headers={'content-type': 'application/json'} if request_body else {})

  data = conn.getresponse().read()
  result = json.loads(data.decode("utf-8"))

  print("Test API call: " + method + " '" + url + "'")
  print(json.dumps(result, indent=4))

test_api()