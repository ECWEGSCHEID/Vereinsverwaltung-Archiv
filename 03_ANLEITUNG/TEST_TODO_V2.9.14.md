# EC Wegscheid – V2.9.14 Kalender-Konflikte: Test-To-do

**Basis:** V2.9.13. **Testversion, nicht als produktiv freigegeben.** V2.9.11 ist der letzte vom Verein vollständig bestätigte Stand. Bestehende Google-Client-ID und Kalender-ID nicht verändern. Firebase-Regeln nicht austauschen.

## Fehlerbehebung V2.9.14

- [ ] Termin- und Turnierplaner → Kalendereinstellungen → **„Jetzt abgleichen“** anklicken.
- [ ] Den bisherigen Konflikt aus V2.9.13 suchen. Unter der Meldung erscheint ein Kasten mit dem Termin und den unterschiedlichen Daten **Programm / Google**.
- [ ] Für den bekannten Testtermin **„Google übernehmen“** wählen und Sicherheitsabfrage bestätigen.
- [ ] Kontrollieren, dass die geänderte **Uhrzeit aus Google** im Programm angekommen ist (ggf. Ansicht neu öffnen).
- [ ] Den gleichen Termin im **Programm** erneut bearbeiten (z. B. um 15 Minuten verschieben). Speichern; die Änderung muss im **bestehenden** Google-Ereignis ankommen.
- [ ] Danach die Uhrzeit wieder **direkt in Google** ändern, im Programm „Jetzt abgleichen“ drücken: neue Uhrzeit muss übernommen werden.
- [ ] Testen: Änderungen an Name, Datum und Ort in Google werden ebenfalls übernommen.
- [ ] Nur bei einem bewusst herbeigeführten Doppelkonflikt (beide Seiten geändert) „Programm übernehmen“ prüfen: Google muss den bestehenden Eintrag aktualisieren, kein neuer Termin.
- [ ] „Abbrechen“ prüfen: Es wird nichts überschrieben, Konflikt taucht beim nächsten Abgleich erneut auf.
- [ ] Prüfen, dass gemeldete Spieler, Turnierart, interne Kennzeichen und andere Daten bei der Google-Übernahme unverändert bleiben.
- [ ] Prüfen, dass keine doppelten Google-Termine entstehen und gelöschte Google-Einträge nicht automatisch neu erstellt oder lokal gelöscht werden.

## Hinweis zu alten Einträgen

Für V2.9.13-Einträge ohne gespeicherten Vergleichsstand kann zunächst **ein Konflikt zur manuellen Entscheidung** erscheinen. Das ist gewollt. Nach „Google übernehmen“ oder „Programm übernehmen“ wird der Kalender-Vergleichsstand gespeichert. Künftige Änderungen lassen sich dann zuverlässig von bloßen Spieler- oder Anmeldungsänderungen unterscheiden.

## Weitere Tests aus V2.9.13

- [ ] Verwaltung → Startseite verwalten → Verbände, Regelwerk und Sonstiges: Link bearbeiten, hinzufügen, sortieren und löschen; in Firebase speichern; am Whiteboard kontrollieren.
- [ ] Startseite anzeigen → Zurück zur Verwaltung: Rückbutton und erhaltene Anmeldung prüfen.
- [ ] Veranstaltungsübersicht: Bearbeiten/Löschen vorhanden; unnötige manuelle Google-Buttons entfernt.

## Offene Aufgaben (nicht in dieser Version behoben)

- [ ] Firebase-Sicherheitsregeln (Punkt 44) prüfen.
- [ ] Sichere Firebase-Auth-Benutzerverwaltung (Punkt 43).
- [ ] Firebase-Dokumente und Druckfunktion (Windows-11-Mini-PC/HP-Drucker).
- [ ] Serienversand und Sponsoren-Mail mit PDF-Anhang testen.
- [ ] Optional: Hintergrundsynchronisierung auch bei geschlossenem Browser.

## Technische Prüfung

- JavaScript-Syntaxprüfung der Webdateien.
- Sechs simulierte Kalenderfälle: Altbestand-Konflikt + Google übernehmen; Spieleränderung ohne Termin-Konflikt; echter Doppelkonflikt + Programm übernehmen; Abbrechen; gelöschter Google-Termin; unveränderte Google-Version bei lokal geändertem Termin.
- Keine echten Google-/Firebase-Zugriffe durch den Ersteller ausgeführt. Bitte mit dem bekannten Testtermin prüfen, **nicht** sofort mit allen produktiven Terminen.
