---
tags:
  - lecture/video
css:
  - css/templates.css
---
<!-- slide template="[[tpl-flex]]"  bg="lightgrey"-->

![[version-control-turing-way.svg]]

::: credit
Illustrasjon ved [Scriberia](https://www.scriberia.com/)  (skapt med [The Turing Way](https://the-turing-way.netlify.app/)) .  [CC-BY 4.0 licence](https://creativecommons.org/licenses/by/4.0/). DOI: [10.5281/zenodo.3695300](https://doi.org/10.5281/zenodo.3695300) (Version 3, [direct download link](https://zenodo.org/record/3695300/files/VersionControl.jpg?download=1)).
:::

note:
En stor og altfor vanlig utfordring der man bruker regneark, er det store antallet filer som sendes rundt omkring i epost og på andre måter. Små endringer skaper flere filer, der ingen vet hva som er den riktigste versjonen. Hvis noen gjør en feil, er det vanskelig å finne tilbake til en versjon som virket.

De som driver med programutvikling jobber praktisk talt alltid med et versjonskontrollsystem, som holder rede på hele versjonshistorikken.

---
<!-- slide template="[[tpl-flex]]"  bg="lightgrey"-->

![[Git-logo.svg]]

::: credit
By Jason Long, CC BY 3.0, via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=19329352)

note:
Det mest kjente versjonskontrollsystemet i dag er `git`, som først kom i 2005.
Det er ikke det eneste, men det er så utbredd at for mange vil versjonskontroll være synonymt med git.

---
<!-- slide template="[[tpl-flex]]"  bg="lightgrey"-->

## Github

![[Codicons_–_github-inverted.svg]]

::: credit
By Microsoft Corporation et al., CC BY 4.0,
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=157670002)
:::

note:
En anden vanlig forveksling er mellom git og github.
Mange tenker på git som github.

Git er en åpen standard og programvare med åpen kildekode.
Github er en av mange tjenester som lar deg lagre prosjektene dine, med versjonshistorikk, på en sentral tjener.

Github ble forøvrig kjøpt opp av MicroSoft for en del år siden.

---
<!-- slide template="[[tpl-flex]]"  bg="cox"-->

![[Revision_controlled_project_visualization-2010-24-02.svg]]

::: credit
Traced by User:Stannered, original by en:User:Sami Kerola
Derivative work: Moxfyre (talk)derivative work: Echion2 (talk), CC BY-SA 3.0,
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=9562807)
:::

note:
Git er et *distribuert* versjonskontrollsystem.
Idén er at flere personer kan arbeide parallelt med ulike versjoner, som siden kan flettes sammen.

Så lenge filene er rene tekstfiler, som Markdown eller python-kode, fungerer dette meget godt. Git klarer å se hvilke *linjer* som er endret. Som regel kan endringer flettes sammen, og dersom der er konflikter, trenger man bare å se på de linjene hvor versjonene avviker.

Det er vanlig å holde seg med en hovedgren som alltid skal virke. Når man gjør rettelser og oppgraderinger, gjør man dem først på en sidegren, som flettes inn på hovedgrenen når man vet at alt virker.

*Office*-programmer gir en del av den samme funksjonaliteten i skybaserte 
samskrivingsløsninger og *sporing av endringer*.
Versjonskontroll er løsningen for alt som lagres som ren tekst.
For binærfiler fungerer det derimot dårlig, siden man da ikke kan sammenligne
linje for linje.

---
<!-- slide template="[[tpl-flex]]" bg="lightgrey" -->

![[Traditional_client-server_diagram.svg]]

::: credit
By Avelludo, CC BY-SA 4.0,
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=108657059)
:::

note:
En sentral tjener, som github, gir oss en anden gevinst.
Siste versjon er til en hver tid tilgjengelig på én plass for hele laget.
Det er også mulig å publisere prosjektet åpent på tjeneren.
Svært mange *open source*-prosjekter blir publisert nettopp på github.

Jeg bruker denne


---
<!-- slide template="[[tpl-word]]" -->

https://github.com/

note:
github er et godt valg for prosjekter som skal publiseres åpent.
Det er gratis og det er utbredd, og de er store nok til at tilbudet
neppe forsvinner uten varsel.

Til virksomhetskritiske operasjoner og alt som ligner på konfidentielt
ville jeg derimot ha gått for en betalt løsning og finlest vilkårene.
For min egen del kjører jeg mine egne tjenere med et system som heter
*gitolite* til mine git-prosjekter.  Ved NTNU har vi også en intern
tjener.  Den kjører github sin programvare, men i et lukket system der
NTNU har eierskap.

---
<!-- slide template="[[tpl-word]]" -->

jupytext

note:
Der er ingenting i veien for å sjekke inn *Jupyter Notebooks* i git,
men det er ikke ideelt.  Man ender opp med en masse falske versjoner,
som bare avviker fordi koden er kjørt på nytt, kanskje med et andet
versjonsnummeret fra Jupyter.

Hvis man derimot konverterer *Notebooks* til et tekstformat, som *Markdown*
eller py:percent, fungerer git helt udmerket.  Det kan lønne seg å sette
seg inn i `jupytext`.

---

## Slutt

note:
Der kan være mange grunner for å ta i bruk versjonskontrollsystemer.
Det fungerer bare skikkelig når man innpasser det i den daglige 
arbeidsflyten.

Den største gevinsten har man når programmeringsprosjektene får en
viss størrelsen, og man røkter koden over tid.

Hver og én må vurdere om det gir verdi for en selv.
