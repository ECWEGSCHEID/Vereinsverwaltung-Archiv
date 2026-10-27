# EC Wegscheid – V2.9.11 Test-To-do

**Basis:** V2.9.10. **Private Testversion.** Vor dem Überschreiben der produktiven Version Sicherung anlegen. Nicht öffentlich veröffentlichen.

## Test 1 – Benutzer, Rechte und Datensicherung
- [ ] Im Verwaltungsmenü steht **Benutzer, Rechte und Datensicherung**.
- [ ] Die alten separaten Menüpunkte **Benutzerkennwort ändern** und **Datensicherung** sind dort nicht mehr vorhanden.
- [ ] Im neuen Bereich sind beide Funktionen als Schaltflächen vorhanden.
- [ ] **Benutzerkennwort ändern** öffnet die bestehende Kennwortseite und führt anschließend zurück.
- [ ] **Datensicherung öffnen** zeigt die bisherigen Sicherungsfunktionen; Zurück führt zum Benutzerbereich.
- [ ] Vorhandene Firestore-Benutzerprofile zeigen mindestens Benutzername/Anzeigename, E-Mail und Rolle.
- [ ] Rechte lassen sich nach Aufklappen weiterhin ansehen und berechtigt bearbeiten.

## Test 2 – Kommende Geburtstage
- [ ] Ein Mitglied, das 2026 70 wird, zeigt vor dem Geburtstag **70 Jahre** (nicht 69).
- [ ] Bei der Anzeige **Nächste 6 Monate** über den Jahreswechsel wird ein Geburtstag 2027 mit dem Alter für **2027** dargestellt.
- [ ] Runde Geburtstage werden korrekt eingeordnet, ohne Doppeleinträge in der normalen Liste.

## Test 3 – Navigation der Ergebnisprogramme
- [ ] Aus **Verwaltung → Doppel KO System**: einmaliger Button **Zurück zur Verwaltung**.
- [ ] Aus **Verwaltung → Interne Cup/Cup-Auswertung**: kein doppelter Hauptmenü-Button; Rücksprung zur Verwaltung.
- [ ] Interne Cup-Detailnavigation (Gruppen, Spiele, Tabelle) funktioniert weiterhin.
- [ ] Solo-Pyramide bleibt korrekt.
- [ ] Jahresmeisterschaft Ziel, Turnierauslosung und Stockdart im jeweils erlaubten Modus auf korrekte Rücknavigation prüfen.
- [ ] Startseite → Verwaltung → Startseite → Verwaltung: **keine erneute Anmeldung**, solange die Sitzung gültig ist.
- [ ] Whiteboard-Berechtigungen und Whiteboard-Ansichten unverändert.

## Test 4 – Turnierwirtschaftlichkeit und Helfer
- [ ] Menü und Kopfzeile heißen **Turnierwirtschaftlichkeit und Helfer**.
- [ ] Jahresabrechnung: **links Sponsoring-Übersicht**, **rechts Jahresabrechnung**.
- [ ] Links: **Sponsoreinnahmen**, **alle Kosten für Preise**, **noch verfügbares Sponsorgeld**; keine zusätzliche Gesamtsumme.
- [ ] Rechts: erst **Einnahmen** (Startgeld, Gastro, Sponsorengelder, weitere Turniereinnahmen), dann **Ausgaben** (Preise, Gastro, weitere Turnierausgaben, weitere Jahresausgaben), ganz unten **Jahresgewinn**.
- [ ] Eingabe **Weitere Jahresausgaben** speichern, Seite neu öffnen, Betrag und Jahresgewinn prüfen.
- [ ] Sponsorengelder im Jahresgewinn nur einmal berücksichtigt; Sachspenden nicht als Geldzufluss.
- [ ] Andere Jahre und Jahresvergleiche sowie Helferplanung bleiben unverändert funktionstüchtig.

## Regression und offene Punkte
- [ ] Vereinsnachrichten: Testnachricht anlegen/löschen, nach Neuladen verschwunden.
- [ ] Fotos Diashow / Fotos Sponsoren: Ordnerbearbeitung und Löschbutton oben.
- [ ] Mitglieder: Aufnahmeantrag mit aktuellem Beitrag, Vorname/Nachname-Spalten, Serienbrief-Dokument entfernen.
- [ ] Cup, Doppel-KO, Solo-Pyramide und Whiteboard-Login erneut testen.
- [ ] Sponsoren-Gmail-Versand erst testen, sobald Sponsorendaten vorliegen.
- [ ] Vollständige Firebase-Authentication-Benutzerliste und sichere direkte Kontoanlage erfordern einen privilegierten Backend-Dienst.
- [ ] Sicherheitsprüfung der Firebase-Regeln weiterhin offen; keine ungeprüfte Regeländerung vornehmen.
