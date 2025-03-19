import pandas as pd

BB_df= pd.read_csv("blackboard.csv", encoding="utf-16", sep="\t")
BB_df = BB_df.set_index("Unnamed: 0")
BB_df.index.name = None


#Alternativt
BB_df= pd.read_csv("blackboard.csv", encoding="utf-16", sep="\t", index_col=0)
BB_dfmoodleEx_df = pd.read_csv("moodle_example.csv")
moodleEx_dfdata = {"username": BB_df["Brukernavn"], "firstname": BB_df["Fornavn"], "lastname": BB_df["Etternavn"]}
datatest = pd.DataFrame(data)

#Med for-løkke
#ny_data = []
#for bruker in datatest["username"]:
#    ny_data.append(f"{bruker}@stud.ntnu.no")
#datatest["email"] = ny_data

#Med listekomprehensjon
#datatest["email"] = [f"{bruker}@stud.ntnu.no" for bruker in data["username"]]

#Med apply/map:
#datatest["email"] = datatest["username"].apply(lambda bruker: f"{bruker}@stud.ntnu.no")

#Med pandas sin serialisering av dataseries
datatest["email"] = datatest["username"]+"@stud.ntnu.no"
datatest
datatest.to_csv("moodle_formatert.csv", index=False)#Vi går til ssb.no og henter et datasett om arbeidsledige
arbeidsledige_df = pd.read_csv("arbeidsledige.csv", sep=";", header=1, index_col=0)

arbeidsledige_df.index.name = None

#Legger til kolonne med arbeidsledighet i prosent

#med apply og lambdafunksjon
#arbeidsledige_df["prosent"] = arbeidsledige_df["Arbeidsledige (1 000 personer)"].apply(lambda x: f"{x/1000:.2%}") 

#Med serialisering/vektorisering
arbeidsledige_df["prosent"] = arbeidsledige_df["Arbeidsledige (1 000 personer)"]/1000

arbeidsledige_df["Arbeidsledige (1 000 personer)"].plot()
arbeidsledige_df.describe()
display(arbeidsledige_df) #Vi kan bruke display istedet for print for en "fin" tabell
arbeidsledige_df = arbeidsledige_df.drop("prosent", axis=1)# Vi henter et datasett med åpnede konkurser fra SSB
konkurser_df = pd.read_csv("konkurser.csv", encoding="ISO-8859-1", sep="\t", index_col = 0)
konkurser_df.index.name=None
konkurser_dfkonkurser_df+arbeidsledige_df #Det funket dårlig....#Jeg måtte gjøre følgende for å få norsk output
#import locale
#locale.setlocale(locale.LC_ALL, "nb_NO.utf8")import datetime
from zoneinfo import ZoneInfo
#Henter tid/dato fra datetime.datetime
dato_og_tid = datetime.datetime.now()

#Henter dato fra datetime.date
dato = datetime.date.today()

print("I dag er datoen", dato)
print("Mer nøyaktig er vi nå", dato_og_tid)#Vi kan lage et spesifikt tidspunkt eller dato:

min_dato = datetime.date(1990,4, 23) #År, måned, dag
print("Jeg valgte dato: ", min_dato)

tid = datetime.datetime(2024,12,13,12, tzinfo=ZoneInfo("Europe/Oslo")) #År, måned, dag, time, minutt, sekund, tzinfo=TIDSSONE
print("Mappeinnlevering stenger", tid)

#Vi kan også lage en ENDRING I TID:
#datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
utsettelse = datetime.timedelta(days=1, hours=4)
ny_tid = tid+utsettelse
print("Ny tid for mappeinnlevering:", ny_tid)

#Vi kan sammenligne tider/datoer
print(ny_tid > tid)print("Mappen skal leveres: ", ny_tid.strftime("Senest klokken %H:%M %A den %d."))
print(ny_tid.strftime("%c"))dato_inn = "21/04/1987"
dato_lest = datetime.datetime.strptime(dato_inn, "%d/%m/%Y")
print("Dato som datetime objekt:", dato_lest)#pd.Period('verdi', freq='frekvenskode')
periode = pd.Period('2024-10-21 15:00', freq='Q') #Verdien er en gyldig tekststreng i en periode med frekvens freq=..
langt_frem = periode+26
langt_fremtidserie = pd.period_range('1980Q1', periods=15, freq="Q")
tidserie2 = pd.period_range('1980', '2000', freq='M')
tidserie2display(konkurser_df.head(2))
display(arbeidsledige_df.head(2))arbeidsledige_df = pd.read_csv("arbeidsledige.csv", sep=";", header=1, index_col=0)
arbeidsledige_df.index.name = None

def formater_kvartal(streng_inn):
    streng_ut = streng_inn.replace('K', 'Q')
    return streng_ut

arbeidsledige_df["kvartal"] = arbeidsledige_df.index.map(formater_kvartal)
arbeidsledige_df["kvartal"] = pd.PeriodIndex(arbeidsledige_df["kvartal"], freq='Q')
arbeidsledige_df =arbeidsledige_df.set_index('kvartal')
arbeidsledige_dfkonkurser_df = pd.read_csv("konkurser.csv", encoding="ISO-8859-1", sep="\t", index_col = 0)
konkurser_df.index.name=None

konkurser_df["date"] = konkurser_df.index.map(lambda x: datetime.datetime.strptime(x, "%YM%m")) #med lambdafunksjon
konkurser_df["date"] = konkurser_df["date"].dt.to_period('Q')
konkurser_dfkonkurser_df = konkurser_df.groupby(by="date").sum()
konkurser_df.index.name="kvartal"
df = pd.merge(konkurser_df, arbeidsledige_df, how='outer', on="kvartal")
df = df.dropna(axis=0)
df = df.rename(columns={"Arbeidsledige (1 000 personer)": "Arbeidsledige", "Opna konkursar": "Konkurser"})
#df = df.set_index("kvartal")
dfimport matplotlib.pyplot as plt
df.plot()
plt.xlabel("Tid")
df.plot.scatter("Arbeidsledige", "Konkurser")
df.cov()df.corr()