# Automatisk Økonomianalyse
Hensikten med dette prosjektet er å lage et program som kan hente inn og analysere kontoutskriften min og fremstille betalinger jeg har gjort på en oversiktlig måte. Målet er å bruke denne koden til å bli mer bevist på egen pengebruk og ta bedre økonomiske valg. 


## Klasser
### Betaling(self, datestamp, forklaring, utFraKonto, innPaaKonto)
🤞Lagrer en betaling som en instanse av en "betalingsklasse". Denne inneholder all informasjon om klassen, f.eks.:beløp inn og ut, dato, beskrivelse osv. Funksjoner:
- __eq__(self, other): Brukes for å se om to betalinger er like
- __hash__(self): Lager en hash-id av betalingen (elns)
- tonpArray(self, columns): Lager en (1, len(columns))-dimensional np-array av betalingen. 


### Betalinger(self, items=None)
Inheriter fra list. Lager et liste av betalinger sortert etter betalingstidspunkt. Funksjoner
- sum(self): Returnerer en tuple med totale utgifter og innskudd i lista
- sort(self): Sorterer betalingene etter tisdpunkt

## excelDokument(self, betalinger_)
Et instans av et excel-dokument som skal skrive betalinger-lista ut osm en fin excel-fil. Funksjoner:
- lagSheet(self, betalinger): Lager et 2d np-array av betalinger. Returnerer arrayet
- make(self, filename, folder, **kwargs): Lager selve exceldokumentet, Først lager den sheets av betalingene det har, deretter bruker den excelwriter til å sette den sammen i et exceldokument. All formatering av exceldokmentet gjøres også her


## Plot(self, numberOfPlots)
Plotter betalingene i fine plots matplotlib. Den tar inn et argument for hvor mange plots den skal lage som kan aksesserers senere med en indeks. Funkjsoner:
- checkInInfexOutOuBounds(self, index): Sjekker om indeksen som gis er større enn antal plots
- show(self): Viser plottet
- addTitles(self, indeks, betalinger): Setter aksene til plotet til det betalingen har selv. 
- plotRekke(self, index, betalinger): plotter en tidsgraf med utbeløp langs y-aksen. Kaller automatisk checkInInfexOutOuBounds og addTitles. 
- plottEtterÅr(self, index, betalinger): Skiller betalinger etter år og plotter dem over hverandre i samme graf. 
- plottSector(self, index, betalinger): Skiller betalinger etter tager og plotter dem i sektordiagram opp mot hverandre. 

## Andre ekstra funkjsoner
### Dict-funksjonene 
Noen ganger er det hensiktsmessig å dele en betalingsliste etter egenskaper. Det har vært tre egenskaper jeg har vært interessert i: måned, år og tags (mer om de senere). Alle funksjonene returner en dict med egenskapen som nøkkel.

### lagListeAvBetalinger(foldernavn)
Tar inn en folder og finner alle exceldokumenter der. Den slår sammen alle betalingslistene til en en enkelt betalingsliste, sletter alle like elementer med "set" og sorterer lista. Den returnerer en lista. 


## TODO
- [ ] Endre exceldokument til å lage sheets med dictionaries isteden. 
- [ ] Legg til flere kwargs i exceldokumentet
- [ ] Gjør indeksene til plotteren til en kwarg for lesbarhet