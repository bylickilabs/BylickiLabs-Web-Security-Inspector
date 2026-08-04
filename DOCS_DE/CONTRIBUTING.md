# Beitragsrichtlinien

## BylickiLabs Web Security Inspector

**Version:** 1.0  
**Gültig ab:** 4. August 2026  
**Projekt:** BylickiLabs Web Security Inspector 2.0.0  
**Verantwortlich:** Thorsten Bylicki | BylickiLabs  

---

## 1. Zweck dieser Beitragsrichtlinien

Diese Beitragsrichtlinien beschreiben, wie Fehlerberichte, Verbesserungsvorschläge, Quellcodeänderungen, Dokumentationsanpassungen, Tests und sicherheitsrelevante Beiträge zum BylickiLabs Web Security Inspector eingereicht werden können.

Ziel ist ein klarer, professioneller und nachvollziehbarer Entwicklungsprozess.

Beiträge sollen:

- technisch begründet sein
- zum Projektumfang passen
- nachvollziehbar dokumentiert werden
- bestehende Funktionen nicht unnötig beeinträchtigen
- die Sicherheit und Stabilität der Anwendung berücksichtigen
- die zweisprachige Struktur des Projekts respektieren
- den bestehenden Code- und Qualitätsstandards entsprechen

Die Einreichung eines Beitrags begründet keinen Anspruch auf Annahme, Veröffentlichung, Vergütung, Namensnennung oder dauerhafte Aufnahme in das Projekt.

---

## 2. Projektübersicht

Der BylickiLabs Web Security Inspector ist eine professionelle Desktop-Anwendung zur strukturierten Analyse von Websites, Domains und webbasierten Diensten.

Die Anwendung umfasst unter anderem:

- HTTP- und TLS-Analysen
- DNS- und Mail-Sicherheitsprüfungen
- Sicherheitsheader
- Cookie- und CORS-Analysen
- Formular- und Inhaltsprüfungen
- Performance-Messungen
- Risiko- und Befundbewertung
- Statistiken mit NumPy und SciPy
- Diagramme mit Matplotlib
- lokale Speicherung mit SQLite
- Exporte in JSON, HTML, CSV, PDF und SARIF
- deutsch- und englischsprachige Benutzeroberflächen
- automatisierte Build- und Qualitätssicherungsprozesse

Beiträge müssen sich inhaltlich in diesen Projektkontext einfügen.

---

## 3. Voraussetzungen für Beiträge

Vor dem Einreichen eines Beitrags sollten folgende Voraussetzungen erfüllt sein:

- aktueller Stand des Repositorys wurde geladen
- bestehende Issues und Pull Requests wurden geprüft
- die Änderung wurde lokal getestet
- bestehende Funktionen wurden nicht unbeabsichtigt verändert
- neue Abhängigkeiten wurden begründet
- Sicherheitsauswirkungen wurden berücksichtigt
- deutsche und englische Texte wurden synchron gehalten
- Code wurde formatiert und geprüft
- relevante Tests wurden ausgeführt
- Dokumentation wurde bei Bedarf angepasst

Beiträge ohne nachvollziehbare Beschreibung oder ohne ausreichende Prüfung können abgelehnt oder geschlossen werden.

---

## 4. Verhaltenskodex

Alle Mitwirkenden müssen den im Repository veröffentlichten Verhaltenskodex einhalten.

Erwartet werden insbesondere:

- respektvolle Kommunikation
- sachliche technische Diskussion
- konstruktive Kritik
- verantwortungsvoller Umgang mit Sicherheitsinformationen
- keine persönlichen Angriffe
- keine diskriminierenden oder abwertenden Inhalte
- keine Veröffentlichung vertraulicher Daten
- keine missbräuchliche Nutzung des Projekts

Verstöße können zur Schließung von Issues oder Pull Requests sowie zum Ausschluss von der weiteren Mitwirkung führen.

---

## 5. Arten von Beiträgen

Willkommen sind insbesondere:

- Fehlerberichte
- Korrekturen reproduzierbarer Fehler
- Performance-Verbesserungen
- Optimierungen der Datenbank
- Verbesserungen der Benutzeroberfläche
- Erweiterungen bestehender Scanner-Module
- neue nicht destruktive Prüfmodule
- Verbesserungen der Risikobewertung
- Statistik- und Diagrammverbesserungen
- zusätzliche Tests
- Verbesserungen der Barrierefreiheit
- Übersetzungsverbesserungen
- Dokumentationskorrekturen
- Build- und Release-Verbesserungen
- Sicherheitskorrekturen
- Verbesserungen der Fehlerbehandlung
- Optimierungen der Exportfunktionen

Nicht jeder Vorschlag wird umgesetzt. Änderungen müssen mit Architektur, Projektzielen und Sicherheitsanforderungen vereinbar sein.

---

## 6. Nicht erwünschte Beiträge

Nicht erwünscht sind insbesondere:

- unbefugte Angriffs- oder Exploit-Funktionen
- Passwortangriffe
- Credential Stuffing
- Brute-Force-Mechanismen
- destruktive Nutzlasten
- Schadsoftware
- Ransomware-Funktionen
- Funktionen zur Umgehung von Zugriffskontrollen
- automatisierte Ausnutzung fremder Systeme
- unkontrolliertes Scannen großer Zielbereiche
- versteckte Telemetrie
- Tracking ohne ausdrückliche Zustimmung
- Sammlung personenbezogener Daten
- ungeprüfte KI-generierte Massenänderungen
- nicht dokumentierte Abhängigkeiten
- kopierter Code ohne passende Lizenz
- Änderungen ohne Bezug zum Projekt
- absichtliche Schwächung vorhandener Sicherheitsmechanismen
- Entfernung von Prüfungen ohne nachvollziehbare Begründung
- Umgehung der Zielvalidierung
- Änderungen, die vertrauliche Daten offenlegen könnten

Beiträge mit missbräuchlichem oder rechtswidrigem Schwerpunkt werden nicht akzeptiert.

---

## 7. Entwicklungsumgebung

### Systemanforderungen

Empfohlen werden:

- Windows 10 oder Windows 11
- Python 3.11 oder neuer
- Git
- mindestens 4 GB Arbeitsspeicher
- Internetzugang für Abhängigkeiten und externe APIs

### Repository klonen

```bash
git clone https://github.com/bylickilabs/BylickiLabs-Web-Security-Inspector.git
cd BylickiLabs-Web-Security-Inspector
```

### Virtuelle Umgebung erstellen

```powershell
py -3 -m venv .venv
```

### Entwicklungsabhängigkeiten installieren

```bat
scripts\setup_dev.cmd
```

Alternativ:

```powershell
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
```

### Anwendung starten

```bat
START.bat
```

Alternativ:

```powershell
.\.venv\Scripts\python.exe main.py
```

---

## 8. Branch-Strategie

Änderungen dürfen nicht direkt auf dem Hauptbranch entwickelt werden.

Für jeden Beitrag ist ein eigener Branch zu erstellen.

Empfohlene Namenskonventionen:

```text
feature/kurze-beschreibung
fix/kurze-beschreibung
security/kurze-beschreibung
docs/kurze-beschreibung
refactor/kurze-beschreibung
test/kurze-beschreibung
build/kurze-beschreibung
performance/kurze-beschreibung
```

Beispiele:

```text
feature/add-certificate-analysis
fix/sqlite-history-loading
performance/optimize-statistics
docs/update-installation
security/harden-url-validation
```

Branch-Namen sollen:

- kleingeschrieben sein
- Bindestriche verwenden
- kurz und eindeutig sein
- keine Sonderzeichen enthalten
- den Zweck der Änderung erkennen lassen

---

## 9. Commit-Richtlinien

Commits sollen klein, nachvollziehbar und thematisch eindeutig sein.

Empfohlene Präfixe:

```text
feat:
fix:
security:
docs:
refactor:
test:
build:
ci:
perf:
style:
chore:
```

Beispiele:

```text
feat: add extended TLS certificate analysis
fix: prevent duplicate scan history entries
security: harden target URL validation
docs: update Windows build instructions
perf: optimize SQLite history queries
test: add statistics regression tests
```

Commit-Nachrichten sollen:

- im Imperativ formuliert sein
- den tatsächlichen Inhalt beschreiben
- keine allgemeinen Aussagen wie „Update“ enthalten
- nicht mehrere unabhängige Änderungen zusammenfassen
- keine vertraulichen Informationen enthalten
- keine Zugangsdaten oder API-Schlüssel enthalten

Ungeeignete Beispiele:

```text
update
changes
fixed stuff
new version
test
work
```

---

## 10. Code-Standards

Beiträge müssen dem bestehenden Python-Stil des Projekts entsprechen.

### Allgemeine Anforderungen

- Python 3.11 oder neuer
- lesbare und eindeutige Bezeichner
- klare Trennung von Benutzeroberfläche, Logik und Datenzugriff
- Typannotationen, soweit sinnvoll
- nachvollziehbare Fehlerbehandlung
- keine unnötigen globalen Zustände
- keine hartcodierten Zugangsdaten
- keine unnötigen Seiteneffekte beim Import
- keine unkontrollierten Netzwerkaufrufe
- keine blockierenden Operationen im UI-Thread
- keine unverschlüsselten sensiblen Werte im Quellcode
- keine unnötigen Abhängigkeiten
- keine versteckten Hintergrundprozesse

### Dokumentation im Code

Neue öffentliche Klassen, Funktionen und Module sollten verständliche Docstrings enthalten.

Docstrings sollen erläutern:

- Zweck
- Parameter
- Rückgabewerte
- mögliche Ausnahmen
- sicherheitsrelevante Einschränkungen
- Seiteneffekte

Kommentare sollen erklären, warum eine Lösung notwendig ist, nicht lediglich wiederholen, was der Code tut.

---

## 11. Architekturprinzipien

Beiträge müssen die modulare Architektur des Projekts respektieren.

Die zentralen Bereiche sind:

```text
app/core
app/scanners
app/reporting
app/ui
app/models.py
app/config.py
app/i18n.py
tests
```

### Scanner-Module

Neue Prüfungen sollen nach Möglichkeit als eigenständiges Modul unter `app/scanners` umgesetzt werden.

Ein Scanner-Modul sollte:

- einen klar abgegrenzten Prüfzweck besitzen
- definierte Eingaben akzeptieren
- einheitliche Befundmodelle zurückgeben
- Zeitlimits beachten
- Fehler kontrolliert behandeln
- keine unkontrollierten Seiteneffekte erzeugen
- keine destruktiven Änderungen am Zielsystem durchführen
- Ergebnisse nachvollziehbar dokumentieren
- in den zentralen Scanner integriert werden
- durch automatisierte Tests abgedeckt werden

### Benutzeroberfläche

UI-Code soll:

- nicht unnötig mit Scanner-Logik vermischt werden
- auf lange blockierende Vorgänge verzichten
- konsistente Bezeichnungen verwenden
- deutsche und englische Texte unterstützen
- bestehende Layout- und Stilregeln respektieren
- Fehler verständlich darstellen
- sensible Daten nicht unnötig anzeigen

### Datenbank

Änderungen an der SQLite-Datenbank müssen:

- Rückwärtskompatibilität prüfen
- Migrationen berücksichtigen
- Transaktionen korrekt verwenden
- Eingaben parametrisiert verarbeiten
- Fehlerfälle abdecken
- bestehende Daten nicht unbeabsichtigt löschen
- durch Tests abgesichert sein

---

## 12. Internationalisierung

Die Anwendung ist vollständig zweisprachig.

Neue sichtbare Texte müssen daher in Deutsch und Englisch bereitgestellt werden.

Dazu gehören:

- Schaltflächen
- Menüs
- Dialoge
- Fehlermeldungen
- Statusmeldungen
- Tooltips
- Tabellenüberschriften
- Befundtexte
- Einstellungen
- Berichtsbezeichnungen

Es darf keine neue Funktion eingereicht werden, die nur in einer Sprache vollständig nutzbar ist.

Übersetzungen sollen fachlich korrekt, konsistent und sinngleich sein.

Automatische Übersetzungen müssen vor der Einreichung manuell geprüft werden.

---

## 13. Tests

Neue Funktionen und Fehlerkorrekturen sollen durch automatisierte Tests abgesichert werden.

Mindestens geprüft werden sollten:

- erwartetes Standardverhalten
- relevante Grenzfälle
- ungültige Eingaben
- Netzwerkfehler
- Zeitüberschreitungen
- Datenbankfehler
- leere Ergebnisse
- fehlerhafte externe Antworten
- sichere Verarbeitung dynamischer Inhalte
- bestehende Rückwärtskompatibilität

### Tests ausführen

```powershell
.\.venv\Scripts\python.exe -m pytest
```

### Vollständige Qualitätsprüfung

```bat
scripts\quality.cmd
```

Die vollständige Qualitätsprüfung umfasst:

- Python-Syntaxprüfung
- Kompilierung
- Ruff
- pytest
- zentrale Modelltests
- Scanner-Tests
- Datenbanktests
- Statistiktests
- Exporttests
- Eingabevalidierung

Ein Pull Request sollte keine bekannten fehlgeschlagenen Tests enthalten.

---

## 14. Codeanalyse mit Ruff

Vor dem Einreichen eines Pull Requests ist Ruff auszuführen:

```powershell
.\.venv\Scripts\python.exe -m ruff check app tests main.py
```

Automatisch korrigierbare Probleme können mit folgendem Befehl bearbeitet werden:

```powershell
.\.venv\Scripts\python.exe -m ruff check --fix app tests main.py
```

Automatische Korrekturen müssen anschließend manuell geprüft werden.

---

## 15. Statistische Änderungen

Änderungen an NumPy-, SciPy- oder Matplotlib-Komponenten müssen besonders sorgfältig geprüft werden.

Erforderlich sind:

- nachvollziehbare mathematische Begründung
- klare Datengrundlage
- definierte Behandlung leerer Datenreihen
- Behandlung von NaN- und Unendlichkeitswerten
- stabile Ergebnisse bei kleinen Stichproben
- keine irreführenden Diagramme
- passende Achsen und Beschriftungen
- reproduzierbare Tests
- Dokumentation neuer Kennzahlen

Statistische Werte dürfen nicht ohne fachliche Begründung in den Risikoscore einfließen.

---

## 16. Risikomodell

Änderungen am Risikomodell müssen dokumentiert und durch Tests abgesichert werden.

Ein Vorschlag muss erläutern:

- welche Gewichtung geändert wird
- warum die Änderung erforderlich ist
- welche Befunde betroffen sind
- wie sich bestehende Scans verändern
- ob historische Vergleiche beeinflusst werden
- welche Grenzwerte gelten
- wie Fehlalarme reduziert werden
- welche Sicherheitsauswirkungen bestehen

Unbegründete Score-Anpassungen werden nicht akzeptiert.

---

## 17. Exportfunktionen

Änderungen an JSON-, HTML-, CSV-, PDF- oder SARIF-Exporten müssen sicherstellen, dass:

- Sonderzeichen korrekt verarbeitet werden
- dynamische Inhalte sicher maskiert werden
- keine Code-Injection entsteht
- keine internen Daten unbeabsichtigt veröffentlicht werden
- bestehende Felder möglichst kompatibel bleiben
- Dateipfade sicher behandelt werden
- Exporte nicht außerhalb vorgesehener Verzeichnisse schreiben
- Berichte vollständig und lesbar bleiben
- neue Felder dokumentiert werden
- Tests für die Ausgabe vorhanden sind

HTML-Berichte dürfen keine ungeprüften aktiven Inhalte aus Zielsystemen übernehmen.

---

## 18. Neue Abhängigkeiten

Neue Abhängigkeiten müssen vor ihrer Einführung begründet werden.

Die Begründung soll enthalten:

- Zweck der Bibliothek
- warum vorhandene Komponenten nicht ausreichen
- Lizenz
- Wartungsstatus
- Sicherheitsstatus
- Größe und Build-Auswirkung
- Windows-Kompatibilität
- Einfluss auf PyInstaller
- mögliche Alternativen
- erforderliche Änderungen an Abhängigkeitsdateien

Abhängigkeiten ohne klaren Mehrwert können abgelehnt werden.

Nicht gepflegte, unsichere oder lizenzrechtlich ungeeignete Bibliotheken werden nicht aufgenommen.

---

## 19. Build und PyInstaller

Änderungen am Windows-Build müssen mit der vorhandenen PyInstaller-Konfiguration kompatibel sein.

Vor einem Pull Request sollte geprüft werden:

```bat
scripts\build_exe.cmd
```

Der Build muss:

- ohne manuelle Nachbearbeitung funktionieren
- erforderliche Ressourcen enthalten
- keine sensiblen Dateien bündeln
- die korrekte Version anzeigen
- ohne separate Python-Installation starten
- keine unnötigen Entwicklungsdateien enthalten
- nachvollziehbar reproduzierbar sein

Änderungen an der `.spec`-Datei müssen begründet werden.

---

## 20. Dokumentation

Änderungen an Funktionen, Installation, Konfiguration, Build, Exporten oder Benutzeroberfläche müssen in der Hauptdokumentation berücksichtigt werden.

Dokumentation soll:

- technisch korrekt sein
- mit dem tatsächlichen Funktionsumfang übereinstimmen
- keine nicht vorhandenen Funktionen versprechen
- nachvollziehbare Beispiele enthalten
- Befehle exakt wiedergeben
- Deutsch und Englisch berücksichtigen
- keine vertraulichen Daten enthalten
- keine veralteten Screenshots oder Pfade verwenden

Reine Codeänderungen ohne notwendige Dokumentationsanpassung können als unvollständig bewertet werden.

---

## 21. Issues erstellen

Vor dem Erstellen eines Issues ist zu prüfen:

- ob bereits ein ähnliches Issue existiert
- ob das Problem in der aktuellen Version besteht
- ob die Ursache in einer Drittanbieterkomponente liegt
- ob das Problem reproduzierbar ist
- ob vertrauliche Sicherheitsinformationen enthalten sind

Ein gutes Issue enthält:

- aussagekräftigen Titel
- betroffene Version
- Betriebssystem
- Python-Version
- Installationsart
- klare Problembeschreibung
- Reproduktionsschritte
- erwartetes Verhalten
- tatsächliches Verhalten
- relevante Fehlermeldungen
- bereinigte Protokolle
- Screenshots, sofern hilfreich
- mögliche Ursache
- mögliche Lösung

Issues ohne ausreichende Angaben können mit einer Rückfrage versehen oder geschlossen werden.

---

## 22. Funktionsvorschläge

Funktionsvorschläge sollten erläutern:

- welches Problem gelöst werden soll
- welche Anwender betroffen sind
- wie die Funktion in die bestehende Anwendung passt
- welche Oberfläche betroffen ist
- welche Sicherheitsauswirkungen bestehen
- welche Daten verarbeitet werden
- welche Abhängigkeiten erforderlich sind
- welche Alternativen geprüft wurden
- wie die Funktion getestet werden kann

Ein Funktionsvorschlag ist keine Zusage zur Umsetzung.

---

## 23. Pull Requests

Ein Pull Request muss:

- einen klaren Titel besitzen
- auf ein bestehendes Issue verweisen, sofern vorhanden
- den Zweck der Änderung beschreiben
- technische Entscheidungen erläutern
- Auswirkungen auf Sicherheit und Kompatibilität nennen
- durchgeführte Tests auflisten
- relevante Screenshots enthalten, wenn die Oberfläche geändert wurde
- Dokumentationsänderungen enthalten, wenn erforderlich
- frei von Zugangsdaten und sensiblen Daten sein
- einen überschaubaren Umfang besitzen

Große Änderungen sollten vorab als Issue diskutiert werden.

Mehrere unabhängige Änderungen gehören in getrennte Pull Requests.

---

## 24. Pull-Request-Checkliste

Vor dem Einreichen sollte bestätigt werden:

- [ ] Der Beitrag passt zum Projektumfang.
- [ ] Es wurde ein eigener Branch verwendet.
- [ ] Der Code wurde lokal ausgeführt.
- [ ] Alle relevanten Tests wurden ausgeführt.
- [ ] Ruff meldet keine ungeklärten Fehler.
- [ ] Die Anwendung startet weiterhin.
- [ ] Die Benutzeroberfläche bleibt funktionsfähig.
- [ ] Deutsch und Englisch wurden berücksichtigt.
- [ ] Neue Abhängigkeiten wurden begründet.
- [ ] Sicherheitsauswirkungen wurden geprüft.
- [ ] Datenbankänderungen wurden getestet.
- [ ] Exportfunktionen wurden getestet.
- [ ] Dokumentation wurde aktualisiert.
- [ ] Es wurden keine Zugangsdaten eingecheckt.
- [ ] Es wurden keine fremden Inhalte ohne Lizenz übernommen.
- [ ] Der Pull Request enthält keine vertraulichen Schwachstellendetails.

---

## 25. Review-Prozess

Pull Requests können geprüft werden auf:

- technische Richtigkeit
- Sicherheitsauswirkungen
- Architekturkonformität
- Codequalität
- Testabdeckung
- Performance
- Benutzerfreundlichkeit
- Übersetzungsqualität
- Datenbankkompatibilität
- Build-Kompatibilität
- Dokumentation
- Lizenzkonformität
- Wartbarkeit

Es können Änderungen angefordert werden.

Ein Pull Request kann abgelehnt werden, wenn:

- er nicht zum Projekt passt
- Sicherheitsrisiken bestehen
- Tests fehlen
- die Änderung nicht nachvollziehbar ist
- bestehende Funktionen unnötig beeinträchtigt werden
- Abhängigkeiten nicht akzeptabel sind
- Lizenzprobleme bestehen
- die Wartung unverhältnismäßig aufwendig wäre
- die Änderung den Projektzielen widerspricht

---

## 26. Merge-Entscheidung

Die endgültige Entscheidung über Annahme, Änderung, Verschiebung oder Ablehnung eines Beitrags liegt beim Projektverantwortlichen.

Ein erfolgreicher Review garantiert keinen Merge.

Beiträge können zurückgestellt werden, wenn:

- ein Release bevorsteht
- Architekturänderungen geplant sind
- weitere Tests erforderlich sind
- externe Abhängigkeiten ungeklärt sind
- Sicherheitsfragen offen sind
- Prioritäten geändert wurden

---

## 27. Sicherheitslücken

Sicherheitslücken dürfen nicht als öffentliches Issue oder Pull Request eingereicht werden.

Sie müssen vertraulich über die auf dem GitHub-Profil von BylickiLabs hinterlegte Kontaktmöglichkeit gemeldet werden.

**GitHub-Profil:**

```text
https://github.com/bylickilabs
```

**Projekt-Repository:**

```text
https://github.com/bylickilabs/BylickiLabs-Web-Security-Inspector
```

Eine Sicherheitsmeldung sollte enthalten:

- betroffene Version
- betroffene Komponente
- technische Beschreibung
- Reproduktionsschritte
- mögliche Auswirkungen
- nicht destruktiven Proof of Concept
- vorgeschlagene Schutzmaßnahme
- bevorzugten Kontaktweg

Öffentliche Exploits, Zugangsdaten oder vertrauliche Scan-Ergebnisse dürfen nicht veröffentlicht werden.

---

## 28. Datenschutz

Beiträge dürfen keine personenbezogenen oder vertraulichen Daten enthalten.

Vor der Veröffentlichung müssen insbesondere entfernt werden:

- Namen unbeteiligter Personen
- E-Mail-Adressen
- Zugangsdaten
- API-Schlüssel
- private Schlüssel
- interne Hostnamen
- interne IP-Adressen
- lokale Benutzerpfade
- vertrauliche Zieladressen
- vollständige Antwortinhalte
- nicht öffentliche Scan-Ergebnisse

Screenshots und Protokolle müssen vor dem Hochladen geprüft und bereinigt werden.

---

## 29. Geistiges Eigentum und Lizenzierung

Mit der Einreichung eines Beitrags bestätigt die beitragende Person, dass:

- sie zur Einreichung berechtigt ist
- der Beitrag keine Rechte Dritter verletzt
- verwendete Inhalte ordnungsgemäß lizenziert sind
- keine vertraulichen Unternehmensdaten enthalten sind
- keine fremden Zugangsdaten enthalten sind
- der Beitrag im Rahmen der Projektlizenz verwendet werden darf

Beiträge dürfen nicht aus fremden Projekten kopiert werden, wenn deren Lizenz eine Nutzung nicht ausdrücklich erlaubt.

Quellen und Lizenzen müssen nachvollziehbar angegeben werden.

Die Annahme eines Beitrags begründet keinen Anspruch auf Vergütung oder spätere Verfügungsrechte am Gesamtprojekt.

---

## 30. Mit künstlicher Intelligenz erzeugte Beiträge

Mit Unterstützung künstlicher Intelligenz erzeugte Inhalte sind nicht grundsätzlich ausgeschlossen.

Sie müssen jedoch vollständig geprüft werden.

Die einreichende Person bleibt verantwortlich für:

- technische Richtigkeit
- Sicherheit
- Qualität
- Lizenzkonformität
- Datenschutz
- Nachvollziehbarkeit
- Funktionsfähigkeit
- Testabdeckung
- mögliche Nebenwirkungen

Ungeprüfte oder massenhaft automatisiert erzeugte Beiträge werden nicht akzeptiert.

---

## 31. Abwärtskompatibilität

Änderungen sollten bestehende Installationen, gespeicherte Scans und Exporte nicht unnötig beschädigen.

Bei inkompatiblen Änderungen müssen:

- Gründe dokumentiert werden
- Auswirkungen beschrieben werden
- Migrationswege geprüft werden
- Versionsnummern angepasst werden
- Datenbankänderungen getestet werden
- Release-Hinweise vorbereitet werden

Unangekündigte Breaking Changes werden nicht akzeptiert.

---

## 32. Performance

Performance-Optimierungen müssen messbar und nachvollziehbar sein.

Ein Beitrag sollte nach Möglichkeit enthalten:

- Ausgangszustand
- verwendete Messmethode
- Testumgebung
- Vergleichswerte
- Ergebnis
- mögliche Nebenwirkungen

Optimierungen dürfen Lesbarkeit, Sicherheit oder Wartbarkeit nicht unverhältnismäßig verschlechtern.

---

## 33. Barrierefreiheit und Bedienbarkeit

Änderungen an der Benutzeroberfläche sollten berücksichtigen:

- lesbare Kontraste
- verständliche Beschriftungen
- logische Tab-Reihenfolge
- skalierbare Layouts
- verständliche Fehlermeldungen
- ausreichende Größen von Bedienelementen
- konsistente Tastaturbedienung
- klare Statusanzeigen
- keine ausschließlich farbbasierte Bedeutung

Verbesserungen der Barrierefreiheit sind ausdrücklich willkommen.

---

## 34. Release-bezogene Änderungen

Änderungen, die ein Release beeinflussen, müssen zusätzlich berücksichtigen:

- Versionsnummer
- Anwendungstitel
- Build-Dateien
- PyInstaller-Konfiguration
- Abhängigkeiten
- Prüfsummen
- Release-Artefakte
- Changelog
- Kompatibilität
- Installation
- Startskripte

Release-Artefakte werden ausschließlich durch den Projektverantwortlichen veröffentlicht.

---

## 35. Kontakt

**Projektverantwortlicher:**  
Thorsten Bylicki | BylickiLabs

**GitHub-Profil:**  
https://github.com/bylickilabs

**Projekt-Repository:**  
https://github.com/bylickilabs/BylickiLabs-Web-Security-Inspector

Allgemeine Beiträge können über Issues und Pull Requests eingereicht werden.

Vertrauliche Sicherheitsmeldungen dürfen nicht öffentlich veröffentlicht werden und müssen über die auf dem GitHub-Profil hinterlegte Kontaktmöglichkeit erfolgen.

---

## 36. Änderungen dieser Beitragsrichtlinien

Diese Beitragsrichtlinien können angepasst werden, wenn sich:

- Projektumfang
- technische Architektur
- Entwicklungsprozess
- Build-System
- Sicherheitsanforderungen
- Kontaktwege
- unterstützte Plattformen
- Qualitätsanforderungen

ändern.

Die jeweils aktuelle Fassung wird im Repository veröffentlicht.

---

## 37. Schlussbestimmung

Beiträge zum BylickiLabs Web Security Inspector sollen die Anwendung technisch verbessern, sicherer machen und langfristig wartbar halten.

Qualität, Nachvollziehbarkeit, Sicherheit und Projektbezug haben Vorrang vor Geschwindigkeit oder Umfang eines Beitrags.

---

Copyright © 2026 Thorsten Bylicki | BylickiLabs.  
Alle Rechte vorbehalten.
