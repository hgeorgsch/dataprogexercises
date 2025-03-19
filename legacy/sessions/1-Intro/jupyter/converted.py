#Dette er en kodecelle i python
#Alt som kommer etter # er en kommentar og blir fullstendig ignorert

print("Hello World!")

print(help(print))
from datetime import datetime

#Her tar vi 1 argument og returnerer ingenting
print("BØ!")

#Her tar print 2 argumenter og returnerer ingenting
print("UÆ!", "ikke skrem meg...", sep="\n", end="\n\n")

#Her tar funksjonen help 1 argument, printfunksjonen, 
#og gir tilbake hjelpetekst som vi printer ut
print(help(print))

#Funksjonen now() fra datetime biblioteket tar ingen argumenter, og returnerer tid og dato
print(datetime.now())
print("""Der bode en underlig gråsprængt en 
på den yderste nøgne ø; –
han gjorde visst intet menneske mén 
hverken på land eller sjø; 
dog stundom gnistred hans øjne stygt, –
helst mod uroligt vejr, –
og da mente folk, at han var forrykt, 
og da var der få, som uden frykt 
kom Terje Vigen nær.""")
#Heltall
antall_epler = 4
Antall_epler = 6


#Flyttall
temperatur = 38.4
celeritas = 3.00e8 #Vitenskaplig notasjon 3.00 x 10^8
h = 6.63e-34 #Plancks konstant: 6.63 x 10^(-34)

print("Per har plukket", antall_epler, "epler")

#Tekststreng
hilsen = "Heisann folkens :)"
hilsen2 = 'hallo, Baloo'
hilsen3 = "What's cookin' good lookin'" #Dersom vi bruker ' i tekststrengen må vi omslutte den med ""
sarkasme = "Deskriptiv statistikk er \"kjempegøy\"" #Vi kan også bruke \" eller \' 
terje_vigen = """
Der bode en underlig gråsprængt en 
på den yderste nøgne ø; –
han gjorde visst intet menneske mén 
hverken på land eller sjø; 
dog stundom gnistred hans øjne stygt, –
helst mod uroligt vejr, –
og da mente folk, at han var forrykt, 
og da var der få, som uden frykt 
kom Terje Vigen nær.
"""

print(terje_vigen)


#Boolean
sant = True
usant = False

print(sant)

#Man kan tilordne funksjoner til en variabel også. Da dropper man ()
printe_funksjon = print
printe_funksjon(hilsen)

#NB - man kan overskrive innebygde funksjoner som print:
#print = antall_epler
#print(Antall_epler)
#Åneeei - vi har ødelagt printefunksjonen vår :(
#Det er fordi jupyter-notebook fortsatt har variabelen print lagret i minnet
#Vi må restarte python som kjører i bakgrunnen (restartknapp ved siden av play,stop)



#Man kan sjekke hvilke datatype en variabel er med funksjonen type()
print("Variabel antall_epler er av typen:", type(antall_epler))

#Man kan lage flere variabler på en linje slik:
sats, ny_sats, type_sats = 0.2, True, "Grunnrenteskatt"
print("Sats, ny?, type sats: ",sats, ny_sats, type_sats)

#Dersom man vil ha heltallet 4 som flyttall bruker man funksjonen float()
#print(help(float))
antall_flyttallsepler = float(4)
print("Antall epler som flyttall:", antall_flyttallsepler)

#Vil man ha flyttallet 3e8 som heltall bruker man int()
#print(help(int))
lysfart_float = 3e8
lysfart_int = int(lysfart_float)
print("Lysests hastighet er:", lysfart_int, "meter per sekund")

#Ofte må man gjøre tekststrenger om til heltall eller flyttall
vekt_str = "90.8"
#vekt_int = int(vekt_str) #Dette funker ikke - vi må gjøre om til flyttall først
vekt_float = float(vekt_str)
vekt_int = int(vekt_float)
print("Min vekt (flyttall):", vekt_float)
print("Min vekt (heltall)", vekt_int) #Merk - tall etter komma fjernes (trunkeres) - bruk round()

#Vi må først avrunde med round(), deretter gjøre om til heltall med int()
vekt_int_avrundet = int(round(vekt_float,0))
print("Vekt avrundet (heltall)", vekt_int_avrundet)# Vi lager 2 variabler, x og y:
x = 8
y = 3

print("x = ", x, "\ny = ", y, "\n\n")

sum_test = x+y
print("x+y = ", sum_test)

sub_test = x-y
print("x-y = ", sub_test)

gange = x*y
print("x*y = ", gange, "\n\n")

dele = x/y
print("x/y = ", dele)
print("brøken vår er av type: ", type(dele))
#Når vi regner med flyttall får vi nesten alltid avrundingsfeil
#Det er derfor som regel lurt å bruke funksjonen round() til å runde av til et fornuftig antall desimaler
dele = round(dele, 4) # Runder av variabel dele til 4 desimaler og lagrer den nye verdien tilbake i dele-variabelen
print("avrundet: x/y = ", dele, "\n\n")

#Modulus gir "rest" etter heltallsdivisjon
modulo = x%y 
print("x%y = ", modulo)

#Heltallsdivisjon gir hvor mange ganger y går opp i x uten rest
#Det blir som vanlig deling, men vi runder alltid ned til nærmeste heltall
dele_heltall = x//y
print("x//y=", dele_heltall)
print("y går opp", dele_heltall, "ganger i x, med rest ", modulo)

potenser = x**y
print("x**y = ", potenser)print( 4/3*7 )
print( 4/(3*7) )#Folketall på Island

e = 2.71828 #Eulers tall (Vi skal se en bedre måte å hente slike konstanter)
K = 4e6 #Maksimal populasjon
r = 0.02 #Relativ vekstrate
start = 2021 #Startår
slutt = 2040 #Sluttår
P0 = 372520 #Startpopulasjon

print("Ved år", start, "var innbyggertallet på Island", P0)
print("Vi antar en årlig vekstrate på", r*100, "%")

tid = slutt-start #Hvor lang tid mellom startår og sluttår
A = (K-P0)/P0   #Koeffisient fra formel

populasjon_2040 = int( K/(1+A*e**(-r*tid))) #Populasjon i år 2040 - som heltall

#Vi vil runde av til nærmeste 1000
#Vi kan gjøre det på 4 måter
populasjon_avrundet = round(populasjon_2040/1000,0)*1000
populasjon_avrundet = int(populasjon_avrundet)

populasjon_avrundet2 = populasjon_2040-populasjon_2040%1000

populasjon_avrundet3 = (populasjon_2040//1000)*1000

populasjon_avrundet4 = round(populasjon_2040,-3)

#print("test", populasjon_avrundet4)

#print(tid, "år senere, i", slutt, "vil populasjon være", populasjon_avrundet4)
print(tid, "år senere, i", slutt, "vil populasjon være omtrent", populasjon_2040//1000, "tusen")# Krisekalkulator: Bruker gir sin alder og programmet oppgir
#hvor lenge det er til han fyller 40

panikk_alder = 50
alder_str = input("Hvor gammel er du?")
alder_int = int(alder_str)
panikk_faktor = panikk_alder-alder_int
print("Om", panikk_faktor, "år, fyller du", panikk_alder)
!jupyter nbconvert --to script plenum.ipynb
