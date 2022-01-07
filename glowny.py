from wynik_liczenia import wynik_liczenia
from zwracacz import aproksymujLicznik
from wczytywacz import wczytaj

parametry_wejsciowe = wczytaj()
wyniki = aproksymujLicznik(parametry_wejsciowe)
for wynik in wyniki:
    print(wynik)

