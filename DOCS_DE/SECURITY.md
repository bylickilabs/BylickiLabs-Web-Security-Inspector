# Sicherheitsrichtlinie

## BylickiLabs Web Security Inspector

**Version:** 1.0  
**Gültig ab:** 4. August 2026  
**Projekt:** BylickiLabs Web Security Inspector 2.0.0  
**Verantwortlich:** Thorsten Bylicki | BylickiLabs  

---

## 1. Zweck dieser Sicherheitsrichtlinie

Diese Sicherheitsrichtlinie beschreibt den verantwortungsvollen Umgang mit Sicherheitsmeldungen, Schwachstellen, vertraulichen technischen Informationen und sicherheitsrelevanten Beiträgen zum BylickiLabs Web Security Inspector.

Sie legt fest:

- welche Versionen unterstützt werden
- welche Arten von Sicherheitsproblemen gemeldet werden sollen
- welche Informationen eine Meldung enthalten sollte
- wie vertrauliche Meldungen eingereicht werden
- wie Sicherheitsmeldungen geprüft und bearbeitet werden
- welche Verhaltensregeln bei Sicherheitsforschung und Offenlegung gelten
- welche Inhalte nicht öffentlich veröffentlicht werden dürfen
- welche Grenzen und Verantwortlichkeiten für Anwender gelten

Diese Richtlinie dient dem Schutz des Projekts, seiner Anwender, der Entwicklungsumgebung und möglicher betroffener Dritter.

---

## 2. Unterstützte Versionen

Sicherheitskorrekturen werden grundsätzlich für die aktuell gepflegte Hauptversion bereitgestellt.

| Version | Unterstützt |
|---|---|
| 2.0.x | Ja |
| 1.x | Nein |
| ältere Versionen | Nein |

Nicht mehr unterstützte Versionen erhalten keine garantierten Sicherheitskorrekturen, Fehlerbehebungen oder Kompatibilitätsanpassungen.

Anwender sollten immer die aktuellste veröffentlichte Version verwenden.

---

## 3. Geltungsbereich

Diese Sicherheitsrichtlinie gilt für:

- den Quellcode des BylickiLabs Web Security Inspector
- die Desktop-Anwendung
- die Scan-Engine
- die Benutzeroberfläche
- die SQLite-Datenbank
- Exportfunktionen
- Berichtsformate
- Build-Skripte
- Installations- und Startskripte
- GitHub Actions Workflows
- Konfigurationsdateien
- optionale externe API-Integrationen
- Repository-Dateien
- Releases und bereitgestellte Binärdateien

Nicht Bestandteil dieser Richtlinie sind:

- fremde Systeme, die mit der Anwendung geprüft werden
- externe Dienste und Plattformen
- Drittanbieterbibliotheken außerhalb des Einflussbereichs des Projekts
- Betriebssysteme und lokale Sicherheitskonfigurationen der Anwender
- Netzwerke oder Server, die nicht durch BylickiLabs betrieben werden

Sicherheitsprobleme in Drittanbieterkomponenten können dennoch gemeldet werden, wenn sie das Projekt unmittelbar betreffen.

---

## 4. Sicherheitsprobleme, die gemeldet werden sollten

Folgende Arten von Sicherheitsproblemen sind für eine Meldung besonders relevant:

- unbeabsichtigte Offenlegung sensibler Daten
- ungeschützte Speicherung von Zugangsdaten oder API-Schlüsseln
- unsichere Verarbeitung von Konfigurationsdaten
- Schwachstellen in der lokalen Datenbank
- SQL-Injection innerhalb der Anwendung
- Path-Traversal-Schwachstellen
- unsichere Dateiverarbeitung
- unkontrollierte Dateischreibvorgänge
- unzureichende Eingabevalidierung
- Server-Side Request Forgery innerhalb der Scan-Engine
- unsichere URL-Verarbeitung
- fehlende Begrenzung von Zieladressen
- ungewollter Zugriff auf lokale oder interne Ressourcen
- unsichere Verarbeitung von HTML- oder Berichtsdaten
- Cross-Site-Scripting in erzeugten HTML-Berichten
- Code-Injection
- Command-Injection
- unsichere Nutzung externer Prozesse
- Manipulation von Build- oder Installationsskripten
- unsichere Update- oder Release-Artefakte
- fehlerhafte Berechtigungen
- unzureichende Trennung sicherheitsrelevanter Komponenten
- unsichere Protokollierung
- Offenlegung vertraulicher Scan-Ergebnisse
- ungeschützte Exportdateien
- unsichere Deserialisierung
- Schwachstellen durch eingebundene Drittanbieterbibliotheken
- Manipulation von Risikoscore oder Befunddaten
- sicherheitsrelevante Fehler in der internationalen Benutzeroberfläche
- Möglichkeiten zur Umgehung vorgesehener Schutzmaßnahmen

Auch reproduzierbare Abstürze oder Denial-of-Service-Situationen können sicherheitsrelevant sein, wenn sie durch gezielte Eingaben oder manipulierte Zielsysteme ausgelöst werden können.

---

## 5. Inhalte, die keine vertrauliche Sicherheitsmeldung erfordern

Folgende Themen können in der Regel als reguläres GitHub Issue gemeldet werden:

- Darstellungsfehler
- Übersetzungsfehler
- Schreibfehler
- allgemeine Funktionswünsche
- nicht sicherheitsrelevante Performanceprobleme
- Bedienungsfragen
- Installationsprobleme
- fehlende Dokumentation
- bekannte Einschränkungen von Drittanbieter-APIs
- unvollständige oder fehlerhafte Scan-Ergebnisse ohne Sicherheitsauswirkung
- falsche Positivmeldungen
- falsche Negativmeldungen
- kleinere Fehler in Diagrammen oder Statistiken
- nicht vertrauliche Build-Probleme

Wenn unklar ist, ob ein Problem sicherheitsrelevant ist, sollte es zunächst vertraulich gemeldet werden.

---

## 6. Vertrauliche Meldung einer Sicherheitslücke

Sicherheitslücken dürfen nicht öffentlich als GitHub Issue, Discussion, Pull Request, Kommentar oder Social-Media-Beitrag veröffentlicht werden.

Vertrauliche Meldungen sind über die auf dem GitHub-Profil von BylickiLabs hinterlegte Kontaktmöglichkeit einzureichen.

**GitHub-Profil:**  
https://github.com/bylickilabs

**Projekt-Repository:**  
https://github.com/bylickilabs/BylickiLabs-Web-Security-Inspector

Die Meldung sollte eindeutig als Sicherheitsmeldung gekennzeichnet werden.

Empfohlener Betreff:

```text
Security Report: BylickiLabs Web Security Inspector
```

Es besteht kein Anspruch auf eine bestimmte Kontaktmethode, Reaktionszeit oder Bearbeitungsfrist.

---

## 7. Erforderliche Angaben einer Sicherheitsmeldung

Eine vollständige Meldung sollte möglichst folgende Informationen enthalten:

- Name oder Kennung der meldenden Person
- bevorzugter Kontaktweg
- betroffene Version
- betroffene Datei oder Komponente
- Betriebssystem und Umgebung
- klare technische Beschreibung
- Voraussetzungen zur Reproduktion
- genaue Reproduktionsschritte
- erwartetes Verhalten
- tatsächlich beobachtetes Verhalten
- mögliche Auswirkungen
- Einschätzung des Schweregrads
- vorhandene Protokolle
- Fehlermeldungen
- Screenshots
- Proof of Concept ohne destruktive Nutzlast
- mögliche Schutzmaßnahme
- bekannte Umgehungen
- Information, ob die Schwachstelle bereits veröffentlicht wurde
- Information, ob Dritte betroffen sind
- Information, ob sensible Daten eingesehen wurden

Unvollständige Meldungen können dennoch geprüft werden, sofern das Problem nachvollziehbar beschrieben ist.

---

## 8. Nicht zulässige Inhalte in Sicherheitsmeldungen

Folgende Inhalte dürfen nicht unnötig übermittelt werden:

- echte Zugangsdaten
- produktive API-Schlüssel
- private Schlüssel
- vollständige personenbezogene Datensätze
- Daten unbeteiligter Dritter
- fremde vertrauliche Dokumente
- Schadsoftware
- Ransomware
- destruktive Exploits
- automatisierte Angriffswerkzeuge
- Anleitungen für unbefugte Angriffe
- Inhalte, die nicht zur Prüfung der Meldung erforderlich sind

Wenn Nachweise sensible Daten enthalten, müssen diese soweit möglich geschwärzt oder anonymisiert werden.

---

## 9. Verantwortungsvolle Sicherheitsforschung

Sicherheitsforschung im Zusammenhang mit diesem Projekt muss verantwortungsvoll, kontrolliert und rechtmäßig durchgeführt werden.

Zulässig sind insbesondere:

- Prüfungen am eigenen System
- Prüfungen in einer eigenen Laborumgebung
- Prüfungen an ausdrücklich freigegebenen Testsystemen
- statische Codeanalyse
- lokale Analyse des Quellcodes
- sichere Reproduktion in isolierten Umgebungen
- nicht destruktive Proof-of-Concepts
- Abhängigkeitsanalysen
- Prüfung veröffentlichter Build-Artefakte

Nicht zulässig sind:

- unbefugte Prüfungen fremder Systeme
- Zugriff auf fremde Daten
- Beeinträchtigung produktiver Dienste
- Denial-of-Service-Angriffe
- Social Engineering
- Phishing
- Manipulation fremder Konten
- Umgehung von Authentifizierung
- dauerhafte Veränderung von Daten
- Veröffentlichung vertraulicher Informationen
- Ausnutzung einer Schwachstelle über das zur Bestätigung notwendige Maß hinaus

Die Verantwortung für Rechtmäßigkeit, Freigaben, Zielsysteme und Folgen einer Prüfung liegt bei der prüfenden Person.

---

## 10. Safe-Harbor-Grundsätze

BylickiLabs beabsichtigt nicht, rechtliche Schritte gegen Personen einzuleiten, die:

- in gutem Glauben handeln
- ausschließlich eigene oder ausdrücklich freigegebene Systeme prüfen
- diese Sicherheitsrichtlinie einhalten
- keine Daten beschädigen oder verändern
- keine personenbezogenen oder vertraulichen Daten unnötig einsehen
- keine Dienste beeinträchtigen
- die Schwachstelle vertraulich melden
- angemessene Zeit für Prüfung und Korrektur einräumen
- keine Erpressung oder Druckmittel einsetzen

Diese Erklärung stellt keine rechtliche Garantie, keinen Vertrag und keine allgemeine Genehmigung für Sicherheitsprüfungen dar.

Sie gilt nicht für Prüfungen fremder Systeme, Verstöße gegen Gesetze, Vertragsverletzungen oder Handlungen außerhalb des Einflussbereichs von BylickiLabs.

---

## 11. Bearbeitung eingehender Sicherheitsmeldungen

Nach Eingang einer Sicherheitsmeldung können folgende Schritte erfolgen:

1. Eingang der Meldung erfassen
2. Plausibilität prüfen
3. betroffene Version bestimmen
4. Reproduzierbarkeit bewerten
5. Auswirkungen einschätzen
6. Schweregrad festlegen
7. vorhandene Schutzmaßnahmen prüfen
8. Korrektur oder Workaround entwickeln
9. Tests durchführen
10. Release oder Patch vorbereiten
11. Veröffentlichung koordinieren
12. Meldung abschließen

Nicht jede Meldung führt automatisch zu einer Änderung.

Eine Meldung kann geschlossen werden, wenn:

- das Verhalten beabsichtigt ist
- keine Sicherheitsauswirkung vorliegt
- das Problem nicht reproduzierbar ist
- die betroffene Version nicht unterstützt wird
- die Ursache in einer fremden Komponente liegt
- notwendige Informationen fehlen
- die Meldung bereits bekannt ist
- die Meldung gegen diese Richtlinie verstößt

---

## 12. Reaktions- und Bearbeitungszeiten

Sicherheitsmeldungen werden nach Möglichkeit zeitnah geprüft.

Es werden jedoch keine verbindlichen Fristen garantiert.

Die Bearbeitungsdauer hängt unter anderem ab von:

- Vollständigkeit der Meldung
- Reproduzierbarkeit
- technischem Umfang
- möglicher Auswirkung
- Verfügbarkeit des Projektverantwortlichen
- Abhängigkeit von Drittanbietern
- notwendigem Testaufwand
- erforderlicher Release-Planung

Kritische Probleme werden grundsätzlich höher priorisiert als kleinere oder theoretische Risiken.

---

## 13. Einstufung des Schweregrads

Die Bewertung kann sich an folgenden Stufen orientieren:

| Stufe | Beschreibung |
|---|---|
| Kritisch | unmittelbare Gefährdung sensibler Daten, Code-Ausführung oder vollständige Kompromittierung |
| Hoch | erhebliche Sicherheitsauswirkung mit realistischem Angriffsweg |
| Mittel | relevante Schwachstelle mit zusätzlichen Voraussetzungen oder begrenzter Auswirkung |
| Niedrig | geringes Risiko, eingeschränkter Angriffsweg oder Härtungsempfehlung |
| Information | technischer Hinweis ohne unmittelbare Sicherheitsauswirkung |

Zur zusätzlichen Einordnung können CVSS, CWE, OWASP oder vergleichbare Standards herangezogen werden.

Die endgültige Bewertung erfolgt durch den Projektverantwortlichen.

---

## 14. Koordinierte Offenlegung

Sicherheitsprobleme sollen koordiniert und erst nach angemessener Prüfung veröffentlicht werden.

Eine Veröffentlichung vor Bereitstellung einer Korrektur kann Anwender unnötig gefährden.

Erwartet wird daher:

- vertrauliche Erstmeldung
- Abstimmung über technische Details
- angemessene Zeit für Analyse und Korrektur
- keine Veröffentlichung funktionierender Exploits vor einem Patch
- keine Weitergabe vertraulicher Informationen an Dritte
- Abstimmung einer möglichen öffentlichen Nennung

Der Zeitpunkt und Umfang einer öffentlichen Veröffentlichung werden durch den Projektverantwortlichen festgelegt.

---

## 15. Anerkennung von Sicherheitsmeldungen

Eine öffentliche Nennung meldender Personen kann nach Ermessen des Projektverantwortlichen erfolgen.

Voraussetzungen können sein:

- verantwortungsvolle Meldung
- Einhaltung dieser Sicherheitsrichtlinie
- nachvollziehbare technische Informationen
- keine vorherige unkoordinierte Veröffentlichung
- Zustimmung zur Namensnennung

Es besteht kein Anspruch auf:

- öffentliche Nennung
- Vergütung
- Prämien
- Bug-Bounty-Zahlungen
- Zertifikate
- Referenzen
- Priorisierung
- Umsetzung eines Lösungsvorschlags

Das Projekt betreibt kein öffentliches Bug-Bounty-Programm.

---

## 16. Sicherheitsupdates und Veröffentlichungen

Sicherheitskorrekturen können bereitgestellt werden als:

- Patch-Release
- Minor-Release
- aktualisierte Binärdatei
- korrigiertes Build-Skript
- aktualisierte Abhängigkeit
- Konfigurationsänderung
- dokumentierter Workaround
- Sicherheitshinweis im Repository
- GitHub Security Advisory

Ein Sicherheitsupdate kann Änderungen an Funktionen, Einstellungen, Datenformaten oder Abhängigkeiten enthalten.

Anwender sollten neue Releases prüfen und zeitnah installieren.

---

## 17. Integrität von Releases

Offizielle Releases werden ausschließlich über das Projekt-Repository veröffentlicht:

https://github.com/bylickilabs/BylickiLabs-Web-Security-Inspector

Anwender sollten:

- Releases nur aus offiziellen Quellen beziehen
- Prüfsummen kontrollieren, sofern vorhanden
- keine veränderten Binärdateien aus unbekannten Quellen verwenden
- lokale Sicherheitssoftware aktiv halten
- Build-Skripte vor der Ausführung prüfen
- unbekannte Abhängigkeiten nicht ungeprüft installieren
- Release-Hinweise beachten

BylickiLabs übernimmt keine Verantwortung für veränderte, inoffizielle oder von Dritten bereitgestellte Versionen.

---

## 18. Abhängigkeiten und Drittanbieterkomponenten

Das Projekt verwendet verschiedene Drittanbieterbibliotheken.

Dazu können gehören:

- PySide6
- NumPy
- SciPy
- Matplotlib
- Requests
- Beautiful Soup
- dnspython
- ReportLab
- PyInstaller
- pytest
- Ruff

Sicherheitsprobleme in Drittanbieterkomponenten sollten nach Möglichkeit zusätzlich an das jeweilige Ursprungsprojekt gemeldet werden.

Das Projekt kann betroffene Abhängigkeiten aktualisieren, ersetzen, einschränken oder entfernen.

Eine vollständige Fehlerfreiheit aller Drittanbieterkomponenten kann nicht garantiert werden.

---

## 19. Externe APIs und Dienste

Die Anwendung kann optionale externe Dienste verwenden.

Dazu gehören beispielsweise:

- Google PageSpeed Insights
- MDN HTTP Observatory

Bei aktivierter Nutzung können Zieladressen und technisch erforderliche Informationen an den jeweiligen Dienst übertragen werden.

Anwender sind selbst dafür verantwortlich:

- die Nutzung externer Dienste zu aktivieren
- deren Datenschutzbedingungen zu prüfen
- API-Schlüssel sicher zu speichern
- Nutzungslimits einzuhalten
- vertrauliche Ziele nicht unbeabsichtigt zu übertragen

Sicherheitsprobleme eines externen Dienstes liegen außerhalb des direkten Verantwortungsbereichs des Projekts.

---

## 20. Schutz von API-Schlüsseln und Zugangsdaten

API-Schlüssel und Zugangsdaten dürfen nicht:

- in Issues veröffentlicht werden
- in Pull Requests enthalten sein
- in Quellcode eingebettet werden
- in Screenshots sichtbar sein
- in Beispielkonfigurationen mit echten Werten erscheinen
- in Protokollen gespeichert werden
- in exportierten Berichten enthalten sein
- in Commit-Historien verbleiben

Wenn ein Schlüssel versehentlich veröffentlicht wurde, muss er unverzüglich widerrufen und ersetzt werden.

Das Entfernen aus einer aktuellen Datei reicht nicht aus, wenn der Schlüssel bereits in der Git-Historie enthalten ist.

---

## 21. Datenbank- und Dateisicherheit

Die Anwendung verwendet eine lokale SQLite-Datenbank und lokale Konfigurationsdateien.

Anwender sollten:

- das Projektverzeichnis schützen
- Dateiberechtigungen angemessen setzen
- sensible Berichte nicht öffentlich speichern
- Sicherungskopien verschlüsseln
- nicht benötigte Scan-Daten löschen
- keine vertraulichen Ergebnisse in öffentliche Repositorys übertragen
- Exportdateien vor Weitergabe prüfen
- lokale Benutzerkonten absichern

Die Anwendung bietet keine Garantie für vollständige Verschlüsselung aller lokalen Daten.

---

## 22. Berichtssicherheit

Exportierte Berichte können sensible technische Informationen enthalten.

Dazu gehören möglicherweise:

- Zieladressen
- Serverinformationen
- Sicherheitsheader
- Zertifikatsdaten
- DNS-Informationen
- Schwachstellen
- technische Nachweise
- interne Pfade
- Risikobewertungen
- Empfehlungen

Berichte müssen entsprechend ihrer Vertraulichkeit behandelt werden.

Sie dürfen nicht ohne Berechtigung veröffentlicht oder an unbeteiligte Dritte weitergegeben werden.

---

## 23. Protokollierung und Fehlerdaten

Protokolle und Fehlermeldungen können technische Details enthalten.

Vor einer Veröffentlichung sollten folgende Informationen entfernt werden:

- Benutzernamen
- lokale Pfade
- interne Hostnamen
- IP-Adressen
- Zugangsdaten
- API-Schlüssel
- personenbezogene Daten
- vertrauliche Zieladressen
- vollständige Antwortinhalte

Nur die für die Fehleranalyse erforderlichen Informationen sollten weitergegeben werden.

---

## 24. Pull Requests mit Sicherheitsbezug

Pull Requests, die eine noch nicht veröffentlichte Sicherheitslücke beheben, dürfen nicht ohne vorherige Abstimmung öffentlich eingereicht werden.

Stattdessen ist zunächst eine vertrauliche Sicherheitsmeldung erforderlich.

Ein sicherheitsrelevanter Pull Request sollte:

- die Ursache klar beschreiben
- keine sensiblen Exploit-Details enthalten
- Tests für die Korrektur enthalten
- bestehende Funktionen nicht unnötig verändern
- Rückwärtskompatibilität berücksichtigen
- sicherheitsrelevante Nebenwirkungen dokumentieren

Die Annahme eines Pull Requests liegt ausschließlich beim Projektverantwortlichen.

---

## 25. Automatisierte Scanner und Analysewerkzeuge

Automatisierte Scanner dürfen zur Analyse des Quellcodes oder eigener Testumgebungen verwendet werden.

Ergebnisse automatisierter Werkzeuge müssen vor der Meldung manuell geprüft werden.

Nicht erwünscht sind:

- ungeprüfte Massenmeldungen
- automatisch generierte Issues ohne technische Bewertung
- Duplikate
- reine Versionswarnungen ohne tatsächliche Auswirkung
- irreführende Schweregrade
- unvollständige Scanner-Ausgaben ohne Kontext

Qualität und Nachvollziehbarkeit sind wichtiger als die Anzahl gemeldeter Ergebnisse.

---

## 26. Sicherheitsrelevante Änderungen

Änderungen mit möglicher Sicherheitsauswirkung müssen besonders sorgfältig geprüft werden.

Dazu gehören insbesondere Änderungen an:

- URL-Validierung
- Netzwerkzugriff
- Dateisystemzugriff
- Exportfunktionen
- HTML-Erzeugung
- Datenbankabfragen
- Konfiguration
- API-Schlüsseln
- externen Prozessen
- Build-Skripten
- Installationsroutinen
- Abhängigkeiten
- Protokollierung
- Risikobewertung
- Berechtigungen

Solche Änderungen sollten durch Tests und eine nachvollziehbare technische Begründung begleitet werden.

---

## 27. Sicherheitsgrenzen der Anwendung

Der BylickiLabs Web Security Inspector ist ein Analysewerkzeug und kann keine vollständige Sicherheit garantieren.

Die Anwendung kann:

- Schwachstellen übersehen
- Fehlalarme erzeugen
- Konfigurationen unvollständig bewerten
- dynamische Inhalte nicht vollständig erfassen
- durch Schutzmechanismen eingeschränkt werden
- von Drittanbieter-APIs abhängig sein
- Ergebnisse abhängig vom Zeitpunkt der Prüfung liefern
- keine vollständige manuelle Sicherheitsprüfung ersetzen

Ergebnisse müssen immer fachlich bewertet werden.

---

## 28. Verantwortung der Anwender

Anwender tragen die Verantwortung für:

- Auswahl des Zielsystems
- rechtliche Freigabe
- Prüfumfang
- Belastung des Zielsystems
- Schutz der Ergebnisse
- sichere Speicherung
- Auswertung der Befunde
- Umsetzung von Maßnahmen
- Aktualisierung der Anwendung
- Einhaltung interner Richtlinien
- Einhaltung gesetzlicher Vorgaben

Die Nutzung der Anwendung erfolgt auf eigenes Risiko.

---

## 29. Änderungen dieser Sicherheitsrichtlinie

Diese Sicherheitsrichtlinie kann angepasst werden, wenn sich:

- Projektumfang
- unterstützte Versionen
- technische Architektur
- Kontaktwege
- gesetzliche Anforderungen
- externe Dienste
- Release-Prozesse
- Sicherheitsanforderungen

ändern.

Die jeweils aktuelle Fassung wird im Repository veröffentlicht.

---

## 30. Kontakt

**Projektverantwortlicher:**  
Thorsten Bylicki | BylickiLabs

**GitHub-Profil:**  
https://github.com/bylickilabs

**Projekt-Repository:**  
https://github.com/bylickilabs/BylickiLabs-Web-Security-Inspector

Vertrauliche Sicherheitsmeldungen sind über die auf dem GitHub-Profil hinterlegte Kontaktmöglichkeit einzureichen.

Sicherheitslücken dürfen nicht als öffentliches Issue veröffentlicht werden.

---

## 31. Schlussbestimmung

Diese Sicherheitsrichtlinie soll eine verantwortungsvolle, nachvollziehbare und koordinierte Bearbeitung von Sicherheitsproblemen gewährleisten.

Vertrauliche Offenlegung, technische Präzision und der Schutz betroffener Anwender haben Vorrang vor öffentlicher Aufmerksamkeit oder schneller Veröffentlichung.

---

Copyright © 2026 Thorsten Bylicki | BylickiLabs.  
Alle Rechte vorbehalten.
