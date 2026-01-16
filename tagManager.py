from Tag import Tags, Tag
from Betalinger_class import *


class basicTagManager(Tags):
    def __init__(self):
        self.append(Tag("Handlevarer", [
            "Varekjøp",
            "Vipps:coca-colaautomaten",
            "Rema Elgeseter", 
            "Toogoodtog",
            "Vipps:nablakiosken",
            "Narvesen",
            "bunnpris",
            "Vipps:tilbords",
            "Pizza",
            "Burger King",
            "Coca-cola Enterprises",
            "Middag",
            "Espresso House",
            "Databrus",
            "7-eleven",
            "cafe",
            "7eleven",
            "Work-work",
            "Coca Cola",
            "Tgtg",
            "Drivethru",
            "Los Tacos Storo",
            "lunsj"
        ]))

        self.append(Tag("Bunnpris", [
            "bunnpris"
        ]))

        self.append(Tag("Outland", [
            "outland"
        ]))

        self.append(Tag("Faste betalinger", [
            "Patreon: Membership", 
            "Leger Uten Grenser"
            "Buckaroo",
            "Chess.com",
            "Aftenposten",
            "Vipps:changemaker",
            "Tekna",
            "Brilliant.org",
            "Buckaroo",
            "If Skadeforsikring",
            "astral Coach",
            "astralcoach",
            "ingenioerer Uten Gr",
            "trondheim Sykkelkjo",
            "Gjensidige",
            "Acoach"
        ]))

        self.append(Tag("Leie", [
            "Studentsamskipnaden",
            "Sit Efaktura",
            "Sit"
        ]))

        self.append(Tag("Donasjoner", [
            "Leger Uten Grenser",
            "Vipps:roede",
            "Operasjon Dagsverk",
            "frelsesarmeen",
            "Knut Skogstrand Gjerden",
            "gibberish",
            "tv-aksjonen",
            "rosa Sloeyfe",
            "Google:donations"
        ]))

        self.append(Tag("Reise", [
            "entur App",
            "Vipps:atb",
            "Vaernesekspressen",
            "Vipps:norwegian",
            "Sas Airline",
            "Vipps:vkt",
            "Vipps:agder",
            "Vipps:vy",
            "Hotel",
            "Drosje",
            "Gotogate",
            "Gamezone.no",
            "Norwegian Air Shuttle",
            "Entur",
            "ruter",
            "bane Nor",
            "banenor"
        ]))

        self.append(Tag("Lønn", [
            "Lønn",
            "Statens Lånekasse",
            "Lånekassa",
            "Lånekassen"
        ]))

        self.append(Tag("Fritidsinteresser", [
            "Ntnui Sjakk",
            "Steamgames.com",
            "Vipps:nablarevyen",
            "Nabla Revy",
            "minifactor",
            "Tønsberg Schakklubb",
            "Amzn Mktp",
            "Linjeforeningen Nabla",
            "Wizards Of The C",
            "Thorstein Mjøs Pla",
            "79066846879 Christoffer Brevik",
            "Nabla",
            "grimfield Games",
            "My Mini Factory",
            "Tønsberg Schackklubb",
            "Klarna:adlibris",
            "Deck Protector",
            "Titancraft",
            "Gridville",
            "Kino"
        ]))

        self.append(Tag("Gaver", [
            "Aasne",
            "Lars",
            "Giro  Reservert transaksjon",
            "Gratulerer",
            "Hipp Hurra",
            "Gave",
            "Kosibox",
            "Puzzle You"
        ]))

        self.append(Tag("Skole", [
            "Norges Tekn.naturvitensk.unive",
            "skap", 
            "Skap",
            "Fysikk-bøker", 
            "Mattebøker",
            "kompendiesalg"
        ]))

        self.append(Tag("Kontoregulering", [
            "Kontoregulering",
            "Kontoregulering",
            "Overføring Mellom Egne Konti"
        ]))

        self.append(Tag("Alkohol", [
            "Den gode nabo",
            "Vinmonopolet"
        ]))

        self.append(Tag("Annet", [
            "atjioeptjnoaf"
        ]))

def findTags(betaling, tagmanager):
    currentTags = Tags()

    for tag in tagmanager:
        if tag.isin(betaling):
            currentTags.append(tag)
    
    if (len(currentTags) == 0):
        currentTags.append(tagmanager[-1])
    return currentTags


def fjernTager(betalinger, tagerAaFjerne, tagmanager):
    print("Fjerner betalinger med tagene: ", end="")
    for tag in tagerAaFjerne:
        print(tag, end="")
        print(",", end="")
    print("")

    ny_betalingsListe = Betalinger()
    for betaling in betalinger:
        j = True

        for tag in betaling.tags:
            if tag in tagerAaFjerne:
                if tag not in tagmanager:
                    raise "Tag " + tag + " ikke gjenkjent"
                j = False
                break
        
        if j:
            ny_betalingsListe.append(betaling)
    
    return ny_betalingsListe

def kunTag(betalinger, tagerAaBeholde, tagmanager):
    if not tagmanager.containsNameList(tagerAaBeholde):
        raise IndexError("Tag " + str(tagerAaBeholde) + " ikke i tagamanger")
    
    ny_betalingsListe = Betalinger()
    for betaling in betalinger:
        j = False

        for tag in betaling.tags:            
            if tag.name in tagerAaBeholde:
                j = True
                break      
        if j:
            ny_betalingsListe.append(betaling)
    
    return ny_betalingsListe