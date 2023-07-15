# MEDIUM CLONE

Instalcja
=====

Instalcja środowiska za pomocą poetry

```commandline
poetry install
```

Uruchomienie
==
Aby uruchomić projekt po zainstalowaniu środowiska nalezy wykoanać kroki:

1. ``python manage.py migrate``
2. ``python manage.py createsuperuser`` 
Tutaj podajemy dane takie jak login i hasło dla admina
3. ``python manage.py populate_db``
Jeżeli chcesz wygenerować fake'owe dane do bazy użyj komendy
4. ``python manage.py runserver``
5. [front](localhost:8000)
6. [admin site](localhost:8000/admin)