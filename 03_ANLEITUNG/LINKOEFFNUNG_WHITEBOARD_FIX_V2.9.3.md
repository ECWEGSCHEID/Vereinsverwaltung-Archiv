# V2.9.3 – Linköffnung am Samsung-Whiteboard (Testversion)

## Fehler in V2.9.2

- Angemeldete Whiteboard-Benutzer wurden bei externen Links pauschal auf `_blank` gesetzt, auch wenn die zentrale Linkeinstellung **Eingebettet** vorsah.
- Im öffentlichen Whiteboard-Modus öffnete `location.href` nicht ein neues Fenster, sondern ersetzte die EC-Wegscheid-Vereinsverwaltung im aktuellen Tab.
- Bei blockierter Einbettung war der Link **In neuem Tab öffnen** am Whiteboard versteckt.

## Korrektur

- Startseiten-Links und die feste Links-Übersicht beachten nun für alle Benutzer die Einstellung **Eingebettet** / **In neuem Tab**.
- Nicht einbettbare Links wie die Google-Startseite öffnen über einen normalen Link mit `target=_blank`, ohne die Vereinsverwaltung absichtlich zu verlassen.
- Bei Einbettung steht **In neuem Tab öffnen** auch auf dem Whiteboard als Ausweichmöglichkeit zur Verfügung.
- Cup, Doppel-KO, Solo-Pyramide, Jahresmeisterschaft und deren Firebase-Sitzungsübergabe aus V2.9.2 wurden nicht geändert. Stockdart bleibt gesperrt.
- Keine Firebase-Regeländerung und keine Datenänderung.

## Test am Samsung

1. Nur in separater GitHub-Testumgebung bereitstellen, nicht die produktive Seite überschreiben.
2. Als Informationssystem anmelden. Einen Link mit Einstellung **Eingebettet** öffnen; die Seite soll im internen Anzeigebereich erscheinen, sofern sie Einbettung erlaubt.
3. Google oder einen Link mit Einstellung **In neuem Tab** öffnen: Das Samsung-Gerät soll eine neue Registerkarte/ein neues Fenster öffnen, die Vereinsverwaltung darf nicht absichtlich durch `location.href` ersetzt werden.
4. Zur Vereinsverwaltung zurückkehren und Ergebnisprogramme erneut öffnen (Sitzungstest).
5. Wenn der Samsung-Browser Pop-ups/neue Tabs blockiert oder nicht sichtbar macht, muss die Browsereinstellung am Gerät separat geprüft werden.

## Grenzen

Fremde Webseiten können die Einbettung per `X-Frame-Options` oder CSP `frame-ancestors` verbieten. Das lässt sich nicht mit unserem HTML-Code aufheben. Ein Browser kann trotz `target=_blank` neue Tabs unterdrücken oder anders anzeigen. Die tatsächliche Funktion am Samsung ist noch nicht verifiziert. Bekannte Firebase-Sicherheitsrisiken bleiben offen.
