# Projektstruktur

## BylickiLabs Web Security Inspector

**Version:** 1.0  
**Gültig ab:** 4. August 2026  
**Projekt:** BylickiLabs Web Security Inspector 2.0.0  
**Verantwortlich:** Thorsten Bylicki | BylickiLabs  

---

## 1. Zweck

Diese Datei definiert die verbindlichen Anforderungen, Abläufe, Zuständigkeiten und Qualitätsmaßstäbe für den Bereich **Projektstruktur** innerhalb des BylickiLabs Web Security Inspector.

Sie dient als eigenständige Referenz für Entwicklung, Betrieb, Prüfung, Veröffentlichung und langfristige Pflege des Projekts.

---

## 2. Geltungsbereich

Die Richtlinie gilt für:

- Quellcode und Desktop-Anwendung
- PySide6-Benutzeroberfläche
- zentrale Scan-Engine und Scanner-Module
- SQLite-Datenbank und lokale Einstellungen
- NumPy-, SciPy- und Matplotlib-Komponenten
- Berichte und Exporte
- Build-, Test- und Release-Prozesse
- Repository, Issues, Pull Requests und Releases

Nicht erfasste Sonderfälle werden durch den Projektverantwortlichen bewertet.

---

## 3. Ziele

Mit dieser Dokumentation werden folgende Ziele verfolgt:

- einheitliche und nachvollziehbare Vorgehensweisen
- klare Verantwortlichkeiten
- reproduzierbare technische Ergebnisse
- Schutz von Sicherheit, Datenschutz und Datenintegrität
- langfristige Wartbarkeit
- konsistente deutsche und englische Dokumentation
- kontrollierte Änderungen ohne unnötige Abwärtsinkompatibilität

---

## 4. Fachliche Schwerpunkte

- **Modulare trennung von benutzeroberfläche, scan-engine, datenhaltung und reporting:** wird verbindlich beschrieben, fachlich eingeordnet und regelmäßig überprüft.
- **Einheitliche datenmodelle für scans, befunde, messwerte und exporte:** wird verbindlich beschrieben, fachlich eingeordnet und regelmäßig überprüft.
- **Kontrollierte kommunikation zwischen pyside6, sqlite, numpy, scipy und matplotlib:** wird verbindlich beschrieben, fachlich eingeordnet und regelmäßig überprüft.
- **Erweiterbarkeit der scanner-module ohne unnötige kopplung:** wird verbindlich beschrieben, fachlich eingeordnet und regelmäßig überprüft.
- **Nachvollziehbare datenflüsse, fehlergrenzen und sicherheitskontrollen:** wird verbindlich beschrieben, fachlich eingeordnet und regelmäßig überprüft.

---

## 5. Verbindliche Anforderungen

Alle Arbeiten in diesem Bereich müssen:

- mit dem tatsächlichen Funktionsumfang übereinstimmen
- technisch nachvollziehbar dokumentiert werden
- sicherheitsrelevante Auswirkungen berücksichtigen
- bestehende Daten und Funktionen schützen
- unter Windows reproduzierbar sein
- automatisierte und manuelle Prüfungen ermöglichen
- die zweisprachige Projektstruktur beachten
- keine Zugangsdaten oder vertraulichen Informationen veröffentlichen
- mit der Projektlizenz und geltendem Recht vereinbar sein

---

## 6. Standardprozess

1. Ziel, Umfang und betroffene Komponenten bestimmen.
2. bestehende Implementierung und Dokumentation prüfen.
3. Sicherheits-, Datenschutz- und Kompatibilitätsauswirkungen bewerten.
4. Änderung oder Maßnahme in einem getrennten Arbeitsstand umsetzen.
5. automatisierte Tests und Qualitätsprüfungen durchführen.
6. Benutzeroberfläche, Datenbank, Exporte und Build bei Bedarf manuell prüfen.
7. deutsche und englische Inhalte synchron aktualisieren.
8. Ergebnis nachvollziehbar dokumentieren.
9. Freigabe durch den Projektverantwortlichen einholen.
10. Änderung kontrolliert veröffentlichen oder archivieren.

---

## 7. Rollen und Verantwortlichkeiten

### Projektverantwortlicher

Der Projektverantwortliche entscheidet über Architektur, Prioritäten, Annahme von Beiträgen, Versionierung, Releases und verbindliche Änderungen.

### Mitwirkende

Mitwirkende sind für technische Richtigkeit, Tests, Dokumentation, Lizenzkonformität und sichere Umsetzung ihrer Beiträge verantwortlich.

### Anwender

Anwender sind für Installation, Zielauswahl, rechtliche Freigabe, sichere Speicherung und fachliche Bewertung der Ergebnisse verantwortlich.

---

## 8. Qualitätskriterien

Ein Ergebnis gilt als professionell, wenn es:

- verständlich und vollständig dokumentiert ist
- reproduzierbar funktioniert
- keine bekannten kritischen Fehler enthält
- bestehende Tests besteht
- keine unnötigen Abhängigkeiten einführt
- sichere Standardwerte verwendet
- Fehler kontrolliert behandelt
- Sonderzeichen und dynamische Inhalte sicher verarbeitet
- Datenbank- und Exportkompatibilität berücksichtigt
- in Deutsch und Englisch konsistent verfügbar ist

---

## 9. Sicherheit und Datenschutz

Sicherheitsrelevante Informationen dürfen nicht unnötig öffentlich gemacht werden.

Besonders zu schützen sind:

- Zieladressen und interne Systeme
- Scan-Ergebnisse
- technische Nachweise
- API-Schlüssel
- lokale Datenbankdateien
- exportierte Berichte
- personenbezogene Daten
- unveröffentlichte Schwachstellen
- Build- und Release-Artefakte

Prüfungen dürfen ausschließlich an eigenen oder ausdrücklich freigegebenen Systemen erfolgen.

---

## 10. Kompatibilität und Änderungen

Änderungen müssen auf Auswirkungen auf folgende Bereiche geprüft werden:

- Python-Version
- Windows-Version
- PySide6
- SQLite-Schema
- Datenmodelle
- Exportformate
- PyInstaller-Build
- gespeicherte Scan-Verläufe
- Einstellungen
- externe APIs

Inkompatible Änderungen sind zu dokumentieren und über eine passende Versionsänderung kenntlich zu machen.

---

## 11. Prüfung und Freigabe

Vor einer Freigabe sind abhängig vom Änderungsumfang auszuführen:

- Python-Syntaxprüfung
- Ruff
- pytest
- Scanner-Tests
- Datenbanktests
- Statistiktests
- Exporttests
- manueller Start der Anwendung
- Windows-Build
- Sichtprüfung der deutschen und englischen Oberfläche

Die endgültige Freigabe erfolgt durch den Projektverantwortlichen.


## Referenzstruktur


```text
BylickiLabs-Web-Security-Inspector/
├── app/
│   ├── core/
│   ├── reporting/
│   ├── scanners/
│   └── ui/
├── assets/
├── data/
├── reports/
├── scripts/
├── tests/
├── INSTALL.bat
├── START.bat
├── main.py
├── pyproject.toml
├── requirements.txt
└── requirements-dev.txt
```


---

## 12. Pflege dieser Datei

Diese Datei wird aktualisiert, wenn sich Projektumfang, Architektur, Prozesse, Abhängigkeiten, Sicherheitsanforderungen oder Kontaktwege ändern.

Die aktuelle Fassung ist im offiziellen Repository zu veröffentlichen.

---

## 13. Kontakt

**Projektverantwortlicher:**  
Thorsten Bylicki | BylickiLabs

**GitHub-Profil:**  
https://github.com/bylickilabs

**Projekt-Repository:**  
https://github.com/bylickilabs/BylickiLabs-Web-Security-Inspector

Vertrauliche Sicherheitsmeldungen dürfen nicht als öffentliches Issue veröffentlicht werden.

---

## 14. Schlussbestimmung

Die Vorgaben dieser Datei sollen einen professionellen, sicheren, nachvollziehbaren und langfristig wartbaren Projektbetrieb gewährleisten.

Qualität, Sicherheit und technische Nachvollziehbarkeit haben Vorrang vor Geschwindigkeit oder Umfang einer Änderung.

---

Copyright © 2026 Thorsten Bylicki | BylickiLabs.  
Alle Rechte vorbehalten.
