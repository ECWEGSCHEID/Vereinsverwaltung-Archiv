# EC Wegscheid – Solo-Pyramide Whiteboard-Hotfix V2.8.9

## Ausgangslage
Das Whiteboard meldet sich erfolgreich am zentralen Informationssystem an. Beim Öffnen der Solo-Pyramide erscheint dennoch die separate Passwortanmeldung.

## Ursache
In `js/hauptprogramm.js` wurde der URL-Parameter `mode=whiteboard` für die Solo-Pyramide bisher nur im *öffentlichen* Whiteboard-Modus ergänzt. Ein regulär mit Firebase angemeldeter Whiteboard-Benutzer wurde nicht erfasst. Die Solo-Pyramide verlangt dann eine separate Anmeldung; deren Standard-Informationssystem-Passwort ist in der aktuellen Fassung absichtlich nicht gesetzt.

## Korrektur
Der Whiteboard-Parameter wird nun auch bei regulär angemeldeten Whiteboard-Benutzern gesetzt. In `js/solo-pyramide.js` bleibt die zusätzliche Sicherheitsprüfung `hasCentralWhiteboardParent()` unverändert: Der Parameter allein berechtigt **nicht** zum Zugang. Der Eltern-Frame muss dieselbe Origin, einen Firebase-Login und die passende Rolle besitzen.

## Testablauf
1. Bestehenden funktionierenden Stand und Firebase-Daten sichern.
2. Nur in einer separaten Testbereitstellung den Inhalt von `01_GITHUB_UPLOAD` veröffentlichen.
3. Whiteboard als Informationssystem bei Firebase anmelden, Startseite öffnen.
4. `Ergebnisse Turniere Intern` → `Solo Pyramide` öffnen.
5. Erwartet: Pyramide öffnet ohne zweite Passwortabfrage und mit Whiteboard-Rechten.
6. `Stockdart` bleibt gesperrt. Adminfunktionen dürfen im Whiteboard nicht sichtbar sein.
7. Whiteboard vollständig neu starten und Test wiederholen.
8. Mit nicht angemeldetem Browser prüfen: `solo-pyramide.html?mode=whiteboard` darf **keine** Whiteboard-Rechte freischalten.

## Grenzen
Dies ist ein gezielter Code-Hotfix mit Syntax-/Quellcodeprüfung, **kein** Live-Test am Samsung oder an Firebase. Die zuvor festgestellten Sicherheitslücken in den Firestore-Regeln und der Solo-Pyramide sind damit **nicht behoben**. Firebase-Regeln wurden nicht geändert. V2.8.9 bezeichnet das Testpaket; bestehende interne Versionsangaben wurden nicht flächendeckend geändert.

## GitHub
Für die Testbereitstellung **nur den Inhalt von `01_GITHUB_UPLOAD`** in den Test-Repository-Root laden. Die übrigen Ordner enthalten interne Anleitungen, Regeln und Werkzeuge und gehören nicht auf die öffentliche GitHub-Pages-Webseite.
