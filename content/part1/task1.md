Title: Oppgave 1
Date: 2019-03-15 13:29
Tags: introduction,main,k8s,kubernetes,del1-oppgave1,del1
Slug: Del1-Oppgave1
Authors: John Sigvald Skauge
Summary: Oppgave liste og introduksjon
Category: Oppgaver


Her er oppgave 1. Det som skal gjørast her, er å installera kubectl verktøyet. Dette verktøyet blir brukt til å knytta seg opp mot ulike kubernetes clustre. Oppgavene skal løysast på eit delt kluster som kjører aws.
Oppkobling mot klusteret er da ei del av oppgava.

<br/>
<br/>

## Oppgave 1a -  Installasjon av kubectl og aws-iam-authenticator
1. [Kubectl installasjon](https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-kubectl){:target=_blank}
2. [Aws-iam-authenticator installasjon](https://docs.aws.amazon.com/eks/latest/userguide/install-aws-iam-authenticator.html){:target=_blank}
3. [Aws-cli installasjon](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html){:target=_blank} 


<br/>
<br/>

### 1. Sette opp kubeconfig for workshop cluster

Personen som står der framme og kaklar, vil straks dele ei konfigurasjonsfil med alle. Denne fila må kopierast inn i ~/.kube/ mappen. Kall filen config den fulle stien blir da **~/.kube/config**
Det de no skal gjennomføre er da:

1. Legge inn kubeconfig under ~/.kube/config
2. Legge inn credentials via aws configure --profile profilnavn
3. Editere kubeconfig under ~/.kube/config med profilnavnet fra steg 2

<br/>
<br/>

### 2. Sjekke cluster

```
kubectl cluster-info
```
Outputen skal da se ut som noe slik:
![cluster-info]({static}/images/part1/task1/cluster-info.png)

<br/>
<br/>

### 3. Liste ut nodar


```
kubectl get nodes
```

Output på denne kommandoen ser noenlunde slik ut:

![nodes]({static}/images/part1/task1/nodes.png)

<br/>
<br/>

### 4. Liste ut namespaces

```
kubectl get namespaces
```

![namespaces]({static}/images/part1/task1/namespaces.png)

<br/>
<br/>

### 5. Liste ut pods i kube-system

```
kubectl get pods -n kube-system
```
![namespaces]({static}/images/part1/task1/pods.png)

Hopp videre til [Oppgave 2]({filename}/part1/task2.md)
