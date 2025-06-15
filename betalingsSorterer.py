from Betalinger_class import *
from tagManager import *

def sorterEtterAarmanneder(betalinger):
    maaneder_dict = {} #dict(zip_longest(maaneder_liste, [], fillvalue=[]))

    for betaling in betalinger:
        betelings_maaned = str(betaling.month) + " " + str(betaling.year)

        if not betelings_maaned in maaneder_dict:
            maaneder_dict[betelings_maaned] = Betalinger()
        maaneder_dict[betelings_maaned].append(betaling)

    maaneder_dict = dict(reversed(list(maaneder_dict.items())))
    return maaneder_dict

def sorterEtterAar(betalinger):
    aar_dict = {} #dict(zip_longest(maaneder_liste, [], fillvalue=[]))

    for betaling in betalinger:
        betelings_maaned = betaling.year

        if not betelings_maaned in aar_dict:
            aar_dict[betelings_maaned] = Betalinger()
        aar_dict[betelings_maaned].append(betaling)

    aar_dict = dict(reversed(list(aar_dict.items())))
    return aar_dict


def sorterBetalingerEtterTags(betalinger):
    sortertEtterTag = dict.fromkeys(alltags.getTags())
    for item in sortertEtterTag.keys():
        sortertEtterTag[item] = Betalinger()

    for betaling in betalinger:
        tags = findTags(betaling)
        for tag in tags:
            sortertEtterTag[tag.name].append(betaling)
    
    return sortertEtterTag
