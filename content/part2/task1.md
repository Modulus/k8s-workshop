Title: Oppgave 1
Date: 2019-03-29 10:01
Tags: introduction,main,k8s,kubernetes,del2-oppgave1,del2
Slug: Del2-Oppgave1
Authors: John Sigvald Skauge
Summary: Limits og Requests
Category: Oppgaver

Her er oppgave 1. Det som skal gjørast her er å deploye ein pod som kjører nginx. Her skal de også sjå nærare på resource limits.

<br />
<br />

## Oppgave 1a - Namespace
Dere skal operere på eget namespace, siden vi deler et cluster.

```
kubectl create ns curious-panda
kubectl config set-context $(kubectl config current-context) --namespace=curious-panda
```

<br />
<br />

## Oppgave 1b - Resource limits 
Deployement av nginx 

```
cd k8s/part2
kubectl apply -f 1_nginx.yml
kubectl get po
```
![apply]({static}/images/part2/task1/2_get_pod.png)

Hva skjer her?!!! Åpne 1_nginx.yml og se på limits og requests.

<br />
<br />


## Oppgave 1c - Redusere limits

Forrige steg feilet da det ikke finnes noen noder med den kapasiteten vi spurte om. Vi må nå redusere minne og cpu på limits og requests.

**Før resources slik ut:**

![limit1]({static}/images/part2/task1/5_limits_orig.png)


**Etter justering skal det se slik ut:**

![limit1]({static}/images/part2/task1/6_limits_adjust.png)

**Deploye ut endringen**
```
kubectl apply -f 1_nginx.yml
```
![pods_a_limit]({static}/images/part2/task1/7_get_po.png)

<br />
<br />

## Oppgave 1d - Rydde

```
kubectl delete -f 1_nginx.yml
```

Du er nå ferdig med oppgave 1. Hopp videre til Hopp videre til [Oppgave 2]({filename}/part2/task2.md), men ikke start før alle er klare og dere har fått forklart hva et StatefulSet er.