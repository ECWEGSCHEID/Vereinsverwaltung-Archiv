# EC Wegscheid – V2.9.14 Kalender-Konfliktlösung

**Basis V2.9.13**, Testversion.

- Kalenderfelder (Name, Datum, Uhrzeit, Ort) erhalten nach erfolgreichem Google-Abgleich einen eigenen gespeicherten Vergleichsstand (`googleSyncedFields`) im jeweiligen Firestore-Termin. Allgemeine `updatedAt`-Zeitstempel von Spieler-/Anmeldungsänderungen führen dadurch nicht mehr automatisch zu falschen Konflikten.
- Für bestehende Einträge ohne Vergleichsstand bleibt ein vorsichtiger Zeitstempel-Fallback. Bei Unsicherheit wird ein Konflikt zur Entscheidung angezeigt, nicht stillschweigend überschrieben.
- Im Bereich **Kalendereinstellungen** werden Konflikte unter dem Abgleichstatus mit **Google übernehmen**, **Programm übernehmen** und **Abbrechen** angezeigt. Die Auswahl gilt für den jeweiligen eindeutig verknüpften Google-Termin.
- Vor jeder Entscheidung werden aktuelle Google- und Firestore-Daten erneut geprüft. Google-Übernahme aktualisiert nur Name/Datum/Uhrzeit/Ort und den Synchronisierungsstand; Spieler, Turnierart und andere Felder bleiben bestehen. Programm-Übernahme aktualisiert per PATCH den bestehenden Google-Eintrag und legt keinen neuen an.
- Google-Änderungen werden nur für verknüpfte Termine übernommen. Keine automatische Löschung, kein Import unbekannter Termine und kein Hintergrunddienst bei geschlossenem Browser.
- Funktionierende Programm→Google-Übertragung und die neue Linkverwaltung V2.9.13 bleiben erhalten.

**Sicherheits- und Testhinweis:** Der Code wurde syntaktisch und mit simulierten Fällen geprüft. Ein Live-Test mit dem Vereins-Google-Kalender und Firebase ist erforderlich. Firebase-Regeln unverändert.
