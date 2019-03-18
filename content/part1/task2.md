Title: Del1-Oppgave 2
Date: 2019-03-15 13:29
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

Neste steg er å bytte til ditt nyoppretta namespace

```
kubectl config use-context $(kubectl config current-context) --namespace=curious-panda
```

**NB!!! Husk å bytte ut "curious-panda" med navnet på namespaces du laga i første delen av denne oppgava!**


## Oppgave 2b - Deployment

```
cd k8s
kubectl apply -f deployment.yml
```

Videre til [Oppgave 3]({filename}/part1/task3.md)