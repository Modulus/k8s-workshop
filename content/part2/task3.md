Title: Oppgave 3
Date: 2019-04-27 13:13
Tags: introduction,main,k8s,kubernetes,del2-oppgave3,del2
Slug: Del2-Oppgave3
Authors: John Sigvald Skauge
Summary: Oppgave liste og introduksjon
Category: Oppgaver

Dere skal nå deploye kibana i deres eget namespace. Dere vil da også få en ingress med en public dns dere kan gå mot for å bruke deres egen kibana instans.

Før de startar skal gnålemåsen der framme deploya ein del graps. Stopp her og vent før de fortsett.


<br />
<br />

## Oppgave 3a

1. cd til k8s/part2
2. Åpne 3_kibana.yml
3. Bytt ut [TODO] med navnet fra namespacet ditt
4. Bytt ut [TODO_DNS] med public dns fra public dns navnet til ingressen

<br />

```
kubectl apply -f 3_kibana.yml
```