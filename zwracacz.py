import wynik_liczenia

def aproksymujLicznik(listaOtwarta):
    wiersze_puste = list(filter(lambda item: item.odczyt == None, listaOtwarta))
    wiersze_zbo = list(filter(lambda item: item.uwagi == 'BO', listaOtwarta))
    lista_wynikow = []
    for wiersz_uzytkownika in wiersze_puste:
        nr_uzytkownika = wiersz_uzytkownika.nr_uzytkownika
        podzielniki_uzytkownika = list(filter(lambda item: item.nr_uzytkownika == nr_uzytkownika, listaOtwarta))
        wiersze_niepuste = list(filter(lambda item: item.odczyt != None, listaOtwarta))
        srednia_wazona = sum(c.odczyt for c in wiersze_niepuste)
        lista_wynikow.append(wynik_liczenia(nr_uzytkownika, wiersz_uzytkownika.numer_podz, wiersz_uzytkownika.wspolczynnik, srednia_wazona, wiersz_uzytkownika.uwagi))
    return lista_wynikow




