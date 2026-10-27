# V2.9.9 – Sammeltest Mitgliederverwaltung

Ausgangsbasis: vollständiges Paket V2.9.8.

1. Aufnahmeantrag: dynamisch erzeugtes A4-PDF aus der vom Benutzer bereitgestellten Originalvorlage; Beitrag aus `S.settings.fee`, aktualisierte Vorschau und Download. Für die dynamische Druckfassung wird die Originalvorlage mit 3x Rasterauflösung wiedergegeben; die unveränderte Original-PDF bleibt im Assets-Verzeichnis.
2. Firebase-Status: nicht mehr fixiert über Bedienelementen.
3. Sponsoren: Gmail-OAuth-Einzelversand mit derselben lokal gespeicherten OAuth-Client-ID wie in der Turnierverwaltung; Text/PDF-Anhang, explizite Versandbestätigung. Ein separater OAuth-Token pro Sitzung wird benötigt. Keine E-Mail wird ohne Nutzerbestätigung gesendet.
4. Benutzer & Rechte: ältere, irreführende lokale Benutzer-/Kennwort-Eingabemaske durch Verweis auf zentrale Firebase-Benutzerverwaltung ersetzt. Alte Daten nicht gelöscht, keine automatische Migration von Firebase-Auth-Konten.
5. Runde Geburtstage: zusätzliche Filter für nächste sechs Monate, beide Halbjahre und Einzelmonat; sechs Monate können über den Jahreswechsel reichen.
6. Anzeige: zusätzliche Datenfelder und spaltenweise Sichtbarkeit/Sortierung; sensible Bankfelder rollenabhängig.
7. Serienbrief: Dokumentauswahl und Vorschau zurücksetzen, einschließlich Schutz vor veralteten asynchronen Vorschauen.

**Nicht geändert:** Firebase-Regeln, produktive Firebase-Daten, Whiteboard-Sitzungslogik, übrige Verwaltungsmenüs. Es wurden keine echten E-Mails versandt.

**Offen:** Gmail-Liveversand und Samsung-Browser-Verhalten sind nur am echten Gerät und mit berechtigtem Google-Konto prüfbar. Sicherheitsbefunde der vorherigen Versionen bestehen fort. Keine Freigabe für ungetesteten Produktiveinsatz.
