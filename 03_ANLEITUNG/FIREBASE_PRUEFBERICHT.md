# Firebase / Firestore – Prüfergebnis V2.8.7

## Ergebnis

**Keine neue Firestore-Collection ist für den vorhandenen Gmail-Einzeltest nötig.** Das Programm aktualisiert das Feld `gmailTestversand` in `turniere/{turnierId}`; die beigefügte Regel erlaubt angemeldeten Nutzern mit `tv`-Bearbeitungsrecht den Schreibzugriff auf `turniere`. Kalender-Termine verwenden `tournamentPlanner`; PDF-Dokumente verwenden `appSettings/druckdokumente` und `appSettings/druckpdf_*`; Doppel-KO verwendet `doppelKoTurniere`. Diese Pfade sind in der beigefügten Referenzregel abgebildet.

**ABER:** Es wurde nicht auf das Firebase-Projekt zugegriffen. Ob die **tatsächlich veröffentlichten** Regeln bereits identisch sind, lässt sich aus dem ZIP nicht feststellen. Deshalb lässt sich keine sichere Aussage „Regeln ändern: nein“ für das Livesystem treffen.

## Kritische Risiken in den mitgelieferten Referenzregeln

1. `soloPyramide/state` ist für alle lesbar, einschließlich des Feldes `passwords`, das laut Sicherheitsbericht noch Spielerpasswörter im Klartext enthält. **Kritisch**: Umstellung der Passwortverwaltung und Regeln nötig.
2. `soloPyramide/state` erlaubt anonymes Anlegen und Ändern von spielrelevanten Feldern. Eine rein clientseitige Passwortprüfung ist keine belastbare Zugriffskontrolle.
3. `tournamentPlanner/{id}` erlaubt anonym das Ändern von `players`, `reportedBy` und `updatedAt` an bestehenden Terminen. Dadurch sind öffentliche Manipulationen möglich.
4. `turnierauswertung/cup` erlaubt öffentliche Schreibzugriffe auf Turnierdaten. Datenmanipulation ist möglich.
5. `appSettings/{id}` ist für jedes vorhandene Benutzerprofil lesbar; `druckdokumente` und `druckpdf_*` sind öffentlich lesbar. Dort dürfen nur ausdrücklich öffentliche PDF-Dateien liegen. Schreibrechte für `appSettings` sind für Benutzer mit `sh`/`lk` sehr breit.
6. `doppelKoTurniere` erlaubt dem Whiteboard-Profil auch das Löschen von Turnieren; Rechte prüfen.
7. In der veröffentlichten Webseite sind feste Namen/Termine in Startdaten eingebettet. Öffentliche Veröffentlichung auf datenschutzrechtliche Zulässigkeit prüfen.

## Vorgehen vor Änderungen

1. In Firebase Console → Firestore Database → Regeln die **aktuell veröffentlichten Regeln vollständig sichern**.
2. Diese mit `02_FIREBASE_REGELN/firestore.rules` vergleichen. Keine pauschale Überschreibung.
3. Testfälle mit Firebase Rules Simulator/Emulator: anonym, Admin, Whiteboard, Turnierverwaltung, Mitgliederverwaltung. Sowohl erlaubte als auch verbotene Lese-/Schreibvorgänge prüfen.
4. Die Solo-Pyramide braucht eine neue, serverseitig überprüfbare Anmeldung bzw. eine andere sichere Datenstruktur, bevor öffentliche Zugriffe auf sensible Daten ausgeschlossen werden können. Keine pauschale Regeländerung ohne Anpassung des Spielablaufs.
5. Datenschutzprüfung und Backups abschließen; erst dann produktive Regeln gezielt veröffentlichen.

## Keine enthaltenen Datenbank-Backups

Die Webdateien enthalten nur die Konfiguration für die Verbindung zum Firebase-Projekt, **nicht** die dort gespeicherten Vereins-/Mitgliederdaten. Eine echte Sicherung muss getrennt aus dem laufenden Programm und Firebase erfolgen. Auch Auth-Konten, Storage-Dateien und veröffentlichte Regeln getrennt sichern.
