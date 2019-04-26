Title: Oppgave 2
Date: 2019-04-23 10:23
Tags: introduction,main,k8s,kubernetes,del2-oppgave2,del2
Slug: Del2-Oppgave2
Authors: John Sigvald Skauge
Summary: Oppgave liste og introduksjon
Category: Oppgaver

De skal deploya ein enkel applikasjon. De vil da også få ein ingress med ein public dns de kan gå mot for å bruke deires egen instans av tenesta.

Før de startar skal han der framme visa detaljar rundt ingress og ingress controller.

<br />
<br />

## Oppave 2a klargjøring av filer

1. Når alt er klart til å fortsette, skal de åpne fila "2_application.yml" i ein editor. 
2.  Bytt ut alle [TODO] med namespacet de har oppretta i forrige oppgave

**For å sjekke namespace**

```
kubectl config get-contexts
```


## Oppgave 2b deploya applikasjon

Deploya applikasjonen ut til ditt eige namespace

```
kubectl apply -f 2_application.yml
```

![apply]({static}/images/part2/task2/1_apply.png)

NB! Det vil ta litt tid før dns blir oppdatert
 

<br />
<br />

## Oppgave 2c Liste ut poddar
```
kubectl get po
```

![pod]({static}/images/part2/task2/2_get_po.png)


<br />
<br />

## Oppgave 2d - Liste ut services

```
kubectl get svc
```

![svc]({static}/images/part2/task2/3_get_svc.png)

<br />
<br />



## Oppgave 2e - Liste ut ingress og akssesera tjenesta fra nettlesaren din

```
kubectl get ingresses
```

![ing]({static}/images/part2/task2/4_get_ingress.png)

**Kopier ut verdien under feltet 'HOST'**

<br />
<br />

1. Lim inn 'HOST' verdien inn i nettlesaren din på pc/mobil. 

![landed]({static}/images/part2/task2/7_landed.png)

<br />
<br />

2. Lek deg litt med applikasjonen


![gen]({static}/images/part2/task2/8_generated.png)

<br />
<br />


**Du er no ferdig og kan fortsette med [Oppgave 3]({filename}/part2/task3.md)**
