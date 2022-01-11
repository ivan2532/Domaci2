def procitaj_kriterijume(kriterijumi):
    kriterijum_spratnosti = -1
    kriterijum_br_soba = -1

    if " " in kriterijumi:
        raise Exception("GRESKA")
    if "," in kriterijumi:
        if kriterijumi.count(',') > 1:
            raise Exception("GRESKA")

        niz_kriterijuma = kriterijumi.split(",")
        niz_kriterijuma = [i for i in niz_kriterijuma if len(i) > 0]

        if len(niz_kriterijuma) > 2:
            raise Exception("GRESKA")

        if len(niz_kriterijuma) == 1:
            if not int(niz_kriterijuma[0]) > 0:
                raise Exception("GRESKA")
            if kriterijumi[0] == ",":
                kriterijum_br_soba = int(niz_kriterijuma[0])
            else:
                kriterijum_spratnosti = int(niz_kriterijuma[0])

        if len(niz_kriterijuma) == 2:
            if not int(niz_kriterijuma[0]) >= 0:
                raise Exception("GRESKA")
            if not int(niz_kriterijuma[1]) > 0:
                raise Exception("GRESKA")
            kriterijum_spratnosti = int(niz_kriterijuma[0])
            kriterijum_br_soba = int(niz_kriterijuma[1])
    else:
        if not int(kriterijumi) >= 0:
            raise Exception("GRESKA")
        kriterijum_spratnosti = int(kriterijumi)

    return kriterijum_spratnosti, kriterijum_br_soba


imeUlazneDatoteke = input()
unosKriterijuma = input()

podaciGradova = dict()

try:
    (kSpratnosti, kBrSoba) = procitaj_kriterijume(unosKriterijuma)
    kriterijumSpratnosti = kSpratnosti
    kriterijumBrSoba = kBrSoba

    try:
        ulaznaDatoteka = open(imeUlazneDatoteke, "r")
        for linija in ulaznaDatoteka:
            argumentiLinije = linija.split(",")
            try:
                naziv_grada = str(argumentiLinije[0])
                povrsina_nekretnine = float(argumentiLinije[1])
                sprat = int(argumentiLinije[2])
                broj_soba = int(argumentiLinije[3])
                cena = float(argumentiLinije[4])

                if povrsina_nekretnine <= 0 or sprat < 0 or broj_soba < 1 or cena < 0:
                    continue
            except ValueError:
                continue

            if not (kriterijumSpratnosti == -1 or sprat == kriterijumSpratnosti):
                continue
            if not (kriterijumBrSoba == -1 or broj_soba == kriterijumBrSoba):
                continue

            if not (naziv_grada in podaciGradova):
                podaciGradova[naziv_grada] = list()

            podaciGradova[naziv_grada].append((cena, povrsina_nekretnine))

        izlaznaDatoteka = open("stats.txt", "x")
        sortiraniPodaciGradova = sorted(podaciGradova.items())

        brojacElemenataRecnika = 0  # koristimo ga samo da ne bi bilo line break-a u poslednjoj liniji
        for grad, listaCena in sortiraniPodaciGradova:
            brojacElemenataRecnika += 1
            minCena = listaCena[0][0]
            maxCena = listaCena[0][0]
            prosecnaCena = 0
            for cena, povrsina_nekretnine in listaCena:
                prosecnaCena += cena / povrsina_nekretnine
                if cena > maxCena:
                    maxCena = cena
                if cena < minCena:
                    minCena = cena
            prosecnaCena = prosecnaCena / len(listaCena)
            if brojacElemenataRecnika == len(sortiraniPodaciGradova):
                izlaznaDatoteka.write(grad + " " + "{:.2f}".format(minCena) + " " + "{:.2f}".format(maxCena) + " " + "{:.2f}".format(prosecnaCena))
            else:
                izlaznaDatoteka.write(grad + " " + "{:.2f}".format(minCena) + " " + "{:.2f}".format(maxCena) + " " + "{:.2f}".format(prosecnaCena) + "\n")

    except IOError:
        print("DAT_GRESKA", end="")
    else:
        ulaznaDatoteka.close()
        izlaznaDatoteka.close()
except ValueError:
    print("GRESKA", end="")
except Exception as e:
    print(e, end="")
