from pathlib import Path
import json,hashlib,zipfile,re,shutil
root=Path('/mnt/data/dko_v26_build')
# UI menu addition on same level as Solo Pyramide and Interne Cup.
p=root/'index.html'; s=p.read_text()
anchor='      <div class="row" data-global-admin hidden style="margin-bottom:8px;gap:6px"><button style="flex:1" onclick="adminSection(\'solo\')">Solo Pyramide</button>'
assert anchor in s
row='      <div class="row" data-global-admin hidden style="margin-bottom:8px;gap:6px"><button style="flex:1" onclick="openInternalCupAdmin(\'doppelko\')">Doppel KO System</button><button style="flex:none;width:44px;padding:12px 0" title="Doppel KO öffnen" onclick="openInternalCupAdmin(\'doppelko\')">👁</button></div>\n'
s=s.replace(anchor,row+anchor,1);p.write_text(s)
# Name and cache busting of verified, separate JS, avoiding HTML parser regressions.
p=root/'doppel-ko.html';s=p.read_text().replace('Integrationstest V2.5','Integrationstest V2.6').replace('V2.5: JavaScript noch nicht gestartet','V2.6: JavaScript noch nicht gestartet').replace('doppel-ko-app-v25.js','doppel-ko-app-v26.js');p.write_text(s)
p=root/'doppel-ko-app-v25.js';s=p.read_text().replace('V2.5:','V2.6:').replace('DKO V2.5 Initialisierung','DKO V2.6 Initialisierung')
# Explicitly mark local/remote save states; do not claim cloud synchronization is active without auth.
s=s.replace("'WHITEBOARD</strong> · Rundenmodus · + / − und ✓ · nur lokal'", "'WHITEBOARD</strong> · Rundenmodus · + / − und ✓ · Firebase nach Anmeldung'")
# If a remote save failed and a user explicitly retries, keep the dirty flag; do not silently skip.
s=s.replace("$('cloudSave').onclick=()=>{if(!state.players.length){alert('Bitte zuerst ein Turnier erstellen.');return}scheduleCloudSave(true)};", "$('cloudSave').onclick=()=>{if(!state.players.length){alert('Bitte zuerst ein Turnier erstellen.');return}cloudDirty=true;scheduleCloudSave(true)};")
# Don't accidentally wipe a dirty unsaved tournament by pressing "new".
s=s.replace("$('cloudNew').onclick=()=>{$('clear').click();cloudStatus('Neues Turnier · Teilnehmer auswählen')};", "$('cloudNew').onclick=()=>{if(cloudDirty&&!confirm('Es gibt noch nicht in Firebase gespeicherte Änderungen. Trotzdem ein neues Turnier beginnen?'))return;$('clear').click();cloudStatus('Neues Turnier · Teilnehmer auswählen')};")
(root/'doppel-ko-app-v26.js').write_text(s)
p.unlink()
# Cache busting for parent turnierauswertung script and child page.
p=root/'js/auswertung-teil-06.js';s=p.read_text().replace('doppel-ko.html?v=2.4-neuer-test','doppel-ko.html?v=2.6-komplett');p.write_text(s)
p=root/'turnierauswertung.html';s=p.read_text().replace('js/auswertung-teil-06.js?v=2.4-dko-test','js/auswertung-teil-06.js?v=2.6-komplett');p.write_text(s)
# Change version metadata conservatively: main app stays V2.5.4, module V2.6.
p=root/'version.json';obj=json.loads(p.read_text());obj['release']='EC Wegscheid V2.5.4 + Doppel KO V2.6 – Integrationstest';obj['doppelKo']={'version':'2.6','status':'Integrationstest; Firebase erst nach Freigabe der Regeln und echtem Funktionstest','dateien':['doppel-ko.html','doppel-ko-app-v26.js']};obj.setdefault('changes',[]).append('Doppel KO V2.6: getrennte JS-Datei, Firebase-Turnierarchiv, Ergebnisspeicherung, vollständige Whiteboard-Bedienung, eigener Admin-Menübutton');p.write_text(json.dumps(obj,ensure_ascii=False,indent=2))
# Build consolidated Firestore rules in an OUTSIDE-of-GitHub folder, no automated publishing.
rules=(root/'FIRESTORE_REGELN_DOKUMENTE_V2.5.3.rules').read_text();anchor='    // ============================================================\n    // Alles andere standardmäßig sperren'
assert anchor in rules
addition='''    // Doppel KO – jeder Turnierstand als eigenständiges Dokument.\n    // Keine anonymen Lese-/Schreibrechte.\n    match /doppelKoTurniere/{turnierId} {\n      allow read: if isAdmin() || isWhiteboard() || canEdit('doppelKoEdit');\n      allow create: if (isAdmin() || isWhiteboard() || canEdit('doppelKoEdit'))\n        && request.resource.data.keys().hasOnly(['state','name','date','archived','revision','updatedAt','updatedBy'])\n        && request.resource.data.keys().hasAll(['state','name','date','archived','revision','updatedAt','updatedBy'])\n        && request.resource.data.state is map\n        && request.resource.data.name is string\n        && request.resource.data.date is string\n        && request.resource.data.archived is bool\n        && request.resource.data.revision == 1\n        && request.resource.data.updatedAt is string\n        && request.resource.data.updatedBy == request.auth.uid;\n      allow update: if (isAdmin() || isWhiteboard() || canEdit('doppelKoEdit'))\n        && request.resource.data.keys().hasOnly(['state','name','date','archived','revision','updatedAt','updatedBy'])\n        && request.resource.data.keys().hasAll(['state','name','date','archived','revision','updatedAt','updatedBy'])\n        && request.resource.data.state is map\n        && request.resource.data.name is string\n        && request.resource.data.date is string\n        && request.resource.data.archived is bool\n        && request.resource.data.revision == resource.data.revision + 1\n        && request.resource.data.updatedAt is string\n        && request.resource.data.updatedBy == request.auth.uid;\n      allow delete: if isAdmin() || isWhiteboard() || canEdit('doppelKoEdit');\n    }\n\n'''
rules=rules.replace(anchor,addition+anchor,1)
assert rules.count('match /doppelKoTurniere/{turnierId}')==1
external=Path('/mnt/data/dko_v26_release');external.mkdir(exist_ok=True)
(external/'FIRESTORE_REGELN_V2.5.4_MIT_DOPPEL_KO_V2.6_TEST.rules').write_text(rules)
# Avoid confusing old rules with consolidated rules inside GitHub package.
(root/'FIRESTORE_REGELN_DOKUMENTE_V2.5.3.rules').unlink()
(root/'FIRESTORE_REGELN_DOPPEL_KO_ERGAENZUNG.txt').unlink()
(root/'START_HIER_V2.5.txt').unlink()
(root/'DIREKTDRUCK_V2.5.4_TESTHINWEISE.txt').write_text('Vereinsverwaltung V2.5.4: Browserdruck kann nicht technisch auf ein Exemplar beschränkt werden. Drucksperre und Direktdruck am Samsung/HP weiterhin offen.\n')
# explanatory deployment guidance
readme='''EC WEGSCHEID – GESAMTPAKET V2.5.4 + DOPPEL KO V2.6 (TEST)\n\n1. Das ZIP enthält die gesamte Vereinsverwaltung, nicht nur Doppel KO.\n2. Inhalt des Ordners 01_GITHUB_UPLOAD/ (nicht den Ordner selbst) nach einem Backup ins GitHub-Repository hochladen.\n3. Für den ersten Test besser den kompletten Ordner 01_GITHUB_UPLOAD/ in VS Code / Live Server öffnen.\n4. In der Turnierauswertung: Doppel KO System; im Verwaltungsmenü eigener Button neben Interne Cup und Solo Pyramide.\n5. Die Spielerauswahl und die Touch-Ergebniseingabe stammen aus der zuletzt funktionierenden V2.5-Einzeltestversion.\n6. Firebase-Speicherung benötigt einen angemeldeten berechtigten Benutzer UND passende Firestore-Regeln.\n7. Die Regeln in 02_FIREBASE_REGELN/ sind eine konsolidierte TESTFASSUNG der bisher mitgelieferten Regeln. VOR dem Einspielen mit den aktuell veröffentlichten produktiven Regeln vergleichen, bestehende Rechte NICHT blind überschreiben.\n8. Bei jedem bestätigten Ergebnis versucht das Programm sofort zu speichern; Statusanzeige beachten. Bei 'Nur lokal' ist Firebase NICHT gesichert.\n9. Turniere können separat angelegt, fortgesetzt, archiviert und gelöscht werden. Firebase und Whiteboard wurden nicht live getestet.\n10. Wertungsblätter: je neu freigegebener Paarung ein einzelner Druckdialog; Browser können Folge-Dialoge blockieren. Kein unbeaufsichtigter Druck.\n11. Kein produktiver GitHub-Upload und keine Änderung an Firebase wurde durch die Erstellung vorgenommen.\n\nTests: JavaScript-Syntax, ZIP-Integrität, Menüs und Dateien statisch geprüft; Live-Firebase-/Samsung-/HP-Test steht aus.\n'''
(external/'START_HIER.txt').write_text(readme)
# Full zip with one GitHub upload folder and separately packaged rules.
out=Path('/mnt/data/EC_Wegscheid_V2.5.4_Doppel_KO_V2.6_KOMPLETTPAKET_TEST.zip')
with zipfile.ZipFile(out,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for file in sorted(root.rglob('*')):
  if file.is_file() and file.name!='build_v26.py':z.write(file,'01_GITHUB_UPLOAD/'+file.relative_to(root).as_posix())
 for file in sorted(external.iterdir()):
  if file.suffix=='.rules':z.write(file,'02_FIREBASE_REGELN/'+file.name)
  else:z.write(file,'03_ANLEITUNG/'+file.name)
print('created',out,out.stat().st_size)
