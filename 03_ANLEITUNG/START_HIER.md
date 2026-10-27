# AKTUELL: V2.9.14 KALENDER KONFLIKT TEST – NICHT PRODUKTIV FREIGEGEBEN

Bitte zuerst `AENDERUNGEN_V2.9.14.md` und `TEST_TODO_V2.9.14.md` lesen. Basis V2.9.13; ältere Hinweise unten sind historisch. Nur `01_GITHUB_UPLOAD/` enthält die Webdateien. Firebase-Regeln nicht ungeprüft einspielen.

# AKTUELL: V2.9.12 SAMMELTEST – NICHT PRODUKTIV FREIGEGEBEN

Bitte zuerst `AENDERUNGEN_V2.9.12.md` und `TEST_TODO_V2.9.12.md` lesen. Basis V2.9.11; ältere Hinweise unten sind historisch. Nur `01_GITHUB_UPLOAD/` enthält die Webdateien. Firebase-Regeln nicht ungeprüft einspielen.

---

# AKTUELL: V2.9.11 SAMMELTEST – NICHT PRODUKTIV FREIGEGEBEN

Bitte zuerst `AENDERUNGEN_V2.9.11.md` und `TEST_TODO_V2.9.11.md` lesen. Basis V2.9.10; ältere Hinweise unten sind historisch. Nur `01_GITHUB_UPLOAD/` enthält die Webdateien. Firebase-Regeln nicht ungeprüft einspielen.

---

# AKTUELL: V2.9.2 WHITEBOARD SESSION TEST – NICHT PRODUKTIV FREIGEGEBEN

Bitte zuerst `WHITEBOARD_SESSION_FIX_V2.9.2.md` lesen. Dieses Paket korrigiert den mehrfachen Anmelde-Dialog in Cup, Doppel-KO und Solo-Pyramide, ist aber am Samsung noch nicht praktisch getestet. Keine Firebase-Regeln ungeprüft übernehmen. Den produktiven GitHub-Stand nicht überschreiben.

---

# EC Wegscheid – Vollständiges Datenpaket V2.8.7

**Stand:** 16.10.2026  |  **Paketstatus:** geprüfter Dateisnapshot / KEINE Produktionsfreigabe

Dieses Paket wurde aus dem zuletzt vorhandenen Komplettarchiv `EC_Wegscheid_V2.5.4_GMAIL_EINZELTEST_V2.8.7_KOMPLETT.zip` zusammengestellt. Die vorhandenen Programmdateien wurden inhaltlich unverändert übernommen. Fehlende Web-App-Icons und das Manifest wurden ergänzt. Interne Buildskripte und historische Testhinweise wurden aus dem GitHub-Upload herausgenommen.

## Verzeichnisse

- `01_GITHUB_UPLOAD/`: **Nur diesen Inhalt** in das GitHub-Pages-Repository hochladen (nach Freigabe).
- `02_FIREBASE_REGELN/`: Referenz der Firestore-Regeln und optionale Firebase-CLI-Konfiguration. **Nicht blind veröffentlichen.**
- `03_ANLEITUNG/`: GitHub-Anleitung, Firebase-Prüfbericht, Testliste, Release-Metadaten und Prüfsummen.
- `04_QUELLCODE_WERKZEUGE/`: historische interne Buildskripte und Hinweise; **nicht auf GitHub hochladen**.

## Wichtige Grenzen

1. Das vorhandene Programm ist der zuletzt verfügbare **Gmail-Einzeltest V2.8.7**. Der besprochene vollständige Gmail-Serienversand (Phase 3, Brotzeit-Mehrfachfilter, sichere Doppelsendsperre, erneutes Senden, BCC-Kontrollkopie) ist in diesem Quellstand **noch nicht umgesetzt**. Phase 1/2 sind nur teilweise vorhanden.
2. Der Browserdruck kann die Kopienanzahl nicht technisch auf 1 begrenzen. Eine serverseitig durchgesetzte 10-Sekunden-Sperre ist in diesem Quellstand ebenfalls nicht nachgewiesen.
3. Die Firestore-Referenzregeln haben bekannte Datenschutz-/Sicherheitsrisiken. Kein Live-Regel-Export und keine Live-Datenbankprüfung war möglich.
4. Das Paket enthält **keine** Firestore-Livedaten, Firebase-Authentication-Nutzer/Passwörter, Cloud-Storage-Daten, Gmail-OAuth-Tokens oder private Backups.
5. Das alte `version.json` im Webordner enthält historische Versionskennzeichen; es wurde absichtlich nicht verändert, um die Versions-/Neuladelogik nicht ohne Regressionstest anzupassen. **V2.8.7 bezeichnet die Gesamtpaketversion.**

**Empfehlung:** Als lokalen Sicherungsstand archivieren und zuerst im Live Server testen. Für einen öffentlichen GitHub-Rollout die Sicherheitsprobleme beheben und den Funktionsumfang mit den Erwartungen abgleichen.
