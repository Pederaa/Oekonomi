from Tag import Tags, Tag
from Betalinger_class import *

alltags = Tags()

alltags.append(Tag("Handlevarer", [
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

alltags.append(Tag("Bunnpris", [
    "bunnpris"
]))

alltags.append(Tag("Outland", [
    "outland"
]))

alltags.append(Tag("Faste betalinger", [
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

alltags.append(Tag("Leie", [
    "Studentsamskipnaden",
    "Sit Efaktura",
    "Sit"
]))

alltags.append(Tag("Donasjoner", [
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

alltags.append(Tag("Reise", [
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

alltags.append(Tag("Lønn", [
    "Lønn",
    "Statens Lånekasse",
    "Lånekassa",
    "Lånekassen"
]))

alltags.append(Tag("Fritidsinteresser", [
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

alltags.append(Tag("Gaver", [
    "Aasne",
    "Lars",
    "Giro  Reservert transaksjon",
    "Gratulerer",
    "Hipp Hurra",
    "Gave",
    "Kosibox",
    "Puzzle You"
]))

alltags.append(Tag("Skole", [
    "Norges Tekn.naturvitensk.unive",
    "skap", 
    "Skap",
    "Fysikk-bøker", 
    "Mattebøker",
    "kompendiesalg"
]))

alltags.append(Tag("Kontoregulering", [
    "Kontoregulering",
    "Kontoregulering",
    "Overføring Mellom Egne Konti"
]))

alltags.append(Tag("Alkohol", [
    "Den gode nabo",
    "Vinmonopolet"
]))

alltags.append(Tag("Annet", [
    "atjioeptjnoaf"
]))

def findTags(betaling):
    currentTags = Tags()

    for tag in alltags:
        if tag.isin(betaling):
            currentTags.append(tag)
    
    if (len(currentTags) == 0):
        currentTags.append(alltags[-1])
    return currentTags


def fjernTager(betalinger, tagerAaFjerne):
    ny_betalingsListe = Betalinger()
    for betaling in betalinger:
        j = True

        for tag in betaling.tags:
            if tag in tagerAaFjerne:
                if tag not in alltags:
                    raise "Tag " + tag + " ikke gjenkjent"
                j = False
                break
        
        if j:
            ny_betalingsListe.append(betaling)
    
    return ny_betalingsListe

def kunTag(betalinger, tagerAaBeholde):
    if not alltags.containsNameList(tagerAaBeholde):
        raise IndexError("Tag " + str(tagerAaBeholde) + " ikke gjenkjent")
    
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