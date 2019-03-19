Title: Del 1 Oppgave 3
Date: 2019-03-15 13:29
Tags: introduction,main,k8s,kubernetes,del1-oppgave3,del1
Slug: Del1-Oppgave3
Authors: John Sigvald Skauge
Summary: Oppgave liste og introduksjon
Category: Oppgaver


Her er oppgave 3. Her skal vi sjå meir på port-forwarding og skalering av kjørandes applikasjonar.


## Oppgave 3a
No skal du deploye ein oppgradert versjon av applikasjonen fra forrige oppgave. Denne versjonen returnerer json-data og har ein frontend som pollar data ca 1 gang per sekund.

```
kubectl apply -f full.yml
```


## Oppgave 3b
Manifestet fra forrige oppgave deployar kun 1 replica av både frontend og backend tjenesten. Desse skal vi no skalere opp til å kjøre 3 instansar av klar tjeneste.


Først lister vi ut deployment info for det vi nettopp har deploya.
```
kubectl get deployments
```
![deployments before scaling]({static}/images/part1/task3/deployment.png)


Poddar som er deploya finn man slik
```
kubectl get pods 
```
![deployments before scaling]({static}/images/part1/task3/pods1.png)


Her skalerer vi backend deploymenten opp til 3 replicas. Det vil sei at vi får 3 poddar når oppskaleringa er ferdig.
```
kubectl scale deployment/version-backend-deployment --replicas=3
```

For å sjå på endring kan vi liste ut deployments slik
```
kubectl get deployments
```
![deployments before scaling]({static}/images/part1/task3/deployment2.png)


Og poddar slik
```
kubectl get pods
```
![deployments before scaling]({static}/images/part1/task3/pods2.png)


Ein kan også bruka lablar til å lista ut ein spesifikk type pod
```
kubectl get pods -l app=version-backend
```
![deployments before scaling]({static}/images/part1/task3/pods3.png)

## Oppgave 3c - Åpne frontend tjenesten i nettlesaren din

For å få dette til må du liste ut tjenester slik

```
kubectl get services
```
![services]({static}/images/part1/task3/services.png)

Kopier ut den lange dns strengen under "EXTERNAL-IP" og klask den inn i nettleseren din og trykk enter

![ellol]({static}/images/part1/task3/version_fail.png)
**Men ka farsken, detta funka jo ikkje. Er da ølagt!!!!?** Eller er da? 


## Oppgave 3d - Port-forward for å få kontakt med backend
For å få frontend til å prate med backend i dette tilfellet, må vi sette opp port-forwarding mot backend tjenesten mot port 5000 lokalt. Alternativet er å bruke ein sentral tjeneste eller ein ingress med ein sentral dns. Men desse tinga er utenfor denne workshoppen.

Liste ut navnet på backend tjenesten
```
kubectl get services -l app=backend
```
![backend service]({static}/images/part1/task3/backend_service.png)

Så kan vi kjøre ein port-forward kommando. Hugs at frontend no forventar trafikk på localhost port 5000 og ikke port 80
```
kubectl port-forward service/version-backend-service 5000:80
```
![port-forward cmd]({static}/images/part1/task3/port_forward.png)

No kan du åpne nettlesaren din igjen og sjå på frontend applikasjonen.

![working]({static}/images/part1/task3/working_front.png)

Du er no ferdig! Hjelp andre dersom andre ikkje er ferdig. Evt. gå og hent deg ein kaffi ;)
