# Automatisk Økonomianalyse
Hensikten med dette prosjektet er å lage et program som kan hente inn og analysere kontoutskriften min og fremstille betalinger jeg har gjort på en oversiktlig måte. Målet er å bruke denne koden til å bli mer bevist på egen pengebruk og ta bedre økonomiske valg. 


## Klasser
### Betaling(self, datestamp, forklaring, utFraKonto, innPaaKonto)
Lagrer en betaling som en instanse av en "betalingsklasse". Denne inneholder all informasjon om klassen, f.eks.:beløp inn og ut, dato, beskrivelse osv. Funksjoner:
- __eq__(self, other): Brukes for å se om to betalinger er like
- __hash__(self): Lager en hash-id av betalingen (elns)
- tonpArray(self, columns): Lager en (1, len(columns))-dimensional np-array av betalingen. 

