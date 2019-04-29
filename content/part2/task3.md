Title: Oppgave 3
Date: 2019-03-29 10:01

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

<br />

```
kubectl apply -f 3_kibana.yml
```
![apply]({static}/images/part2/task3/1_apply.png)

### Oppgave 3b - Lage index pattern for filebeat i kibana

Det kan ta ein del tid før dns innslag blir aktive. Dersom dette tar for lang tid kan dette legges inn i /etc/hosts fila di

åpne kibana-namespacenavn.aws5.tv2.no i nettelseren din. Dersom dette går dårlig kan du enten venta eller endra /etc/hosts som nevnt over.

1. Åpne "Management" under hoved menyen

![managment]({static}/images/part2/task3/2_index_pattern_link.png)
<br />
<br />

2. Trykk på "Index Patterns".
3. Skriv "filebeat*"
4. Trykk "Next Step"

![index_pat]({static}/images/part2/task3/2_index_pattern.png)
<br />
<br />

5. Velg "@timestamp" fra dropdown
6. Trykk "Create index pattern"

![index_pat]({static}/images/part2/task3/3_index_pattern.png)

<br />
<br />

### Oppgave 3c - Leke med applikasjonen fra oppgave 2 og se i kibana

Applikasjonen fra oppgave 2 logger ganske mykje, kanskje litt for mykje. Men dette er bra for dette eksempelet. Tryk "Generate" Eit par gangar i appen og sjå på "Discovery" i kibana.

![kibana]({static}/images/part2/task3/4_discovery.png)


<br />
<br />

Da er vi ferdige, ikkje meire å gjøra no. 