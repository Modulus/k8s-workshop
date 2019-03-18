Title: Del 1 Oppgave 3
Date: 2019-03-15 13:29
Tags: introduction,main,k8s,kubernetes,del1-oppgave3,del1
Slug: Del1-Oppgave3
Authors: John Sigvald Skauge
Summary: Oppgave liste og introduksjon
Category: Del 1

Her er oppgave 3. Her skal vi sjå meir på port-forwarding og skalering av kjørandes applikasjonar.


### Oppgave 3a
No skal du deploye ein oppgradert versjon av applikasjonen fra forrige oppgave. Denne versjonen returnerer json-data og har ein frontend som pollar data ca 1 gang per sekund.

```
kubectl apply -f full.yml
```


### Oppgave 3b
Manifestet fra forrige oppgave deployar kun 1 replica av både frontend og backend tjenesten. Desse skal vi no skalere opp til å kjøre 3 instansar av klar tjeneste.

```
kubectl get deployments
```

```
kubectl scale deployment/version-backend-deployment --replicas=3
```

```
kubectl get deployments
```


```
kubectl get pods -l app=version-backend
```

### Oppgave 3c - Åpne frontend tjenesten i nettlesaren din


### Oppgave 3d - Port-forward for å få kontakt med backend
For å få frontend til å prate med backend i dette tilfellet, må vi sette opp port-forwarding mot backend tjenesten mot port 5000 lokalt. Alternativet er å bruke ein sentral tjeneste eller ein ingress med ein sentral dns. Men desse tinga er utenfor denne workshoppen.

Du er no ferdig! Hjelp andre dersom andre ikkje er ferdig. Evt. gå og hent deg ein kaffi ;)
