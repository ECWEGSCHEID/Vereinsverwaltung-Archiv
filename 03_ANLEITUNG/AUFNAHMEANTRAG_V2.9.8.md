# EC Wegscheid – V2.9.8 – Aufnahmeantrag korrigiert

Grundlage: Testversion V2.9.7.

## Änderung
- In **Mitgliederverwaltung → Aufnahmeantrag** wurde die bisherige HTML-Ersatzvorlage entfernt.
- Die vom Verein hochgeladene Originaldatei liegt unverändert unter `01_GITHUB_UPLOAD/assets/Mitgliedsantrag.pdf`.
- Direktansicht im Verwaltungsbereich sowie „PDF öffnen / drucken“ und „PDF herunterladen“.
- Die PDF enthält das Logo, den SEPA-Teil, die Datenschutzerklärung und die Unterschriftsfelder der Vorlage.
- Die frühere Eingabemaske zum Vorbefüllen entfällt mit dieser Umstellung; die PDF ist eine Blankovorlage zum Ausfüllen.
- Die Vorlage nennt **16,00 EUR** und **Stand 2020**. Diese Angaben wurden nicht verändert. Bitte vor produktivem Einsatz fachlich prüfen.

## Test
1. `01_GITHUB_UPLOAD` vollständig in eine getrennte GitHub-Testumgebung hochladen.
2. Mitgliederverwaltung → Verwaltung → Aufnahmeantrag öffnen.
3. PDF-Vorschau kontrollieren, „PDF öffnen / drucken“ und „PDF herunterladen“ testen.
4. Den Ausdruck auf DIN A4 mit der Original-PDF vergleichen.
5. Übrige Verwaltungsfunktionen und Whiteboard-Anmeldung stichprobenartig prüfen.

## Sicherheit
- Keine Firebase-Regeln oder Daten geändert.
- Keine Zugangsdaten in die PDF eingefügt.
- Achtung: In einem öffentlichen GitHub-Repository ist auch die hochgeladene PDF öffentlich abrufbar.
- Diese Version ist nicht am realen Whiteboard oder Drucker getestet.
