# Testkorrektur V2.8.8 – Whiteboard-Ergebnisse

Ausgangsbasis: Gesamtpaket V2.8.7. Die Version V2.8.8 bezeichnet ausschließlich diesen Test-Hotfix.

## Korrekturen
- `js/auswertung-teil-01.js`: Die eigenständige Turnierauswertung erkennt das eingeschränkte Firebase-Whiteboard-Profil (`whiteboard: true`) und historische kompatible Profile, statt alle Nicht-Admins als `user` abzulehnen.
- `js/hauptprogramm.js`: Stockdart bleibt für das Whiteboard fest gesperrt. Der irreführende Whiteboard-Freigabe-Schalter wird entfernt.
- Keine Firebase-Regeln, Zugangsdaten oder Daten wurden geändert.

## Prüfschritte (zuerst Testumgebung!)
1. Bestehende GitHub-Dateien sichern; Änderungen zunächst in einem Test-Repository/Testzweig ausprobieren.
2. Nach Upload das Whiteboard vollständig neu laden (ggf. Browser-Cache leeren).
3. Am Whiteboard Cupauswertung, Jahresmeisterschaft Ziel, Turnierauslosung, Doppel-KO und Solo-Pyramide jeweils öffnen.
4. Stockdart muss gesperrt bleiben.
5. Als Administrator prüfen, dass Stockdart weiterhin funktioniert.
6. Whiteboard ausschalten/einschalten: automatische Vollbild-Startseite ohne erneute Anmeldung kontrollieren.
7. Falls der Whiteboard-Zugang weiterhin gesperrt ist: unter Firebase Authentication/Firestore prüfen, ob das Whiteboard mit seinem eigenen Konto angemeldet ist und im Dokument `users/{UID}` das Feld `whiteboard: true` gesetzt ist. Nicht einfach öffentliche Leserechte erweitern.

**Grenzen:** Statische Syntax und Rollenlogik wurden lokal getestet. Kein Live-Test mit Firebase/Samsung WM65B. Die bereits im vorherigen Prüfbericht genannten Firebase-Sicherheitsrisiken sind weiterhin offen. Daher nicht als sicherheitsgeprüfte Produktionsfreigabe verstehen.
