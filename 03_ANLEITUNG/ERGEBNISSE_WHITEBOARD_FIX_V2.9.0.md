# EC Wegscheid – V2.9.0 Whiteboard-Ergebnisprogramme (TEST)

## Ausgangsfehler
- Solo-Pyramide: „Benutzer nicht freigegeben“.
- Jahresmeisterschaft Ziel und Doppel-KO: Login wird akzeptiert, anschließend Sprung ins Startmenü.
- Stockdart bleibt gesperrt.

## Technische Befunde und Korrekturen
1. `auswertung-teil-06.js`: Nach Login wurde bei allen Zielen außer Jahresmeisterschaft `showHome()` ausgeführt. Nun wird der ursprünglich angeforderte Deep-Link geöffnet (auch Doppel-KO). Die zentrale Benutzerrolle wird vorher aus Firestore geladen.
2. `hauptprogramm.js`: Der öffentliche Whiteboard-Modus war nicht gleichbedeutend mit einer echten Firebase-Anmeldung. Interne Ergebnisprogramme verlangen nun zuerst eine bestehende Firebase-Sitzung und prüfen das reale Benutzerprofil in `users/{uid}`. Ohne Sitzung wird die zentrale Anmeldung angezeigt und der gewählte Button nach erfolgreichem Login erneut geöffnet.
3. `solo-pyramide.js`: Das eingebettete Programm übernimmt Whiteboard-Rechte nur, wenn die Elternseite die angemeldete Benutzerkennung anhand von Firestore verifiziert hat.
4. `auswertung-teil-01.js`: Ein URL-Parameter `whiteboard=1` alleine darf keine Whiteboard-Rechte vergeben.
5. Browser-Versionsparameter der Turnierauswertung aktualisiert.

## Testanleitung (separates Test-Repository)
1. V2.8.9 und aktuelle Firebase-Daten sichern. NICHT direkt in den Produktivstand laden.
2. Nur `01_GITHUB_UPLOAD` in die separate GitHub-Testseite hochladen.
3. Auf dem Whiteboard mit bestehender Firebase-Informationssystem-Anmeldung die 3 Fehlerbereiche testen. Ohne bestehende Firebase-Sitzung ist eine einmalige Anmeldung erforderlich; danach soll die dauerhafte Firebase-Sitzung greifen, sofern der Samsung-Browser sie speichert.
4. Solo-Pyramide, Jahresmeisterschaft Ziel und Doppel-KO müssen ohne zweite Login-Schleife aufrufbar sein.
5. Stockdart bleibt gesperrt. Als unberechtigter Nutzer und ohne Anmeldung dürfen `?whiteboard=1` und `?mode=whiteboard` keinen Zugriff verschaffen.
6. Test auch nach vollständigem Samsung-Neustart; lokale Sitzungsdauer hängt vom Browser ab.
7. Adminzugriff und Daten-Synchronisation am PC ebenfalls prüfen.

## Wichtige Grenzen
- Quellcode- und Syntaxprüfungen ersetzen keinen echten Test mit Firebase und Samsung.
- Firestore-Regeln sind unverändert und haben die zuvor festgestellten Sicherheitsprobleme.
- Der Whiteboard-Browser kann Firebase-LOCAL-Persistenz nach Neustart verlieren. In diesem Fall muss das Anmelde-/Hostingkonzept weiter angepasst werden; keine Passwörter im JavaScript hinterlegen.
- V2.9.0 ist eine Testpaket-Version, keine bestätigte stabile Produktivversion.
