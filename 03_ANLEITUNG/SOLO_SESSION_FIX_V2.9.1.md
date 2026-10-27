# EC Wegscheid – V2.9.1 Solo-Pyramide: erneute Anmeldung (TEST)

## Gemeldetes Verhalten
Solo-Pyramide funktioniert nach einer Anmeldung, verlangt nach „Beenden“ und erneutem Öffnen aber wieder ein Passwort. Andere Ergebnisprogramme funktionieren.

## Fehlerursache im Quellcode
Die Solo-Pyramide speichert aus Sicherheitsgründen nur Spieler-Sitzungen in sessionStorage, nicht den privilegierten Informationssystem-Login. Die Übernahme der zentralen Firebase-Sitzung war an die Whiteboard-Rollenerkennung und an den URL-Modus gebunden. Profile mit `role: whiteboard` wurden bei der zentralen Rollenerkennung nicht einheitlich behandelt.

## Änderungen
- `js/hauptprogramm.js`: Erkennung von `role: whiteboard` ergänzt. Bei jedem Aufruf wird das echte Firebase-Profil in Firestore überprüft und ein nur für diese Sitzung gültiges Whiteboard-Merkmal gesetzt. Solo-Pyramide erhält `mode=whiteboard` nur bei verifizierter Whiteboard-Berechtigung.
- `js/solo-pyramide.js`: Übernahme der eingebetteten Whiteboard-Sitzung verlangt zusätzlich das verifizierte Whiteboard-Merkmal der Elternseite.
- `index.html`, `solo-pyramide.html`: JavaScript-Cachekennung aktualisiert.
- Keine Passwörter im Browser gespeichert. Keine Firebase-Regeln und keine Firestore-Daten verändert. Stockdart bleibt gesperrt.

## Test am Samsung WM65B
1. Die vollständigen Dateien aus `01_GITHUB_UPLOAD` zuerst in eine getrennte GitHub-Testumgebung laden.
2. Am Whiteboard einmal mit dem vorhandenen Firebase-Informationssystem-Konto anmelden, falls nicht bereits angemeldet.
3. Ergebnisse Turniere Intern → Solo Pyramide öffnen; die Pyramide muss ohne eigene Anmeldung erscheinen.
4. „Beenden“ und anschließend Solo Pyramide erneut öffnen. Mindestens fünfmal wiederholen. Keine erneute Solo-Anmeldung.
5. Whiteboard einmal vollständig neu starten und Solo erneut öffnen. Falls der Samsung-Browser die Firebase-Anmeldung verwirft, ist einmaliges zentrales Login weiterhin nötig.
6. Stockdart muss weiterhin gesperrt sein. Cup, Jahresmeisterschaft Ziel, Doppel-KO und Admin-Zugang prüfen.
7. Negativtest: Solo-Pyramide direkt mit `?mode=whiteboard` ohne gültige Eltern-Sitzung darf nicht automatisch als Whiteboard öffnen.

## Grenzen
Statische Code- und Rollentests ersetzen keinen echten Test mit Firebase und dem Samsung-Browser. Die bereits dokumentierten Firestore-Sicherheitslücken bleiben bestehen. V2.9.1 ist eine Testversion, nicht als sicherer Produktivstand freigegeben.
