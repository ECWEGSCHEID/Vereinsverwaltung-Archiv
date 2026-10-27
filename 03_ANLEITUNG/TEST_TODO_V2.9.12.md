# EC Wegscheid – V2.9.12 Test-To-do

**Basis:** V2.9.11 (vom Verein vollständig getestet). **Neue private Testversion.** Vor dem Hochladen den bisherigen Stand sichern. Firebase-Sicherheitsregeln unverändert; nicht ungeprüft produktiv veröffentlichen.

## Test 1 – Bezeichnung Termin- und Turnierplaner
- [ ] Verwaltungsmenü zeigt „Termin- und Turnierplaner“.
- [ ] Verwaltungsübersicht zeigt denselben Namen.
- [ ] Im Untermenü stehen Überschrift und Schaltfläche „Termin- und Turnierplaner“.
- [ ] Vorhandene Termine, Spielerliste und Einstellungen bleiben unverändert.

## Test 2 – Rückkehr von der Startseite
- [ ] Angemeldet als Administrator: Verwaltung → „Startseite anzeigen“ (Augensymbol bei „Startseite bearbeiten“).
- [ ] Rechts unten erscheint gut sichtbar „← Zurück zur Verwaltung“.
- [ ] Auf der Startseite ein Untermenü öffnen, zurückkehren: Button bleibt sichtbar.
- [ ] Klick öffnet die Verwaltung, **ohne** erneute Anmeldung.
- [ ] Beim normalen Whiteboard-/Informationsmodus ohne Admin-Vorschau erscheint dieser Button nicht.

## Test 3 – Bestehende Veranstaltungen
- [ ] Im Bereich „Vorhandene Veranstaltungen“ sind nur noch „Bearbeiten“ und „Löschen“ vorhanden.
- [ ] „In Google aktualisieren“, „Duplikate prüfen“, „Export prüfen“ werden **nicht mehr in dieser Liste** angezeigt.
- [ ] Veranstaltung bearbeiten und speichern: Termin im Programm und in Firebase korrekt.
- [ ] Bei bestehender Google-Verbindung wird der verknüpfte Google-Termin weiterhin aktualisiert (keine neue Kopie).

## Test 4 – Google Kalender → Vereinsverwaltung
**Nur mit einem eigens angelegten Testtermin prüfen! Keine produktiven Veranstaltungen für den Ersttest verändern.**
- [ ] In „Kalendereinstellungen“ Google verbinden und abgleichen. Der Abgleich meldet die Anzahl geprüfter und geänderter Termine.
- [ ] Ein bereits **mit Google verknüpftes** Testereignis im Google Kalender umbenennen oder Datum/Uhrzeit/Ort ändern.
- [ ] In der Verwaltung „Termin- und Turnierplaner“ öffnen (bei noch gültiger Google-Verbindung) oder in den Kalendereinstellungen „Mit Google verbinden und abgleichen“ wählen.
- [ ] Der geänderte Termin wird in Firebase und im Programm aktualisiert; **kein zweiter Termin** entsteht.
- [ ] Spielernamen, „Gemeldet von“ und Veranstaltungsart bleiben unverändert.
- [ ] Testweise gleichzeitig auf beiden Seiten ändern: Konflikt wird gemeldet; keine stille Überschreibung.
- [ ] Testweise verknüpften Google-Testtermin löschen: im Programm wird er **nicht automatisch gelöscht**, sondern als fehlend gemeldet.
- [ ] Nach Ablauf der OAuth-Verbindung muss der Administrator Google gegebenenfalls erneut verbinden. Eine echte serverseitige Hintergrund-Synchronisierung ohne offenen Browser ist **noch nicht enthalten**.
- [ ] Alte .ics-Exporte ohne gespeicherte Google-Ereignis-ID werden aus Sicherheitsgründen **nicht automatisch übernommen**.

## Regression
- [ ] Cup, Doppel-KO, Solo-Pyramide und Navigation zur Verwaltung funktionieren weiterhin.
- [ ] Jahresabrechnung und Sponsoring-Übersicht unverändert korrekt.
- [ ] Vereinsnachrichten, Foto-Diashow, Mitgliederverwaltung und Benutzerverwaltung funktionieren.
- [ ] Auf Samsung WM65B prüfen, dass die Rückkehr-Schaltfläche sichtbar und gut bedienbar ist.

## Weiterhin offene große To-do-Liste
- [ ] **Punkt 43:** Sichere vollständige Firebase-Auth-Benutzerliste und direkte Benutzeranlage (Backend erforderlich).
- [ ] **Punkt 44:** Firebase-Sicherheitsregeln und Datenschutz umfassend prüfen.
- [ ] Sponsoren-Gmail-Versand mit PDF testen, sobald Sponsorendaten vorliegen.
- [ ] Dokumentenanzeige und Drucken über den Windows-11-Mini-PC abschließen.
- [ ] Serienversand und ggf. weitere E-Mail-Funktionen abschließen.
- [ ] Optional: echte serverseitige kontinuierliche Google-Kalender-Synchronisierung (OAuth/Cloud Functions), falls Änderungen ohne geöffneten Verwaltungsbrowser übernommen werden sollen.
