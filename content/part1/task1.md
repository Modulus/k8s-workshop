Title: Del 1 Oppgave 1
Date: 2019-03-15 13:29
Tags: introduction,main,k8s,kubernetes,del1-oppgave1,del1
Slug: Del1-Oppgave1
Authors: John Sigvald Skauge
Summary: Oppgave liste og introduksjon
Category: Oppgaver

## Del 1 - Oppgave 1

Her er oppgave 1. Det som skal gjøres her er å installere kubectl verktøyet. Dette verktøyet blir brukt til å knytte seg opp mot ulike kubernetes cluster.

### Installasjon av kubectl
Installasjons instrukser for kubectl finnes her: [https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-kubectl]({https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-kubectl})

### Sette opp kubeconfig for workshop cluster

Personen som står der framme og kaklar, vil straks dele ei konfigurasjonsfil med alle. Denne fila må kopierast inn i ~/.kube/ mappen. Kall filen config den fulle stien blir da **~/.kube/config**


### Sjekke cluster 

```
kubectl cluster-info
```

### Liste ut noder


```
kubectl get nodes
```

Hopp videre til [Oppgave 2]({filename}/part1/task2.md)
