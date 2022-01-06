class wynik_liczenia:
    def __init__(self, numer_podz, wspolczynnik, odczyt):
        self.numer_podz = numer_podz
        self.wspolczynnik = wspolczynnik
        self.odczyt = odczyt

    def __repr__(self):
        return "Test()"
    def __str__(self):
        attrs = vars(self)
        return '{'+(', '.join("%s: %s" % item for item in attrs.items()))+'}'
