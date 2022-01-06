from wynik_liczenia import wynik_liczenia
from zwracacz import aproksymujLicznik

parametry_wejsciowe = [wynik_liczenia(1, 2, 3), wynik_liczenia(4, 5, 6)]
wyniki = aproksymujLicznik(parametry_wejsciowe)
for wynik in wyniki:
    print (wynik.numer_podz, wynik.wspolczynnik, wynik.odczyt)