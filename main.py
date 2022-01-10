class UnosNekretnine:
    nazivGrada = ""
    povrsinaNekretnine = 0.0
    sprat = 0
    brojSoba = 1
    cena = 0.0

    def __init__(self, nazivGrada, povrsinaNekretnine, sprat, brojSoba, cena):
        self.nazivGrada = nazivGrada
        self.povrsinaNekretnine = povrsinaNekretnine
        self.sprat = sprat
        self.brojSoba = brojSoba
        self.cena = cena


def procitajKriterijume(kriterijumi):
    kriterijumSpratnosti = 0
    kriterijumBrSoba = 1

    if "," in kriterijumi:
        if kriterijumi.count(',') > 1:
            raise Exception("GRESKA")

        nizKriterijuma = kriterijumi.split(",")
        nizKriterijuma = [i for i in nizKriterijuma if len(i) > 0]

        if len(nizKriterijuma) > 2:
            raise Exception("GRESKA")

        if len(nizKriterijuma) > 2:
            return (kriterijumSpratnosti, kriterijumBrSoba)

        if len(nizKriterijuma) == 1:
            if not int(nizKriterijuma[0]) > 0:
                raise Exception("GRESKA")
            kriterijumBrSoba = int(nizKriterijuma[0])

        if len(nizKriterijuma) == 2:
            if not int(nizKriterijuma[0]) >= 0:
                raise Exception("GRESKA")
            if not int(nizKriterijuma[1]) > 0:
                raise Exception("GRESKA")
            kriterijumSpratnosti = int(nizKriterijuma[0])
            kriterijumBrSoba = int(nizKriterijuma[1])
    else:
        if not int(kriterijumi) >= 0:
            raise Exception("GRESKA")
        kriterijumSpratnosti = int(kriterijumi)

    return (kriterijumSpratnosti, kriterijumBrSoba)


imeUlazneDatoteke = input()
kriterijumi = input()

kriterijumSpratnosti = 0
kriterijumBrSoba = 1

try:
    (kSpratnosti, kBrSoba) = procitajKriterijume(kriterijumi)
    kriterijumSpratnosti = kSpratnosti
    kriterijumBrSoba = kBrSoba
except ValueError:
    print("GRESKA")
except Exception as e:
    print(e)

print(kriterijumSpratnosti)
print(kriterijumBrSoba)