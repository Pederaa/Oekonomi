def sorterEtterAarmanneder(betalings_liste):
    maaneder_dict = {} #dict(zip_longest(maaneder_liste, [], fillvalue=[]))

    for betaling in betalings_liste:
        betelings_maaned = str(betaling.month) + " " + str(betaling.year)

        if not betelings_maaned in maaneder_dict:
            maaneder_dict[betelings_maaned] = []
        maaneder_dict[betelings_maaned].append(betaling)

    maaneder_dict = dict(reversed(list(maaneder_dict.items())))
    return maaneder_dict
