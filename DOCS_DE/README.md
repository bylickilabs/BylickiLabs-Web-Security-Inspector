<div align="center">

| <img src="assets/bwsi.png" alt="BylickiLabs Web Security Inspector" width="150"> |
|---|

# BylickiLabs Web Security Inspector

### Enterprise Website Security Analytics

**Professionelle, zweisprachige Desktop-Anwendung für strukturierte Website-, Konfigurations-, Performance- und Sicherheitsanalysen**

| [![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)](https://github.com/bylickilabs/BylickiLabs-Web-Security-Inspector) | [![Python](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/) | 
|---|---|

| [![PySide6](https://img.shields.io/badge/UI-PySide6-green.svg)](https://doc.qt.io/qtforpython-6/) | [![NumPy](https://img.shields.io/badge/Analytics-NumPy-blue.svg)](https://numpy.org/) | [![SciPy](https://img.shields.io/badge/Statistics-SciPy-blue.svg)](https://scipy.org/) |
|---|---|---|

| [![Matplotlib](https://img.shields.io/badge/Charts-Matplotlib-orange.svg)](https://matplotlib.org/) | [![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)](https://www.microsoft.com/windows) | [![License](https://img.shields.io/badge/License-All%20Rights%20Reserved-red.svg)](#lizenz |
|---|---|---|

</div>

<br>

---

<br>

## Übersicht

> Der **BylickiLabs Web Security Inspector 2.0.0** ist eine vollständig neu entwickelte Desktop-Anwendung zur strukturierten Analyse von Websites, Domains und webbasierten Diensten.

> Die Anwendung verbindet technische Prüfverfahren mit einer professionellen Benutzeroberfläche, einem einheitlichen Risikomodell, lokaler Scan-Historie, statistischen Auswertungen und exportierbaren Berichten.

> Der Schwerpunkt liegt auf einer nachvollziehbaren und zentralisierten Bewertung sicherheitsrelevanter Konfigurationen. Ergebnisse werden nicht nur erfasst, sondern nach Schweregrad, Kategorie und Vertrauensniveau eingeordnet, statistisch ausgewertet und übersichtlich visualisiert.

> Die Anwendung ist vollständig in **Deutsch und Englisch** nutzbar.

<br>

---

<br>

## Kernfunktionen

### Professionelle Benutzeroberfläche

> Die Anwendung ist in klar getrennte Arbeitsbereiche gegliedert:

- **Dashboard** mit zentralen Kennzahlen und Gesamtbewertung
- **Scan Center** zur Konfiguration und Durchführung von Analysen
- **Befunde** mit Suche, Filterung und Detailansicht
- **Statistik** mit numerischen Auswertungen und Diagrammen
- **Verlauf** für frühere Analysen und historische Vergleiche
- **Protokoll** für technische Status- und Fehlermeldungen
- **Einstellungen** für Sprache, Zeitlimits, Messungen und optionale Dienste
- **Info-Dialog** mit vollständigen Anwendungsinformationen
- **GitHub-Button** mit direkter Verknüpfung zum BylickiLabs-Profil

### Dashboard

> Nach Abschluss einer Analyse zeigt das Dashboard unter anderem:
  - Risikoscore von 0 bis 100
  - Sicherheitsbewertung
  - Gesamtzahl der Befunde
  - Anzahl ausgeführter Prüfungen
  - durchschnittliche Antwortzeit
  - vollständige Scandauer
  - Verteilung der Schweregrade
  - Kategorien der erkannten Befunde
  - technische Zusammenfassung des aktuellen Scans

<br>

---

<br>

## Scanprofile

| Profil | Beschreibung |
|---|---|
| **Quick** | Schnelle Prüfung zentraler HTTP-, TLS-, DNS-, Inhalts- und Performance-Merkmale |
| **Standard** | Erweiterte Prüfung einschließlich CORS, HTTP-Methoden und zusätzlicher Konfigurationsanalysen |
| **Extended** | Umfassendes Profil mit zusätzlichen Ressourcen-, Deployment- und Detailprüfungen |

> Die Profile ermöglichen eine kontrollierte Anpassung des Prüfumfangs an Zielsystem, Zeitbedarf und Analysezweck.

<br>

---

<br>

## Integrierte Prüfbereiche

### HTTP und Transport

- HTTP-Statuscodes
- Weiterleitungsketten
- HTTP-Version
- Antwortgröße
- Antwortzeiten
- Serverinformationen
- Transportverschlüsselung
- HTTPS-Nutzung
- technische Antwortmerkmale

### HTTP-Sicherheitsheader

- Content Security Policy
- Strict Transport Security
- X-Content-Type-Options
- X-Frame-Options
- Referrer Policy
- Permissions Policy
- Cross-Origin-Opener-Policy
- Cross-Origin-Resource-Policy
- Cross-Origin-Embedder-Policy
- Schutz gegen MIME Sniffing
- Frame-Schutz
- Richtlinienqualität und Konfigurationshinweise

### Cookies

- Secure
- HttpOnly
- SameSite
- Cookie-Laufzeiten
- Cookie-Konfigurationen
- sicherheitsrelevante Abweichungen
- erkannte Session- und Tracking-Eigenschaften

### CORS

- Access-Control-Allow-Origin
- reflektierte Origin-Werte
- Wildcard-Konfigurationen
- Credential-Kombinationen
- sicherheitsrelevante Cross-Origin-Einstellungen

### Formulare

- Formularmethoden
- Zieladressen
- HTTPS-Übertragung
- Passwortfelder
- externe Formularziele
- sichtbare Token-Hinweise
- mögliche CSRF-Schutzmerkmale
- auffällige Eingabekonfigurationen

### Inhalte und Ressourcen

- Mixed Content
- externe Ressourcen
- externe Domains
- HTML-Kommentare
- Generator-Metadaten
- JavaScript-Bibliothekshinweise
- öffentlich erreichbare Standardressourcen
- typische Deployment-Artefakte
- robots.txt
- sitemap.xml
- security.txt

### TLS und Zertifikate

- Zertifikatsgültigkeit
- verbleibende Laufzeit
- Aussteller
- Subject Alternative Names
- verwendetes TLS-Protokoll
- Cipher Suite
- Zertifikatsinformationen
- Hostname- und Zertifikatsbezug
- grundlegende Transportbewertung

### DNS und Mail-Sicherheit

- A-Records
- AAAA-Records
- MX-Records
- NS-Records
- TXT-Records
- CAA-Records
- SPF
- DMARC
- Mail-Sicherheitskonfiguration
- Nameserver- und Domaininformationen

### HTTP-Methoden

- verfügbare HTTP-Methoden
- OPTIONS-Auswertung
- TRACE-Verhalten
- auffällige oder unnötige Methodenfreigaben
- serverseitige Methodenkonfiguration

### Performance

- mehrfache Antwortzeitmessungen
- Mittelwerte
- Median
- Perzentile
- Schwankungen
- Ausreißer
- zeitlicher Verlauf der Messwerte

<br>

---

<br>

## Statistik mit NumPy und SciPy

> Der Statistikbereich verarbeitet Scanergebnisse und Messreihen mit **NumPy** und **SciPy**.

### NumPy

> NumPy wird unter anderem eingesetzt für:
  - numerische Datenreihen
  - Mittelwertberechnung
  - Medianberechnung
  - Standardabweichung
  - Perzentile
  - Risikogewichtungen
  - aggregierte Kennzahlen
  - vektorisierte Auswertungen
  - Vorbereitung von Diagrammdaten

### SciPy

> SciPy erweitert die Analyse um:
  - Shannon-Entropie
  - lineare Regression
  - Trendberechnungen
  - Schiefe von Verteilungen
  - Z-Score-basierte Ausreißererkennung
  - statistische Bewertung historischer Messreihen
  - weiterführende Verteilungs- und Zusammenhangsanalysen

### Matplotlib

> Die Ergebnisse werden direkt in der Anwendung visualisiert:
  - Schweregradverteilung
  - Befunde nach Kategorien
  - Antwortzeitverlauf
  - historische Risikoentwicklung
  - Vergleich vergangener Scans
  - statistische Trends

<br>

---

<br>

## Risikomodell

> Jeder Befund wird anhand mehrerer Merkmale eingeordnet:
  - Schweregrad
  - Vertrauensniveau
  - Kategorie
  - technischer Nachweis
  - betroffene Adresse
  - Beschreibung
  - empfohlene Maßnahme
  - optionale CWE-Zuordnung
  - Scannerquelle

Verwendete Schweregrade:

| Schweregrad | Bedeutung |
|---|---|
| **Critical** | Sehr hohes Risiko mit unmittelbarem Handlungsbedarf |
| **High** | Erhebliches Risiko mit hoher Priorität |
| **Medium** | Relevante Auffälligkeit mit notwendiger Bewertung |
| **Low** | Geringeres Risiko oder Optimierungspotenzial |
| **Info** | Technischer Hinweis ohne unmittelbare Risikowertung |

> Der Gesamtscore fasst die gewichteten Ergebnisse zu einer einheitlichen Bewertung zusammen. Der Score dient der Priorisierung und ersetzt keine manuelle fachliche Prüfung.

<br>

---

<br>

## Scan-Historie und SQLite

> Abgeschlossene Analysen können lokal in einer SQLite-Datenbank gespeichert werden.
  - Dadurch stehen folgende Funktionen zur Verfügung:
    - Laden früherer Ergebnisse
    - erneute Anzeige aller Befunde
    - historische Risikoverläufe
    - statistische Vergleiche
    - zeitliche Entwicklung der Bewertungen
    - Löschen einzelner Einträge
    - vollständiges Leeren des Verlaufs
    - optionales Deaktivieren der lokalen Speicherung

> Die lokalen Daten werden standardmäßig innerhalb des Projektverzeichnisses gespeichert:

```text
data/scan_history.sqlite3
```

> Anwendungseinstellungen werden lokal gespeichert:

```text
data/settings.json
```

<br>

---

<br>

## Berichte und Exporte

> Scanergebnisse können in mehreren Formaten exportiert werden:

| Format | Einsatzzweck |
|---|---|
| **JSON** | Vollständige strukturierte Daten für Weiterverarbeitung und Archivierung |
| **HTML** | Eigenständiger, browserbasierter Business-Bericht |
| **CSV** | Tabellenbasierte Analyse und Import in Office- oder BI-Werkzeuge |
| **PDF** | Managementübersicht, Archivierung und Weitergabe |
| **SARIF 2.1.0** | Integration in Security-, Entwicklungs- und CI-Plattformen |

> Die Berichte enthalten abhängig vom Format:
  - Zieladresse
  - Scanzeitpunkt
  - Risikoscore
  - Gesamtbewertung
  - Scanprofil
  - Kennzahlen
  - Antwortzeiten
  - Schweregradverteilung
  - vollständige Befundliste
  - technische Nachweise
  - Empfehlungen
  - Kategorien und Referenzen

> Exportierte Berichte werden standardmäßig im Ordner `reports` abgelegt.

<br>

---

<br>

## Optionale externe Dienste

> Die externen Integrationen sind standardmäßig deaktiviert und können innerhalb der Einstellungen aktiviert werden.

### Google PageSpeed Insights

> Die Integration kann zusätzliche Lighthouse-Kategorien liefern:
  - Performance
  - Accessibility
  - Best Practices
  - SEO

> Für häufigere Abfragen kann ein eigener API-Schlüssel hinterlegt werden.

### MDN HTTP Observatory

> Die Observatory-Integration ergänzt die lokale Analyse um eine externe Bewertung sicherheitsrelevanter HTTP-Konfigurationen.
  - Bei aktivierten externen Diensten werden die für die jeweilige Analyse erforderlichen Zielinformationen an den gewählten Dienst übertragen.

<br>

---

<br>

## Systemanforderungen

### Empfohlene Plattform

- Windows 10 oder Windows 11
- 64-Bit-System
- mindestens 4 GB Arbeitsspeicher
- Internetzugang für öffentliche Ziele und externe APIs
- Python 3.11 oder neuer bei Nutzung des Quellcodes

### Verwendete Hauptkomponenten

- Python
- PySide6
- NumPy
- SciPy
- Matplotlib
- SQLite
- Requests
- Beautiful Soup
- dnspython
- ReportLab
- PyInstaller

<br>

---

<br>

## Installation unter Windows

### Automatische Installation

1. Repository herunterladen oder ZIP-Archiv entpacken.
2. `INSTALL.bat` ausführen.
3. Warten, bis die virtuelle Umgebung und alle Abhängigkeiten eingerichtet wurden.
4. `START.bat` ausführen.

> Die Installation erstellt automatisch eine virtuelle Python-Umgebung im Ordner `.venv`.

### Installation über die Eingabeaufforderung

```bat
INSTALL.bat
START.bat
```

### Installation über die vorbereiteten Skripte

```bat
scripts\setup.cmd
scripts\run.cmd
```

### Manuelle Installation

```powershell
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe main.py
```

<br>

---

<br>

## Anwendung starten

> Nach der einmaligen Installation:

```bat
START.bat
```

> Alternativ:

```bat
scripts\run.cmd
```

> Oder direkt über die virtuelle Umgebung:

```powershell
.\.venv\Scripts\python.exe main.py
```

<br>

---

<br>

## Erste Analyse durchführen

1. Anwendung starten.
2. Sprache auswählen.
3. Zum Bereich **Scan Center** wechseln.
4. Zieladresse vollständig eingeben.
5. Scanprofil auswählen.
6. Zeitlimit und Messanzahl kontrollieren.
7. Analyse starten.
8. Ergebnisse im Dashboard prüfen.
9. Befunde nach Schweregrad, Kategorie oder Vertrauensniveau filtern.
10. Statistische Auswertungen im Statistikbereich öffnen.
11. Ergebnis bei Bedarf als HTML, JSON, CSV, PDF oder SARIF exportieren.

Beispiel einer gültigen Zieladresse:

```text
https://example.com
```

<br>

---

<br>

## Automatischer Windows-Build

> Die Anwendung enthält vorbereitete Build-Skripte für die automatische Erstellung einer ausführbaren Windows-Anwendung.

### Entwicklungsumgebung einrichten

```bat
scripts\setup_dev.cmd
```

### EXE-Build starten

```bat
scripts\build_exe.cmd
```

> Der Build-Prozess:
  - prüft die vorhandene Entwicklungsumgebung
  - verwendet die vorbereitete PyInstaller-Konfiguration
  - sammelt benötigte Python-Module
  - integriert Ressourcen und Anwendungssymbole
  - bereinigt vorherige Build-Artefakte
  - kompiliert die Anwendung reproduzierbar
  - erzeugt eine ausführbare Windows-Version

> Das Ergebnis wird standardmäßig hier erstellt:

```text
dist/BylickiLabsWebSecurityInspector/
```

> Die kompilierte Version kann anschließend ohne separate Python-Installation gestartet werden.

<br>

---

<br>

## Qualitätssicherung

### Entwicklungsabhängigkeiten installieren

```bat
scripts\setup_dev.cmd
```

### Vollständige Qualitätsprüfung ausführen

```bat
scripts\quality.cmd
```

> Der Qualitätslauf umfasst:
  - Python-Syntaxprüfung
  - Kompilierung der Python-Module
  - Ruff-Codeanalyse
  - automatisierte pytest-Tests
  - Validierung zentraler Modelle
  - Scanner-Tests
  - Datenbanktests
  - Statistiktests
  - Exporttests
  - Eingabevalidierung

### Tests direkt starten

```powershell
.\.venv\Scripts\python.exe -m pytest
```

### Ruff direkt starten

```powershell
.\.venv\Scripts\python.exe -m ruff check app tests main.py
```

<br>

---

<br>

## Projektstruktur

```text
BylickiLabs-Web-Security-Inspector/
├── app/
│   ├── core/
│   │   ├── database.py
│   │   ├── scanner.py
│   │   ├── settings.py
│   │   ├── statistics.py
│   │   └── validation.py
│   ├── reporting/
│   │   └── exporters.py
│   ├── scanners/
│   │   ├── content.py
│   │   ├── cookies.py
│   │   ├── cors.py
│   │   ├── dns_scan.py
│   │   ├── external.py
│   │   ├── forms.py
│   │   ├── http_headers.py
│   │   ├── methods.py
│   │   ├── performance.py
│   │   ├── resources.py
│   │   └── tls_scan.py
│   ├── ui/
│   │   ├── about_dialog.py
│   │   ├── charts.py
│   │   ├── main_window.py
│   │   ├── theme.py
│   │   └── widgets.py
│   ├── config.py
│   ├── i18n.py
│   └── models.py
├── assets/
├── data/
├── reports/
├── scripts/
├── tests/
├── BylickiLabsWebSecurityInspector.spec
├── INSTALL.bat
├── START.bat
├── main.py
├── pyproject.toml
├── requirements.txt
└── requirements-dev.txt
```

<br>

---

<br>

## Technische Architektur

> Die Anwendung ist modular aufgebaut.

### Benutzeroberfläche

> Die PySide6-Oberfläche verwaltet Navigation, Tabellen, Dialoge, Diagramme, Einstellungen und Benutzerinteraktionen.

### Scan-Engine

> Die zentrale Scan-Engine koordiniert:
  - Zielvalidierung
  - Profilauswahl
  - einzelne Prüfmodule
  - Statusmeldungen
  - Ergebnisaggregation
  - Risikoberechnung
  - Statistik
  - Datenbankspeicherung

### Scanner-Module

> Jeder Prüfbereich ist als separates Modul organisiert. Dadurch können Funktionen erweitert, getestet und gewartet werden, ohne die gesamte Anwendung neu strukturieren zu müssen.

### Datenmodelle

> Einheitliche Datenmodelle sorgen dafür, dass Befunde, Messwerte, Scan-Metadaten und Exportdaten konsistent verarbeitet werden.

### Datenbank

> SQLite speichert Scanverläufe lokal und unterstützt historische Auswertungen.

### Reporting

> Die Exportkomponente erzeugt strukturierte Berichte in mehreren Formaten.

### Internationalisierung

> Texte und Bezeichnungen werden zentral verwaltet, damit die Oberfläche vollständig zwischen Deutsch und Englisch umgeschaltet werden kann.

<br>

---

<br>

## Performance-Optimierungen

Die Version 2.0.0 enthält mehrere technische Optimierungen:

- effizientere Scan-Abläufe
- reduzierte redundante Verarbeitung
- optimierte Ergebnisaggregation
- verbesserte Datenbankzugriffe
- kontrollierte Antwortgrößen
- konfigurierbare Zeitlimits
- konfigurierbare Messanzahl
- strukturierte Modulkommunikation
- optimierte Diagrammaktualisierung
- stabilere Exportverarbeitung
- sicherere Behandlung dynamischer Inhalte
- verbesserte Verarbeitung von IP-Zielen und DNS-Sonderfällen

<br>

---

<br>

## Einstellungen

Innerhalb der Anwendung können unter anderem konfiguriert werden:

- Sprache
- Netzwerkzeitlimit
- Anzahl der Performance-Messungen
- lokale Speicherung
- PageSpeed-Integration
- PageSpeed-API-Schlüssel
- MDN-Observatory-Integration
- Scanoptionen
- Berichtseinstellungen

<br>

---

<br>

## Fehlerbehebung unter Windows

### PowerShell blockiert Skripte

> Die CMD- und BAT-Dateien können ohne Änderung der PowerShell-Ausführungsrichtlinie verwendet werden:

```bat
INSTALL.bat
START.bat
```

### Virtuelle Umgebung fehlt

> Installation erneut ausführen:

```bat
INSTALL.bat
```

### Python wurde nicht gefunden

> Python 3.11 oder neuer installieren und während der Installation die Option **Add Python to PATH** aktivieren.
  - Danach die Eingabeaufforderung neu öffnen und prüfen:

```bat
py --version
```

oder:

```bat
python --version
```

### Anwendung startet nicht

> Direkter Start mit sichtbarer Fehlermeldung:

```powershell
.\.venv\Scripts\python.exe main.py
```

### Build-Skript findet PyInstaller nicht

> Entwicklungsumgebung installieren:

```bat
scripts\setup_dev.cmd
```

> Danach erneut:

```bat
scripts\build_exe.cmd
```

### Alte Build-Dateien verursachen Probleme

> Das Build-Skript verwendet die Option `--clean` und entfernt veraltete temporäre PyInstaller-Daten automatisch.

<br>

---

<br>

## Datenschutz und lokale Verarbeitung

> Die Anwendung speichert Scanverläufe und Einstellungen standardmäßig lokal.
  - Folgende Daten können lokal verarbeitet werden:
    - Zieladresse
    - Scanzeitpunkt
    - Scanprofil
    - Befunde
    - technische Nachweise
    - Antwortzeiten
    - Risikoscore
    - Statistikwerte
    - exportierte Berichte
    - optionale API-Einstellungen

> Die lokale Scan-Historie kann deaktiviert werden.
  - Bei Nutzung externer Dienste gelten zusätzlich deren jeweilige Datenverarbeitungsbedingungen.

<br>

---

<br>

## Verantwortungsvolle Nutzung

> Die Anwendung ist für eigene Systeme, eigene Entwicklungsumgebungen sowie ausdrücklich freigegebene Prüfziele vorgesehen.

> Verantwortlich für die Auswahl des Zielsystems, den Prüfumfang, die erforderlichen Berechtigungen und die Einhaltung rechtlicher oder organisatorischer Vorgaben ist ausschließlich der jeweilige Anwender.

> Automatisierte Ergebnisse müssen fachlich geprüft werden. Kein Scanner kann jede Schwachstelle zuverlässig erkennen oder Fehlalarme vollständig ausschließen.


<br>

---

<br>

## Status

**Version:** 2.0.0  
**Entwicklungsstatus:** Aktive Entwicklung und Optimierung  
**Build-Ziel:** Native Windows-Anwendung  
**Sprachen:** Deutsch und Englisch

<br>

---

<br>

## Lizenz

Copyright © 2026 Thorsten Bylicki | BylickiLabs.
[LICENSE](LICENSE)