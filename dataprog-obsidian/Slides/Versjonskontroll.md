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

---

- Versjonskontroll
    - alt. til samskriving
- jupytext
