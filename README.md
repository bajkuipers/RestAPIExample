RestApiExercise
===============

Gebruik
-------

Deze voorbeeldapplicatie bestaat uit twee delen: een management functie om de database te vullen met films uit The Movie Database die op dit moment draaien en een API om die films op te vragen.

Met het standalone script 'test_script.py' kan de API getest worden. Het script doet een aantal API calls en toont de JSon output.

Database
--------

De applicatie werkt met een MySQL database die 'restapiapp' moet heten met een utf-8 encoding. In my.cnf (die bevindt zich in dezelfde directory als deze readme) staan de gebruikersgegevens voor MySQL.

De setup van de database kan met de migration die in het project staat.

De database kan worden gevuld via de management functie 'populatedatabase'. Dus via python(3) manage.py populatedatabase.

Dependencies
------------

Ik heb voor dit project gebruik gemaakt van rest_framework en requests. Ik heb (in de root) een requirements.txt gegenereerd met 'pip freeze'. Met pip install -r requirements.txt installeer je alle requirements.

Setup in het kort
-----------------

Kortom de volgende stappen zijn nodig om de applicatie te draaien:
- Maak MySQL database 'restapiapp'
- Pas username en pasword van de database aan in my.cnf
- pip install -r requirements.txt
- python3 manage.py migrate
- python3 manage.py populatedatabase
- python3 test_script.py om te testen of alles werkt.

Verantwoording keuzes
---------------------

Django rest_framework
---------------------

Ik heb er uiteindelijk voor gekozen toch met het rest_framework van Django te werken omdat ik dat toch de meest elegante manier vind om JSon te serveren binnen Django. Het met de hand serialiseren van modellen voelt teveel als overbodig.


Opbouw database
---------------

De opbouw van de database spreekt denk ik voor zich. Ik heb ervoor gekozen de cast en crew in aparte tabellen op te slaan, omdat de velden ervan in dit voorbeeld dusdanig van elkaar verschillen dat me dat best keuze lijkt. Daarom zijn ze via de API ook als verschillende resources beschikbaar gemaakt.

TMDb API calls
--------------

Ik heb overwogen een Python library voor TMDb te gebruiken (zoals genoemd op https://www.themoviedb.org/documentation/api/wrappers-libraries), maar die blijken geen van allen rekening te houden met de rate limit van TMDb. Overigens is het mij niet gelukt tegen de limieten op te lopen omdat de responsetijd van TMDb niet supersnel is.