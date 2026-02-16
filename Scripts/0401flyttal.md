# Flyttal og NaN


Data er sjelden perfekte.

Der er nesten alltid feil og mangler, av mange ulike årsaker.

Vi må være beredt på å håndtere feil, både i datakildene og i vår egen behandling av data.


($1 \neq 1 + 10^{-16}$)

Den første utfordringen vi skal ha med oss er at datamaskiner er *endelige* tilstandsmaskiner.

For å ta et eksempel kan vi se på tallet en, og tallet 1,000 osv, med en ener i 16de desimal.  I praksis kan det være at forskjellen er uvesentlig, men den er ikke null.

Datamaskiner vil ofte ikke se forskjell.

Det er ikke sikkert at datamaskinen har plass til å huske den 16de desimalen i det hele tatt.

(${\pm} {m}  \cdot 2^{{a}}$)

De vanlige datatypene bruker et bestemt antall *bits*, typisk 64 *bits* i dag.   
Når vi regner med penn og papir er der i prinsippet uendelig mange desimaltall. Der er ingen grense for hvor mange desimaler vi kan skrive hvis vi er tålmodige og skriver smått.

Når vi regner på maskin har vi kanskje bare 2^{64} eller 16 trillioner forskjellige tall som er mulige. Den vil hele tiden runde av til nærmeste lovlige tall.

OK.  16 trillioner er ganske mye, men vi må likevel spørre oss *hvilke* tall vi ønsker å representere.  Trenger vi veldig store tall?  Eller trenger vi mange desimalplasser på små tall?

Det komprisset som moderne maskiner bruker kalles for flyttal, og innebærer at vi skriver tall på en videnskablig form, $m$ ganger 2 opphøyd i $a$.  Så bruker vi f.eks. 53 bits til $m$, som vi kaller for mantissen og 11 til eksponenten $a$, så har vi en bit til overs til fortegnet, pluss eller minus.   

Dette formatet gir oss 15-16 signifikante siffer i titallsystemet, så vi kan skrive alle heltall opp til 15 siffer.   Skal vi representere tall rundt én, har vi 15-16 desimalplasser.  Vi kan skrive tall ned til omtrent $10^{-323}$ og det største tallet vi kan skrive har over 300 siffer, selv om det ikke er mer enn høyst 17 siffer som skiller det fra neste tall.

Dette talformatet kaller vi gjerne for tradisjonelt for `double` men i python heter det gjerne `float64`.   Det siste er lett å forstå; et flyttall med 64 bits.  Begrepet `double` skriver seg fra den tiden 32 *bits* var standard.  Det ble standardisert i 1984.

Vi kaller det for flyttall for de desimalkommaet flyter.  Vi har ikke et fast antall plasser bak kommaet, men et fast antall signifikante, eller meningsfulle, siffer.

(Feilkjelder)


Problemet med flyttalspresisjon kan synes akademisk.  Det skal litt til før vi får alvorlige feil.

Men, vi bruker datamaskiner til meget store datamodeller og kompliserte utregninger, og når vi tar med alle feilkildene i systemet, blir effekten ofte tilfeldige. 

Presisjonen i de tallene som vi kan representere er én feilkilde.

I tillegg har vi trunkeringer i numeriske utregninger.  Mange utregninger, som f.eks. løsning av optimeringsproblemer, består av en *while*-løkke som gir en litt bedre tilnærming for hver iterasjon.  Dersom den kjører uendelig lenge, så kan vi få uendelig bra nøyaktighet, men siden vi ikke har uendelig tid, må vi balansere tid og nøyaktighet.

Neste problem er feilpropagering.  Dvs. at vi må akseptere approksimasjoner i mellomregningene, slik at vi i senere utregninger har upresise inndata.  I lange kjeder av beregninger kan det godt skje at feilene vokser for hvert steg.

Det er de tre store feilfenomenene i selve programmeringen.  I tillegg har vi feil i datainnsamlingen.  Det kan være målefeil og registreringsfeil som gir unøyaktige data. Dersom data er samlet fra et utvalg, uten at man har talt hele populasjonen, får vi estimeringsfeil.  Dette skal vi derimot la ligge, siden datainnsamling er et kapittel for seg.

Det vi derimot er nødt til å se på, er manglende data.  Det er helt vanlig, når vi laster ned data, at der er huller i tabellen.  Det kan stå blankt eller et eller andet symbol som en strek eller N/A.

(NaN)

Flyttallene gir oss et par ekstra verdier for å håndtere manglende data.
Vi har $\pm\infty$ som gjerne brukes for tall som er for store til å representeres.

I tillegg har vi NaN --- *Not a Number* --- som opprinnelig ble brukt til ulovlige operasjoner og til tall som blir for små til å representeres.  Det er ofte viktig å unngå en avrunding til null, fordi videre multiplikasjon med null også gir null uansett hvor stor den andre faktoren er.
Når det skjer er det umulig å si hvor stor den samlede feilen blir.

Vi bruker også NaN til å kode verdier som mangler eller er uleselige i datasettet.

(coerce)

Det skjer ganske ofte, når vi jobber med datasett i pandas, at en søyle som skulle ha vært tall ender opp som strenger.
Ofte skyldes det manglende data.

Hvis datasettet representerer manglende verdier som en strek, vil pandas tolke dette som en streng, selv om de som formatterte datasettet tenkte at det skulle bety NaN.

Dette må vi være oppmerksomme på, men løsningen er relativt enkel.
Vi bruker ofte `to_numeric`-funksjonen for å konvertere strengsøyler til tall.  Denne funksjonen tar et argument `errors` for å fortelle hva den skal gjøre med det som ikke lar seg formattere.

Begrepet som vi er på jakt efter er det engelske ordet *coerce*. Vi ønsker å tvinge pandas til å konvertere til tall, og hvis det ikke er tall, er resultatet nødvendigvis NaN,  *not a number*.

(NaN)

Det kjekke med NaN-verdier er at mange funksjoner kan regne med NaN.
Når pandas skal regne gjennomsnitt, vil den f.eks. se bort fra alle NaN-verdiene og gi en faktisk verdi.  

Mange funksjoner som aksepterer NaN inn, kan også gi NaN ut. Hvis du f.eks. regner gjennomsnitt av mange verdier som alle er NaN, vil resultatet også bli NaN.

(dropp radar)

Det betyr likevel ikke at vi aldri trenger å tenke på at vi har NaN-verdier i datasettet.

For hver funksjon som virker på NaN-data har noen gjort et valg for hvordan NaN skal håndteres.  Det valget er fornuftig i en eller anden kontekst, men ikke alltid fornuftig i vår.
Noen ganger trenger vi å gjøre våre egne valg.

Der er i alle fall tre vanlige måter å håndtere NaN på.
Vi kan droppe rader med NaN-verdier, f.eks. med dropna-metoden i pandas.
Vi kan interpolere, dvs. estimere den manglende verdien basert på to eller flere naboverdier.
Eller vi kan sette inn null eller en like vilkårlig verdi.

Hva som er fornuftig avhenger av problemet.
Jeg håper med denne videoen å ha klargjort et par sentrale begreper slik at de er kjente når dere møter de store utfordringene i praksis.


