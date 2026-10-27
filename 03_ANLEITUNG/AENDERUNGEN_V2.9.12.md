# Änderungen V2.9.12 – Termin- und Turnierplaner

**Basis:** V2.9.11. Das neue Paket enthält alle Webdateien; nur `01_GITHUB_UPLOAD/` nach einem erfolgreichen Test für GitHub Pages verwenden.

1. Im Verwaltungsmenü, der Verwaltungsübersicht, der Anmeldeseite und dem Untermenü heißt der Bereich jetzt **Termin- und Turnierplaner**. Interne Datenbank-/Berechtigungskennungen bleiben erhalten.
2. **Startseite anzeigen** aus der Verwaltung erhält einen sichtbaren Button **Zurück zur Verwaltung** rechts unten. Der Aufrufkontext bleibt beim Wechsel innerhalb der Startseite erhalten; die Firebase-Anmeldung wird nicht absichtlich beendet. Keine Anzeige im öffentlichen Whiteboard-Modus.
3. In **Vorhandene Veranstaltungen** werden die manuellen Zusatzbuttons „In Google aktualisieren“, „Duplikate prüfen“, „Export prüfen“ und ähnliche Kalenderaktionen entfernt. Die automatische Kalenderübertragung beim Speichern bleibt bestehen.
4. **Google Kalender → Programm:** Ein Rückabgleich prüft nur eindeutig verknüpfte Google-Ereignis-IDs. Bei bestehendem gültigem Google-Zugriff erfolgt er beim Öffnen des Verwaltungsbereichs; andernfalls kann der Administrator über **Kalendereinstellungen → Mit Google verbinden und abgleichen** den Zugriff herstellen. Google-Änderungen an Titel, Datum, Uhrzeit und Ort werden nach Konfliktprüfung in Firestore übernommen. Andere Veranstaltungsfelder bleiben erhalten. Keine automatische Löschung; fehlende oder widersprüchliche Termine werden gemeldet. Ohne gespeicherte Google-ID keine automatische Übernahme.
5. Google-Ereignis-Zeitstempel werden zur Konflikterkennung gespeichert. Bei einem manuellen Speichern wird vor einer Google-Änderung geprüft, ob das verknüpfte Ereignis zwischenzeitlich auf Google verändert wurde.

**Einschränkungen:** Die Google-Verbindung nutzt Browser-OAuth und muss nach Ablauf erneuert werden. Kein Cloud-Backend und keine fortlaufende Synchronisierung bei geschlossenem Browser. Echte Firebase-/Google-Livetests konnten nicht durchgeführt werden. Die Firebase-Sicherheitsregeln bleiben unverändert; bestehende Sicherheitsaufgaben sind offen. Vor produktiver Nutzung sichern und auf einem Teststand prüfen.
