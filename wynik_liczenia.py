class wynik_liczenia:
    def __init__(self, nr_uzytkownika, numer_podz, wspolczynnik, odczyt, uwagi):
        self.nr_uzytkownika = nr_uzytkownika
        self.numer_podz = numer_podz
        self.wspolczynnik = wspolczynnik
        self.odczyt = odczyt
        self.uwagi = uwagi

    def as_string(self):
        attrs = vars(self)
        return '{' + (', '.join("%s: %s" % item for item in attrs.items())) + '}'

    def __repr__(self):
        return self.as_string()
    def __str__(self):
        return self.as_string()
