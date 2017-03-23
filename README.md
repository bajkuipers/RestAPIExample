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

Ik heb voor dit project gebruik gemaakt van de libraries 'rest_framework', 'requests' en natuurlijk 'mysqlclient'. Ik heb (in de root) een requirements.txt gegenereerd met 'pip freeze'. Met pip install -r requirements.txt installeer je alle requirements.

Setup in het kort
-----------------

Kortom de volgende stappen zijn nodig om de applicatie te draaien:
- Maak MySQL database 'restapiapp' (met uft-8 encoding)
- Pas username en pasword van de database aan in my.cnf
- pip install -r requirements.txt
- python3 manage.py migrate
- python3 manage.py populatedatabase
- python3 test_script.py om te testen of alles werkt.

