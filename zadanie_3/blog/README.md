# Opis
Zgodnie z zadaniem Api serwujace posty na zasadach publicznego GET
(każdy autor może oglądać cudze posty)

Edycja i usuwanie psotu zarazerwowane jest tylko dla autora (Ten sam adres IP co twórcy postu)
Autor jest dodawany do post automatycznie (request IP) i dodawany do bazy jeśli wcześniej nie istniał.

Zinterpretowałem, że autoryzacje do procesów update/del dla Post, wykonujemy na podstawie IP,
dlatego taką też permission class zaimplementowalem.

Wszystkie inne obostrzenia co do pol tekstowych waliduje na pozimie serializera.

# Uruchomienie
1. Pobierz repozytorium i przejdź do `zadanie_3/blog`
2. Stwórz wirualne środowisko `python -m venv venv`
3. Zainstaluj dependencje: `pip install -r requirements.txt`
4. Repozytorium zawiera juz plik bazodanowy db.sqlite3. Nie trzeba robic migracji ani tworzyc superusera
5. Uruchom aplikacje poleceniem `python manage.py runserver`
6. Przejsc w przeglądarce na adres `127.0.0.1:8000`

# Testy
Skonfigurowane na lib django-pytest (wymaga instalacji z requirements.txt)
Przejdz do `cd zadanie_3/blog`
run `python -m pytests tests`


# Dokumentacja API:
### Authors:
`GET blog/api/authors/` - zwraca liste autorow w paginacji

`GET blog/api/authors/<pk>` - zwraca autora po id

### Posts
`GET blog/api/posts/` - zwraca liste dostepnych postow w paginacji

`GET blog/api/posts/<pk>` - zwraca pojedynczy post

`POST blog/api/posts/` - utworzenie postu (i autora jesli nie istniał)
```json
{
    "name": "Testowy Post 2",
    "description": "Lorem impsum dolor",
    "keywords": "foo, bar, zet",
    "url": "https://example-2.com"
}
Obiekt przechowuje IP autora automatycznie. 
Ma tez automatyczne pola created_at/modify_at
```

`PATCH blog/api/posts/<pk>` - edycja postu (tylko dla autora) wraz z logiem zmian.
Edytowac mozna każde pole (partial update) z wyjatkiem autora (read only)

`DELETE blog/api/posts/<pk>` - usuniecie postu (tylko dla autora).
Usuwa też wszystkie relacyjne obiekty histori.

### PostChangeHistory
`GET blog/api/posts/<int:post_id>/history-change/` - zwraca histore zmian dla danego postu w paginacji

### Django Admin
`/admin`
login: admin
pass: admin
