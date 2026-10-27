# EC Wegscheid V2.9.11 – Sammeltest

Basis: V2.9.10. **Private Testversion, nicht ungeprüft in der produktiven Vereinsverwaltung veröffentlichen.**

## Änderungen

1. **Benutzer, Rechte und Datensicherung**: Umbenennung im Verwaltungsmenü. „Benutzerkennwort ändern“ und „Datensicherung“ sind dort jetzt als Unterfunktionen erreichbar. Die separaten Einträge im Verwaltungsmenü wurden entfernt. Kennwortänderung ist nur für berechtigte persönliche Konten möglich; Datensicherung nur für Administratoren.
2. **Benutzernamen**: In der Liste der verfügbaren Firestore-Benutzerprofile steht der Benutzername/Anzeigename explizit, außerdem E-Mail und Rolle. Die Details/Rechte können aufgeklappt werden. Falls Firestore die vollständige Abfrage verbietet, wird höchstens das eigene Profil angezeigt und eine Einschränkung erläutert. Die vollständige Firebase-Authentication-Kontenliste ist weiterhin ohne sicheren Serverdienst nicht abrufbar.
3. **Kommende Geburtstage**: Das angezeigte Alter wird aus dem Jahr des kommenden Geburtstags berechnet, einschließlich Jahreswechsel. Die Einteilung normal/rund nutzt dasselbe Jahr.
4. **Ergebnisprogramme**: Einbetten von Cup, Doppel-KO und anderen internen Ergebnisprogrammen merkt sich den Aufrufkontext. Der obere Rücksprung führt aus dem Adminbereich zur Verwaltung und von der Startseite zur Startseite. Der doppelte untere externe Hauptmenü-Button wurde entfernt. Die Cup-Hauptansicht blendet im eingebetteten Adminmodus einen unnötigen internen Startmenü-Button aus; Detail-Rücksprünge bleiben erhalten. Beim normalen Wechsel von Verwaltung zur Startseite bleibt die Firebase-Sitzung erhalten.
5. **Turnierwirtschaftlichkeit und Helfer**: Neuer Menüname und Titel.
6. **Jahresabrechnung**: Links Sponsoring-Übersicht mit drei **nicht addierten** Kennzahlen (Sponsoreinnahmen in Geld, alle erfassten Preiskosten des Jahres, noch verfügbares Sponsorgeld nach bisheriger Zuordnungslogik). Rechts die Jahresabrechnung: zuerst Startgeld-, Gastro-, Sponsoren- und weitere Turniereinnahmen, dann Preise, Gastro, weitere Turnierausgaben und weitere Jahresausgaben, darunter der Jahresgewinn. Eingabefeld „Weitere Jahresausgaben“ bleibt erhalten. Der Jahresgewinn berechnet sich aus Geldzuflüssen abzüglich tatsächlicher Kosten; Sachspenden werden nicht als Geldzufluss gebucht.

## Hinweise

- Bestehende Firebase-Daten und Sicherheitsregeln werden durch dieses ZIP nicht automatisch verändert.
- Die Testberechnung wurde mit synthetischen Daten überprüft (605 EUR Einnahmen, 185 EUR Ausgaben, 420 EUR Gewinn; 90 EUR gesamte Preiskosten, 170 EUR Sponsorrest bei 200 EUR Geldspenden und 30 EUR Zuordnungen).
- Echte Anmeldung, Firestore-Zugriffsrechte, Whiteboard-/43-Zoll-Darstellung und Datenabgleich sind **noch vor Ort zu testen**.
- Sponsor-Gmail-Versand bleibt auf der großen To-do-Liste, bis Sponsordaten vorliegen.
