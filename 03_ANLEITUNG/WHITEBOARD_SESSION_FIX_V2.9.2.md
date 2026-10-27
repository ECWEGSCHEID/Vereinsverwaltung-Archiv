# EC Wegscheid V2.9.2 – Whiteboard-Sitzung: Testversion

## Korrektur

- Turnierauswertung (Cup, Doppel-KO und Ziel): übernimmt bei eingebettetem Start eine **zuvor in Firestore geprüfte** Whiteboard-Firebase-Sitzung des Elternfensters, statt im Unterprogramm eine zweite Firebase-Anmeldung zu verlangen.
- Doppel-KO verwendet die bereits angemeldete Firebase-Compat-Verbindung der Hauptverwaltung. Die Whiteboard-Rolle bleibt **whiteboard**, nicht **admin**.
- Solo-Pyramide: der Start setzt `mode=whiteboard` nur für eine geprüfte Whiteboard-Sitzung. Bei Administratoren erfolgt `mode=admin-embedded`. Eine irreführende separate Informationssystem-Passwortabfrage wird nicht mehr angeboten.
- Erkennung lokaler Dateien auch auf separaten Test-GitHub-Repositories.
- Stockdart bleibt **nicht** für Whiteboard freigegeben.

## Test (nur Test-Repository)

1. V2.9.2 separat bereitstellen. Nicht den laufenden produktiven Stand ersetzen.
2. Am Samsung als Informationssystem anmelden.
3. Cup-Ergebnisse öffnen, schließen und wieder öffnen (3×). Keine erneute Anmeldung.
4. Doppel-KO öffnen, schließen und wieder öffnen (3×). Daten laden und speichern nur mit vorhandenen Testdaten prüfen.
5. Solo-Pyramide öffnen, schließen und wieder öffnen (3×). Keine separate Passwortabfrage.
6. Ziel-Jahresmeisterschaft erneut testen. Stockdart muss gesperrt bleiben.
7. Browser neu starten und Whiteboard komplett neu starten; prüfen, ob die Firebase-Sitzung erhalten bleibt.

## Einschränkungen

- Browser-/Firebase-Live-Test am Samsung ist noch nicht erfolgt. Diese Version ist **nicht produktionsfreigegeben**.
- Aktive Firebase-Regeln wurden nicht geändert oder mit dem Live-Projekt verglichen. Die bekannten Sicherheitsprobleme aus dem V2.8.7-Prüfbericht bleiben bestehen.
- Ein Firebase-Benutzerprofil muss in `users/{uid}` wirklich als Whiteboard berechtigt sein (`whiteboard: true` oder `role: whiteboard`, ggf. unterstütztes Legacy-Profil). Ein Benutzer mit fehlenden Rechten wird **nicht** durch einen URL-Parameter freigeschaltet.
- Ohne bestehende gültige Firebase-Sitzung kann keine automatische Anmeldung erfolgen.
