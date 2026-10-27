# EC Wegscheid – Verwaltungsmenü V2.9.4 TEST

Basis: V2.9.3 (Linköffnung), inklusive Whiteboard-Sitzungskorrekturen aus V2.9.2.

## Änderungen

- Startseite bearbeiten steht direkt über Turnierplaner.
- Eigene Turniereinladungen steht direkt unter Turnierverwaltung.
- Zeitungsberichte stehen direkt unter Fotos für Diashow.
- Turnierwirtschaftlichkeit steht direkt unter Dokumente & Drucken verwalten.
- Systemeinstellungen steht direkt unter Benutzer & Rechte.
- Links für die Startseite werden direkt **innerhalb** von Startseite bearbeiten angezeigt. Der eigenständige Menüknopf entfällt.
- Whiteboard-Freigaben werden direkt **innerhalb** von Benutzer & Rechte angezeigt. Der eigenständige Menüknopf entfällt.
- Speicher verwalten wird direkt **innerhalb** von Datensicherung angezeigt. Der eigenständige Menüknopf entfällt.
- In Dokumente & Drucken verwalten gibt es für gespeicherte PDFs nun **Vorschau** (eingebettetes PDF) und **Separat öffnen**. Die Vorschau hängt von der PDF-Unterstützung des Browsers ab.

Alle Bereiche der linken Menüleiste bleiben auf derselben Ebene – **keine Untermenüs**.

## Testablauf

1. Nur in einem separaten Test-Repository/auf einer Testseite bereitstellen, bestehende Produktivseite nicht überschreiben.
2. Als Admin anmelden und Reihenfolge der Menüpunkte prüfen.
3. Startseite bearbeiten: Links/Öffnungsart ändern und zentral speichern; danach Startseite prüfen.
4. Benutzer & Rechte: Whiteboard-Freigaben prüfen (NICHT versehentlich umstellen).
5. Datensicherung: Speicherinformation anzeigen. NICHT „Alle lokalen Bilder/PDF-Seiten löschen“ drücken, außer ausdrücklich beabsichtigt.
6. Dokumente & Drucken verwalten: PDF-Vorschau testen, PDF separat öffnen und ggf. drucken.
7. Whiteboard: Cup-Ergebnisse, Jahresmeisterschaft, Doppel-KO, Solo-Pyramide mehrfach öffnen; Stockdart bleibt gesperrt.
8. Linköffnung auf dem Samsung testen.

## Sicherheit und Grenzen

- Firebase-Regeln wurden nicht geändert. Die aus V2.8.7 bekannten Sicherheitsrisiken bleiben offen.
- Weder produktive Firebase-Daten noch GitHub wurden durch das Erstellen dieses ZIP verändert.
- Statische JavaScript-Syntax- und Menüstrukturprüfungen wurden durchgeführt. Kein Live-Firebase- oder Samsung-Gerätetest.
- Die PDF-Vorschau kann auf dem integrierten Samsung-Browser wegen dessen PDF-Viewer eingeschränkt sein.
- Der Menüumbau ist eine TESTVERSION, kein bestätigter stabiler Stand.
