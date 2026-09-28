# AI Agent V1 — Opportunity Hunter

## Cos'è
Una prima base funzionante per un agente che analizza opportunità per prodotti digitali.

## Cosa fa V1
- analizza dati forniti manualmente;
- assegna un punteggio indicativo basato sulle informazioni inserite;
- salva una memoria locale;
- crea report JSON;
- non spende denaro;
- non invia messaggi;
- non pubblica;
- non effettua acquisti;
- non accede ad account.

## Avvio
Richiede Python 3.

Nel terminale, dentro questa cartella:

```bash
python agent.py
```

Per provare l'interfaccia:
apri `dashboard.html` nel browser.

## Importante
Il punteggio non è una previsione di successo: è solo un indicatore tecnico basato sui dati inseriti.

## Prossima evoluzione: V2
La V2 potrà aggiungere un browser controllato, ricerca web e strumenti con permessi espliciti.
Prima di qualsiasi azione esterna, il sistema dovrebbe fermarsi per chiedere conferma.
