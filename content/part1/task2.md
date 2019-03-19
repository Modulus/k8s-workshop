Title: Oppgave 2
Date: 2019-03-18 07:56
Tags: introduction,main,k8s,kubernetes,del1-oppgave2,del1
Slug: Del2-Oppgave2
Authors: John Sigvald Skauge
Summary: Oppvage 2
Category: Oppgaver


# Oppgave 2

Her er oppgave 2. I denne delen skal de opprette eige namespace på det delte kubernetes clusteret.

## Oppave 2a - Opprette namespace

```
kubectl create namespace curious-panda
```
Denne kommandoen vil opprette et namespace som **du** skal deploye til. Her kan du bruke eit navnet ditt e.l.

![create namespace]({static}/images/part1/task2/namespace_created.png)

Neste steg er å bytte til ditt nyoppretta namespace

```
kubectl config use-context $(kubectl config current-context) --namespace=curious-panda
```

**NB!!! Husk å bytte ut "curious-panda" med navnet på namespaces du laga i første delen av denne oppgava!**

### Sjekke aktivt namespace

```
kubectl config get-contexts
```

Resultatet av dei forrige kommandoane vil sjå nokonlunde slik ut

![change namespace]({static}/images/part1/task2/change_namespace.png)




## Oppgave 2b - Git clone repo

Før vi kan deploye noko, må de klone eit git repository. Repositoriet ligg her [https://github.com/Modulus/k8s-workshop.git]. Velg dei ei fornuftig rot-mappe ala

/Users/Dittbrukernavn/GitProjects e.l

```
git clone https://github.com/Modulus/k8s-workshop.git
```

Innholdet i k8s-workshop folderen skal sjå slik ut:
![Files]({static}/images/part1/task2/git_repo_output.png)

Inni denne mappa finnes det enda ei mappe med navnet "k8s" cd til denne mappa. Denne skal ha to filer, slik som under:
![Manifests]({static}/images/part1/task2/manifests.png)


Bytt til k8s mappa og gjer deg klar til å deploye ein applikasjon. 



## Oppgave 2c Deploye backend
```
cd k8s
kubectl apply -f backend.yml
```

## Oppgave 2d Liste ut objekt

TODO: FYll inn meir kjøt her veit eg

```
kubectl get deployments
```
![deployments]({static}/images/part1/task2/deployments.png)
```
kubectl get pods
```
![Running pods]({static}/images/part1/task2/running_pods.png)

```
kubectl get services
```
![Serivce]({static}/images/part1/task2/service.png)

Kopier ut "EXTERNAL-IP" verdien. (IP Adressa / DNS Navn). Denne skal brukast på den neste oppgava.  


## Oppgave 2f 

**NB! Husk å bytte ut 192.168.1.241 med verdien fra "EXTERNAL-IP"**

curl 192.168.1.241

![curl]({static}/images/part1/task2/curl1.png)


### Oppgave 2f - Fjerne deployment

```
kubectl delete -f backend.yml
```





Du er no ferdig med oppgave 2, Gå vidare til [Oppgave 3]({filename}/part1/task3.md)