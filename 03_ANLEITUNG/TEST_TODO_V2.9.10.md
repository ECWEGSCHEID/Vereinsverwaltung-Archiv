# EC Wegscheid – V2.9.10 – Test-To-do

**Basis:** V2.9.9. **Status:** Testversion. **Nicht ungeprüft produktiv veröffentlichen.**

## Test 1 – Benutzer und Rechte (Nachbesserung aus V2.9.9)
- [ ] Admin öffnet „Benutzer & Rechte“: vorhandene **Firestore-Benutzerprofile** und ihre Rechte erscheinen.
- [ ] „Benutzerliste aktualisieren“ funktioniert.
- [ ] „+ Neuen Benutzer hinzufügen“ zeigt den sicheren Ablauf mit direktem Link zur Firebase Authentication-Konsole.
- [ ] Ein neues Konto in Firebase Authentication anlegen, einmal anmelden und danach dessen Profil/Rechte hier prüfen.
- [ ] Whiteboard-Berechtigungen bleiben unverändert.

**Technische Einschränkung:** Eine reine Browser-Anwendung kann weder die vollständige Firebase-Authentication-Kontenliste abrufen noch Konten mit Admin-Schutz anlegen. Der Button führt daher durch den gesicherten Konsolen-Ablauf; es gibt in dieser Version **noch keine vollständige In-App-Auth-Benutzeranlage**. Für diese wäre ein autorisierter Serverdienst/Cloud Function erforderlich. In der Verwaltung gelistet werden Firestore-Profile, nicht alle Firebase-Auth-Konten.

## Test 2 – Geburtstagsfilter
- [ ] „Altersgrenzen & Beitrag“ öffnen; die zusätzliche Monatsauswahl ist entfernt.
- [ ] 6-Monats- und Halbjahresauswahl funktionieren weiterhin.

## Test 3 – Spaltenauswahl
- [ ] „Admin-Menü → Anzeige“: „Nachname“ und „Vorname“ erscheinen einzeln mit Kontrollkästchen.
- [ ] Beide lassen sich unabhängig aus- und wieder einblenden.
- [ ] Nach Speichern/Neuladen bleibt die Auswahl bestehen.

## Test 4 – Fotos Diashow
- [ ] Unterhalb der Fotos sind die doppelten Eingabefelder für Ordnername, Darstellung und Wechselzeit verschwunden.
- [ ] „Ordner bearbeiten“ springt zur oberen Eingabemaske; dort ändern und speichern.
- [ ] „Ordner löschen“ befindet sich direkt oben am jeweiligen Ordner.
- [ ] **Nur mit Testordner**: Löschen bestätigen und danach speichern; prüfen, ob die Löschung in Firebase ankommt.

## Test 5 – Fotos Sponsoren
- [ ] Dieselben Punkte wie Test 4 für die Sponsorendiashow prüfen.
- [ ] Keine bestehenden Sponsorenfotos zum Test löschen; Testordner verwenden.

## Test 6 – Vereinsnachrichten
- [ ] Eine **Testnachricht** speichern und in Firebase verifizieren.
- [ ] Testnachricht löschen und Sicherheitsabfrage bestätigen.
- [ ] Erfolgsmeldung erst nach erfolgreicher Firebase-Löschung; Nachricht verschwindet sofort aus der Liste.
- [ ] Verwaltung neu laden: gelöschte Nachricht darf nicht wieder erscheinen.
- [ ] Test mit absichtlich verweigerter Verbindung: keine falsche Erfolgsmeldung.
- [ ] Nachricht mit Enddatum gestern: auf der Startseite unsichtbar, im Admin-Menü als „ABGELAUFEN“ erkennbar.

**Ablaufdatum:** Abgelaufene Nachrichten werden automatisch ausgeblendet, **nicht automatisch endgültig gelöscht**. Sie bleiben für spätere Nachvollziehbarkeit gespeichert und können gezielt gelöscht werden.

## Regression – bisher funktionierende Bereiche
- [ ] Whiteboard: Cup-Ergebnisse, Doppel-KO, Solo-Pyramide, Ziel-Jahresmeisterschaft wiederholt ohne neue Anmeldung öffnen.
- [ ] Stockdart bleibt am Whiteboard gesperrt.
- [ ] Mitgliedsantrag übernimmt weiterhin den aktuellen Mitgliedsbeitrag.
- [ ] Serienbrief: ausgewähltes Dokument entfernen.
- [ ] Dokumente und Drucken: Ansichtsvorschau über Augen-Button.

## Noch offen auf der großen To-do-Liste
- [ ] Sponsoren-E-Mail-Versand mit echten Sponsorendaten testen (derzeit keine vorhanden).
- [ ] Geschützte serverseitige Benutzeranlage und vollständige Firebase-Authentication-Benutzerliste ergänzen.
- [ ] Bekannte Sicherheitsprobleme der Firebase-Referenzregeln beheben; **Regeln nicht ungeprüft veröffentlichen**.
- [ ] Raspberry Pi 3B / HP-Druckserver einrichten und testen.
