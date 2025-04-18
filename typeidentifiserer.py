kategorier = {
    "Handlevarer": ["Varekjøp",
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
                    "7-eleven"],

    "Faste betalinger": ["Patreon: Membership", 
                   "Leger Uten Grenser"
                   "Buckaroo",
                   "Chess.com",
                   "Sit Efaktura",
                   "Aftenposten",
                   "Vipps:changemaker",
                   "Tekna",
                   "Brilliant.org",
                   "Buckaroo",
                   "Studentsamskipnaden",
                   "If Skadeforsikring",
                   "astral Coach",
                   "astralcoach"],

    "Donasjoner": ["Leger Uten Grenser",
                   "Vipps:roede",
                   "Operasjon Dagsverk",
                   "frelsesarmeen",
                   "Knut Skogstrand Gjerden",
                   "gibberish",
                   "tv-aksjonen",
                   "rosa Sloeyfe"],

    "Reise": ["entur App",
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
              "Norwegian Air Shuttle"],

    "Lønn": ["Lønn",
             "Statens Lånekasse"],
            
    "Fritidsinteresser": ["Ntnui Sjakk",
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
                          "Klarna:adlibris"],
    
    "Gaver": ["Aasne",
              "Lars",
              "Giro  Reservert transaksjon",
              "Gratulerer",
              "Hipp Hurra",
              "Gave"],
            
    "Skole": ["Norges Tekn.naturvitensk.unive",
              "skap", "Skap",
              "Fysikk-bøker", "Mattebøker"],

    "Ikke relevant": ["Kontoregulering"],

    "Alkohol": ["Den gode nabo",
                "Vinmonopolet"],

    "Annet": ["ofrhpiswufejds,m"]
}


def identifiserKategori(forklaring):
    for kategori in kategorier:
        for nøkkelord in kategorier[kategori]:
            if type(forklaring) != type("d"):
                break
            
            if nøkkelord.lower() in forklaring.lower():
                return kategori
    
    return "Annet"
