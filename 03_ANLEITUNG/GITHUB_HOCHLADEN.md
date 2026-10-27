# GitHub Pages – Hochladen und Zurückrollen

1. **Vorher** bestehendes GitHub-Repository sichern (ZIP herunterladen oder neuen Git-Tag/Branch erstellen).
2. Den Inhalt von `01_GITHUB_UPLOAD/` lokal über VS Code Live Server testen. Keine echte Vereins-Serienmail auslösen.
3. Prüfen, ob `index.html` direkt im Root des Repositories liegt, nicht in einem zusätzlichen Unterordner.
4. Nach Datenschutz-/Sicherheitsfreigabe ausschließlich den **Inhalt** von `01_GITHUB_UPLOAD/` in das bestehende Repository `Vereinsverwaltung-Aktuell` hochladen. Vorhandene Dateien ersetzen. Interne Anleitungen, Firebase-Regeln, private Sicherungen und Zugangsdaten NICHT ins öffentliche Repository laden.
5. GitHub Pages sollte den Branch/Root verwenden, auf dem `index.html` liegt. Adresse: https://ecwegscheid.github.io/Vereinsverwaltung-Aktuell/
6. Nach Veröffentlichung Browsercache prüfen, Admin- und Whiteboard-Login, Navigation, Kalender, PDF-Anzeige, Doppel-KO und Gmail-Einzeltest. Nicht den Serienversand als vorhanden annehmen.
7. Bei Problemen auf den vorher gesicherten Git-Stand zurückrollen. Firestore-Regeln und Daten müssen separat gesichert werden.

**Achtung:** GitHub Pages ist öffentlich. Alle Dateien im GitHub-Ordner sind öffentlich abrufbar; Firebase-Web-Konfiguration ist zwar kein Geheimnis, aber Sicherheitsregeln müssen Datenzugriffe schützen.
