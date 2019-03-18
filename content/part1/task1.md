Title: Del 1 Oppgave 1
Date: 2019-03-15 13:29
Tags: introduction,main,k8s,kubernetes,del1-oppgave1,del1
Slug: Del1-Oppgave1
Authors: John Sigvald Skauge
Summary: Oppgave liste og introduksjon
Category: Oppgaver


Her er oppgave 1. Det som skal gjøres her er å installere kubectl verktøyet. Dette verktøyet blir brukt til å knytte seg opp mot ulike kubernetes cluster. Oppgavene skal løysast på eit delt kluster som kjører aws.
Oppkobling mot klusteret er da ei del av oppgava.

## Oppgave 1a -  Installasjon av kubectl
Installasjons instrukser for kubectl finnes her: [https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-kubectl]({https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-kubectl})

### Sette opp kubeconfig for workshop cluster

Personen som står der framme og kaklar, vil straks dele ei konfigurasjonsfil med alle. Denne fila må kopierast inn i ~/.kube/ mappen. Kall filen config den fulle stien blir da **~/.kube/config**


## Oppgave 1b Sjekke cluster

```
kubectl cluster-info
```
Outputen skal da se ut som noe slik:
![cluster-info]({filename}/images/part1/task1/cluster-info.png)

## Oppgave 1c Liste ut nodar


```
kubectl get nodes
```

Output på denne kommandoen ser noenlunde slik ut:

![nodes]({filename}/images/part1/task1/nodes.png)


## Oppgave 1d - Liste ut namespaces

```
kubectl get namespaces
```

![namespaces]({filename}/images/part1/task1/namespaces.png)

## Oppgave 1e - Liste ut pods i kube-system

```
kubectl get pods -n kube-system
```
![namespaces]({filename}/images/part1/task1/pods.png)

Hopp videre til [Oppgave 2]({filename}/part1/task2.md)
