# EC Wegscheid – Verwaltungsmenü V2.9.5 TEST

Basis: V2.9.4. Änderungen ausschließlich an Menüanordnung, Bezeichnung und der sichtbaren PDF-Vorschau.

## Änderungen

1. Menüpunkt „Benutzer & Rechte“ mit „Systemeinstellungen“ ans Ende der Verwaltungsnavigation verschoben. „Systemeinstellungen“ steht wie bisher direkt unter „Benutzer & Rechte“.
2. „Dokumente & Drucken verwalten“ heißt jetzt „Dokumente und Drucken“.
3. Dokumentenvorschau steht in „Dokumente und Drucken“ **oben**, ist immer sichtbar und zeigt eine Dokumentauswahl, Vorschau, separates Öffnen und Drucken. Bei vorhandenen PDFs wird das erste Dokument automatisch zur Vorschau geladen; der bisherige Vorschau-Button in jeder Dokumentzeile bleibt erhalten. Bei leerer Liste gibt es einen verständlichen Hinweis.
4. Nach Auswahl einer neuen PDF-Datei wird zusätzlich eine Vorschau **vor dem Speichern** angezeigt. Die Datei ist zu diesem Zeitpunkt nur lokal ausgewählt.
5. Der PDF-Druckdialog ist weiterhin browserabhängig; am Samsung-Browser kann die eingebettete PDF-Vorschau leer bleiben. „PDF separat öffnen“ ist der Ausweichweg. Keine Druckfunktion über Raspberry Pi enthalten.

## Tests am PC und Whiteboard

- Als Administrator anmelden: Reihenfolge am Ende prüfen (Datensicherung, Benutzer & Rechte, Systemeinstellungen).
- „Dokumente und Drucken“ öffnen: Vorschau erscheint unmittelbar oben; PDF-Auswahl ändern; PDF separat öffnen und bei Bedarf drucken. Bei leerer Liste erscheint der Hinweis.
- Vorhandene Dokumente nicht löschen. Upload und Speichern nur mit einem Test-PDF prüfen.
- Whiteboard: Ergebnisprogramme und Linköffnung weiterhin prüfen. Firebase-Regeln unverändert.

## Grenzen

Statische Tests und simulierte UI-Prüfungen sind keine Bestätigung für den Samsung-PDF-Viewer oder das produktive Firebase-Projekt. Die bekannten Sicherheitsprobleme in den mitgelieferten Firestore-Regeln bleiben bestehen. Nur in getrennter Testumgebung verwenden.
