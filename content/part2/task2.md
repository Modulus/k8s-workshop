Title: Oppgave 2
Date: 2019-04-23 10:23
Tags: introduction,main,k8s,kubernetes,del2-oppgave2,del2
Slug: Del2-Oppgave2
Authors: John Sigvald Skauge
Summary: Oppgave liste og introduksjon
Category: Oppgaver

De skal deploya ein enkel applikasjon. De vil da også få ein ingress med ein public dns de kan gå mot for å bruke deires egen instans av tenesta.

Før de startar skal gnålemåsen der framme deploya ein del graps. Stopp her og vent før de fortsett.


## Oppave 2a

1. Når alt er klart til å fortsette, skal de åpne fila "2_application.yml" i ein editor. 
2.  Bytt ut alle [TODO] med namespacet de har oppretta i forrige oppgave


## Oppgave 2b

Deploya applikasjonen ut til ditt eige namespace

```
kubectl apply -f 2_application.yml
```



