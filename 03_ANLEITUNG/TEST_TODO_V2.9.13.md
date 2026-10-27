# EC Wegscheid – V2.9.13 Test-To-do

**Basis:** V2.9.12 (noch nicht vollständig live getestet). **Neue private Testversion**, nicht ungeprüft auf produktive GitHub-Seite laden. Die V2.9.11 bleibt letzter vom Verein bestätigter stabiler Stand.

## Neu: Links unter „Startseite verwalten“
- [ ] Verwaltungsmenü öffnen: Bereich heißt **Startseite verwalten**.
- [ ] Unter „Verbände, Regelwerk und Sonstiges – Links verwalten“ sind die zehn bisherigen Links bereits vorhanden.
- [ ] Einen Link (z. B. „Kreis 107“) testweise in Name und Internetadresse ändern.
- [ ] „+ Link hinzufügen“ ausprobieren und eine gültige `https://`-Adresse eintragen.
- [ ] Pfeile ↑ / ↓ testen, dann testweise einen Link löschen (Sicherheitsabfrage).
- [ ] Änderungen erscheinen sofort unter Startseite → Links; unvollständige/unsichere Adressen werden nicht als anklickbare Links angezeigt.
- [ ] **„Startseite speichern“** oder **„Links und Startseite in Firebase speichern“** drücken; Bestätigung abwarten.
- [ ] Seite am PC neu laden und am Whiteboard öffnen: dieselben Links und Reihenfolge sichtbar.
- [ ] Prüfen, dass bestehende Startseitenbuttons, Texte, Hintergründe und Untermenüs unverändert sind.
- [ ] Teständerungen zurücksetzen oder ursprüngliche Links wiederherstellen und erneut speichern.

**Technik:** Die Linkliste wird in `appSettings/startseite` unter `config.links` mitgespeichert. Bestehende Konfigurationen ohne `links` erhalten die zehn bisherigen Links als Standard. Ein absichtlich gespeichertes leeres Array bleibt leer. Es werden keine neuen Firestore-Sammlungen oder -Regeln benötigt. HTTP/HTTPS erlaubt, JavaScript- oder Daten-URLs ausgeschlossen. Ein Browser- und Firebase-Echttest ist erforderlich.

## Aus V2.9.12 weiter zu prüfen
- [ ] „Termin- und Turnierplaner“ überall richtig bezeichnet.
- [ ] „Zurück zur Verwaltung“ nach Startseiten-Vorschau und Untermenüs sichtbar, Anmeldung erhalten.
- [ ] In „Vorhandene Veranstaltungen“ nur „Bearbeiten“ und „Löschen“; automatische Google-Aktualisierung weiter intakt.
- [ ] Google-Kalender-Client-ID eingerichtet; Programm → Google Kalender an einem Testtermin prüfen.
- [ ] Google → Programm: Änderungen an einem eindeutig verknüpften Testtermin abgleichen; keine Duplikate oder stillen Überschreibungen.

## Offene große To-do-Liste
- [ ] Punkt 43: sichere vollständige Firebase-Auth-Benutzerliste und Benutzeranlage mit Backend.
- [ ] Punkt 44: Firestore-/Storage-Sicherheitsregeln und Datenschutz umfassend prüfen.
- [ ] Sponsoren-Gmail-Versand mit PDF testen, wenn Sponsorendaten vorliegen.
- [ ] Dokumentenanzeige und Drucken über Windows-11-Mini-PC abschließen.
- [ ] Serienversand und weitere E-Mail-Funktionen abschließen.
- [ ] Optional: serverseitige Google-Kalender-Synchronisierung bei geschlossenem Browser.
