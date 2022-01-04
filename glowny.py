from wynik_liczenia import wynik_liczenia
from zwracacz import aproksymujLicznik

parametry_wejsciowe = [wynik_liczenia(0, 1, 2), wynik_liczenia(3, 4, 5)]
wyniki = aproksymujLicznik(parametry_wejsciowe)
for wynik in wyniki:
    print (wynik.numer_podz, wynik.wspolczynnik, wynik.odczyt)