## models.py
1. Dla pól typu CharField() należy dodać parametr max_length
2. Pole established_year jest instancją IntegerField. Powinniśmy więc użyć null=True (zamiast blank=True), bo pusty string nie będzie skonwertowany do int co zaskutkuje errorem
3. Pole nip: Opcjonalnie: można rozwazyc czy nip nie powinien byc polem obowiązkowym i unikalnym (jesli chcemy go później walidować)
4. short_name:
   - mimo, że pole self.name jest wymagane, to technicznie wciąż, może być empty stringiem, co bedzie powodować błąd w wyniku funkcji short name
   - short_name - powinna być zmieniona na __repr__ (reprezentacja techniczna) lub __str__ (reprezentacja biznesowa), a nie być property modelu. Funkcja ewidentnie uzyta do wyswietlania (reprezentacji obiektu), a nie jako jego właściwość.
5. get_share_capital_in_euro():
    - brak parametryzacji kursu
    - brak uwzględnienia, że shared_capital może być NULLem co zaskutkuje TypeErrorem. Może być tez 0.0 i wtedy wynik nie będzie tym o co nam chodzi.
    - output warto zaokrąglić do 2ch miejsc po przecinku, a wynik otypowac type hint (przydatne w custom funkcjach).
    - Opcjonalnie: zaproponowałbym też dodanie tej funkcji jako property właśnie, dla poręczniejszego użycia i schludności. W tej opcji kurs może być wyliczany z zewnętrzego serwisu.

## forms.py (funkcje clean_nip)
1. Pierwszym największym błędem jest to, że funkcja nie zwraca poprawnej wartości pola (nipu) tylko bool. Funkcja musi zwrócić nip.
Dokumentacja Django mówi wprost, że nawet jeśli wartosć pola sie nie zmieni, nalezy ją zawsze zwrócić.
2. W miejscach gdzie funkcja zwraca False powinna zwrocic ValidationError, jako komunikat o błędzie, do nadawcy zapytania.
3. Ocena dobrych praktyk kodowania dla funkcji:
   - w obecnej formie (opcjonalny nip) przy próbie wyciągnięcia wartości dla nip-u, możemy otrzymać None.
   wyjatek KeyError w niczym tu nie pomoze. W tym miejscu może wystąpić AttributeError (None nie ma attr replace)
   - tak szeroki blok try/expt to antypatern. 
   Blok powinien byc jak najbardziej zwęzły i dotyczyc tylko fragemntu gdzie isniteje ryzyko faktycznego wystopenia wyjątku
   - Zaproponowałbym też zmiane kompozycji samej funkcji. Do zewnętrznego serwisu przeniósłbym logike dotyczącą samego parsowania
   oraz oddzielnie logike biznesową (faktyczna walidacje wag itd). W funkcji clean_nip wywołałbym poprostu te dwa serwisy i zwrócił poprawną wartość.
   Zasada single responsibility jest ciężka do osiągnięcia w frameworku takim jak Django 
   ale nad kompozycją i czystoscią kodu, jak najbardziej można mieć kontrole.

## views.py
1. Należy dodać obowiązkowy model (Enterprice) zgodnie z dokumentacją: When specifying a custom form class, you must still specify the model, even though the form_class may be a ModelForm.
2. Widok powinien sie nazywac EnterpriseUpdateView zgodnie z konwencja Django
3. get_form_kwargs -> tutaj funkcja probuje przekazac do kwargsow property modelu (short_name), ktore nie jest uwzględnione w formie,
z racji tego ze to property a nie pole modelu. Zaskutkuje to bledem przekazania nieznanego klucza do formy. Mozna to rozwiązac nadpisujac __init__ formy
lub dodac do contextu
4. get_context_data funkcja nadpisuje context zamiast tylko rozszerzyc go o usera:
   ```
   context = super().get_context_data(**kwargs)
   context["user"] = self.request.user
   return context
   ```
