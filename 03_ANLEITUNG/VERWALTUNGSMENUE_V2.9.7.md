# V2.9.7 TEST – Vorschau „Dokumente und Drucken“

Basis: V2.9.6 Carbon Red Premium.

## Änderung

- Neben „Dokumente und Drucken“ im Verwaltungsmenü gibt es jetzt denselben **Augen-Button** wie bei anderen Bereichen.
- Klick auf den Text: Bearbeitungsverwaltung für Dokumente und Drucken.
- Klick auf das Auge: **Anzeigemodus**, also die normale Ansicht mit Bereichen und PDFs wie am Whiteboard.
- In der Vorschau führt der Zurück-Button zur Verwaltung; beim regulären Öffnen von der Startseite weiterhin zur Startseite.
- Die große, fälschlich als Menüvorschau eingeführte PDF-Vorschau in der Dokumentenverwaltung wurde entfernt. Die vorhandene PDF-Öffnung und die Vorschau einer neu gewählten PDF vor dem Hochladen bleiben erhalten.
- Design, Benutzerrechte, Whiteboard-Anmeldung und Firestore-Regeln unverändert.

## Test

1. Als Administrator öffnen → Verwaltungsmenü → „Dokumente und Drucken“: Bearbeitungsseite muss erscheinen.
2. Daneben auf 👁 klicken: Anzeigemodus mit Kategorien muss erscheinen.
3. Kategorie und PDF öffnen; Zurück führt wieder zur Verwaltung.
4. Von der Startseite „Dokumente Drucken“ öffnen: Zurück führt zur Startseite.
5. Whiteboard-Ergebnisprogramme und Anmeldung kurz gegenprüfen.

**Nur Testversion.** Kein echter Firebase-/Samsung-Test. Bekannte Firestore-Sicherheitsprobleme bleiben offen.
