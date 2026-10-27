# EC Wegscheid – Test-To-do V2.9.9

**Status:** Neue Sammel-Testversion, noch nicht produktiv freigegeben.  
**Grundlage:** V2.9.8 + sieben vereinbarte Änderungen in der Mitgliederverwaltung.  
**Vorgehen:** Zuerst Datensicherung, dann Testumgebung, danach die Punkte nacheinander abhaken. Änderungen an Firebase-Regeln sind nicht Bestandteil dieses Pakets.

## Vorbereitung
- [ ] Bisherige GitHub-Version und Firebase-Mitgliederdaten sichern.
- [ ] Nur `01_GITHUB_UPLOAD` in ein **separates Test-Repository / Testverzeichnis** hochladen.
- [ ] Als Administrator anmelden und Mitgliederverwaltung öffnen.
- [ ] Vorhandene Mitglieder, Sponsoren und Beiträge kontrollieren – keine produktiven Datensätze für Tests überschreiben.

## 1. Aufnahmeantrag – dynamischer Mitgliedsbeitrag
- [ ] Mitgliederverwaltung → Admin → Altersgrenzen & Beitrag öffnen; aktuellen Betrag notieren.
- [ ] Unter „Aufnahmeantrag“ prüfen, ob Vorschau, PDF-Download und Druck **denselben** aktuellen Betrag zeigen.
- [ ] In der Testumgebung Beitrag beispielsweise auf 23,50 € ändern und speichern.
- [ ] Aufnahmeantrag erneut öffnen: Überall muss **23,50 €** stehen; alte „16,00 €“ und „Stand 2020“ dürfen nicht mehr erscheinen.
- [ ] Layout, Vereinslogo, SEPA-Mandat, Bankverbindung und Unterschriftsfelder kontrollieren.
- [ ] Ursprünglichen Beitrag wiederherstellen.

## 2. Firebase-Speicherstatus
- [ ] Mitgliederverwaltung → Admin öffnen und zum Seitenende scrollen.
- [ ] Prüfen, dass der Firebase-Hinweis keinen Button mehr überdeckt.
- [ ] Auch bei kleiner Fensterhöhe und am Whiteboard prüfen.
- [ ] Ein **Testdatensatz** speichern und tatsächliche Firebase-Speicherung kontrollieren.

## 3. Sponsoren – direkter Gmail-Versand
- [ ] Unter Turnierverwaltung → Einladung senden die **bereits vorhandene Google OAuth-Client-ID** kontrollieren.
- [ ] Sponsoren → E-Mail öffnen; Empfänger, Betreff und Nachricht werden korrekt vorbelegt.
- [ ] Mit Gmail verbinden (möglicherweise zweimal klicken, falls die Google-Bibliothek erst geladen werden muss).
- [ ] **Nur mit eigener Testadresse** einen Testversand ohne Anhang durchführen.
- [ ] Zweiten Test mit kleiner PDF als Anhang durchführen; Anhang auf Richtigkeit prüfen.
- [ ] Erfolgsmeldung erst nach Bestätigung durch Gmail; bei Fehler kein automatischer Zweitversand.
- [ ] Sicherstellen, dass keine Nachricht unbeabsichtigt an einen echten Sponsor gesendet wurde.

## 4. Benutzer & Rechte
- [ ] Mitgliederverwaltung → Admin → Benutzer & Rechte öffnen.
- [ ] Statt der alten, irreführenden Felder erscheint der Hinweis auf die zentrale Firebase-Anmeldung.
- [ ] Schaltfläche „Zentrale Benutzer & Rechte öffnen“ führt zur Hauptverwaltung.
- [ ] Bestehende Firebase-Benutzer und Rollen sind unverändert.
- [ ] Kein neues Passwort wird in der alten lokalen Mitgliederverwaltung gespeichert.

## 5. Altersgrenzen & Beitrag – runde Geburtstage
- [ ] „Alle dieses Jahr“ und „Nur zukünftig“ vergleichen.
- [ ] „Januar bis Juni“ und „Juli bis Dezember“ überprüfen.
- [ ] „Nächste 6 Monate“ prüfen, besonders am Jahreswechsel (Geburtstage im Folgejahr).
- [ ] „Einzelnen Monat auswählen“ mit zwei unterschiedlichen Monaten prüfen.
- [ ] Einstellung speichern, neu öffnen und prüfen, ob sie erhalten bleibt.

## 6. Admin → Anzeige – Spalten
- [ ] Zusätzliche Felder wie Festnetz, Land, Notizen, Austrittsdatum und Zahlungsart sind auswählbar.
- [ ] Eine zusätzliche Spalte aktivieren und in der Mitgliederliste prüfen.
- [ ] Spalte wieder deaktivieren und Sortierreihenfolge mit ▲/▼ ändern.
- [ ] Seite neu laden; Auswahl und Reihenfolge sollen gespeichert bleiben.
- [ ] Bankfelder nur mit ausreichender Berechtigung sichtbar.

## 7. Serienbrief – Dokument entfernen
- [ ] Word-Dokument auswählen, Vorschau abwarten.
- [ ] „Ausgewähltes Dokument entfernen“ anklicken: Auswahl und Vorschau werden geleert.
- [ ] Neues PDF auswählen, dann sofort wieder entfernen (auch während Vorschau lädt).
- [ ] Originaldateien bleiben erhalten; andere Datei kann gewählt werden.
- [ ] Serienbrief mit neuer Datei und **nur einem Testmitglied** in Druckansicht prüfen.

## Regression – bestehende Funktionen
- [ ] Cup-Ergebnisse am Whiteboard ohne erneute Anmeldung mehrfach öffnen.
- [ ] Doppel-KO am Whiteboard ohne erneute Anmeldung mehrfach öffnen.
- [ ] Solo-Pyramide am Whiteboard ohne Passwortfehler mehrfach öffnen.
- [ ] Ziel-Jahresmeisterschaft öffnen; Stockdart bleibt am Whiteboard gesperrt.
- [ ] Dokumente und Drucken: Augen-Vorschau funktioniert weiterhin.
- [ ] Startseitenlinks: Einbettung und neuer Tab wie in V2.9.3.
- [ ] Verwaltung: Carbon-Red-Menü und Reihenfolge aus V2.9.6/2.9.7 unverändert.

## Offene Sicherheits-/Produktionsprüfungen
- [ ] Aktive Firebase-Regeln separat überprüfen; mitgelieferte Referenzregeln **nicht ungeprüft veröffentlichen**.
- [ ] Zugriff auf Mitglieder-/Bankdaten und historisch eingebettete Kontaktdaten absichern.
- [ ] Öffentliche GitHub-Dateien / privates Repository / geschützte Bereitstellung separat planen.
- [ ] **Erst nach erfolgreichem Praxistest** über die Übernahme in den Produktivstand entscheiden.

### Testergebnisse / Fehlernotizen
| Nr. | Ergebnis (OK/Fehler) | Beobachtung / Screenshot | Erledigt am |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |
| 6 | | | |
| 7 | | | |
