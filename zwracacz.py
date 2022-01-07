from wynik_liczenia import wynik_liczenia

def aproksymujLicznik(listaOtwarta):
    wiersze_puste = list(filter(lambda item: item.odczyt == None, listaOtwarta))
    wiersze_zbo = list(filter(lambda item: item.uwagi == 'BO', listaOtwarta))
    lista_wynikow = []
    for wiersz_uzytkownika in wiersze_puste:
        nr_uzytkownika = wiersz_uzytkownika.nr_uzytkownika
        podzielniki_uzytkownika = list(filter(lambda item: item.nr_uzytkownika == nr_uzytkownika, listaOtwarta))
        wiersze_niepuste = list(filter(lambda item: item.odczyt != None, podzielniki_uzytkownika))
        mianownik = sum(c.wspolczynnik for c in wiersze_niepuste)
        srednia_wazona = sum(wiersze_niepuste[g].odczyt * wiersze_niepuste[g].wspolczynnik / mianownik for g in range(len(wiersze_niepuste)))
        funkcja = wynik_liczenia(wiersz_uzytkownika.nr_uzytkownika, wiersz_uzytkownika.numer_podz, wiersz_uzytkownika.wspolczynnik, srednia_wazona, wiersz_uzytkownika.uwagi)
        lista_wynikow.append(funkcja)
    return lista_wynikow




