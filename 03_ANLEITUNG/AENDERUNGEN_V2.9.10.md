# V2.9.10 – Sammelkorrekturen

- Fotos Diashow und Fotos Sponsoren: redundante Ordner-Einstellungsfelder unter der Fotoliste entfernt; Einstellungen im oberen Formular; Buttons „Ordner bearbeiten“ und „Ordner löschen“ im Ordnerkopf.
- Vereinsnachrichten: Einzelnes Löschen erfolgt direkt in Firebase, mit vorheriger Sicherung, serverseitiger Prüfung und erst danach lokaler Entfernung/Erfolgsmeldung. Ablaufdatum blendet Nachrichten aus, ohne sie automatisch unwiederbringlich zu löschen.
- Benutzer und Rechte: Firestore-Profilliste mit Aktualisieren und geführter sicherer Neuanlage über Firebase Authentication-Konsole. Keine vollständige Auth-Liste und keine privilegierte Kontenerstellung allein über den Browser möglich.
- Geburtstage: unerwünschte Monatsauswahl entfernt; sechs Monate/Halbjahre erhalten.
- Mitglieder-Spalten: Nachname und Vorname separat auswählbar, ohne doppelte Spalten.
- Bekannte Sicherheitsprobleme der Firebase-Referenzregeln bleiben bestehen. Keine Firebase-Regeln verändert.
