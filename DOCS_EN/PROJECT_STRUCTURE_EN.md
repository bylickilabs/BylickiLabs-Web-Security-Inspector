# Project Structure

## BylickiLabs Web Security Inspector

**Version:** 1.0  
**Effective date:** August 4, 2026  
**Project:** BylickiLabs Web Security Inspector 2.0.0  
**Responsible party:** Thorsten Bylicki | BylickiLabs  

---

## 1. Purpose

This file defines the binding requirements, procedures, responsibilities, and quality standards for **Project Structure** within BylickiLabs Web Security Inspector.

It serves as a standalone reference for development, operation, assessment, publication, and long-term maintenance of the project.

---

## 2. Scope

This policy applies to:

- source code and desktop application
- PySide6 user interface
- central scan engine and scanner modules
- SQLite database and local settings
- NumPy, SciPy, and Matplotlib components
- reports and exports
- build, test, and release processes
- repository, issues, pull requests, and releases

Special cases not covered by this document are evaluated by the project maintainer.

---

## 3. Objectives

This documentation pursues the following objectives:

- consistent and traceable procedures
- clear responsibilities
- reproducible technical results
- protection of security, privacy, and data integrity
- long-term maintainability
- consistent German and English documentation
- controlled changes without unnecessary backward incompatibility

---

## 4. Technical Focus Areas

- **Modular separation of user interface, scan engine, data storage, and reporting:** is defined, professionally assessed, and reviewed on a regular basis.
- **Consistent data models for scans, findings, measurements, and exports:** is defined, professionally assessed, and reviewed on a regular basis.
- **Controlled interaction between PySide6, SQLite, NumPy, SciPy, and Matplotlib:** is defined, professionally assessed, and reviewed on a regular basis.
- **Extensibility of scanner modules without unnecessary coupling:** is defined, professionally assessed, and reviewed on a regular basis.
- **Traceable data flows, error boundaries, and security controls:** is defined, professionally assessed, and reviewed on a regular basis.

---

## 5. Binding Requirements

All work in this area must:

- match the actual functionality
- be documented in a technically traceable manner
- consider security implications
- protect existing data and functionality
- be reproducible on Windows
- support automated and manual validation
- respect the bilingual project structure
- avoid publishing credentials or confidential information
- comply with the project license and applicable law

---

## 6. Standard Process

1. Determine the objective, scope, and affected components.
2. Review the existing implementation and documentation.
3. Assess security, privacy, and compatibility implications.
4. Implement the change or measure in a separate working branch.
5. Run automated tests and quality checks.
6. Manually validate the user interface, database, exports, and build where required.
7. Update German and English content consistently.
8. Document the result transparently.
9. Obtain approval from the project maintainer.
10. Publish or archive the change in a controlled manner.

---

## 7. Roles and Responsibilities

### Project Maintainer

The project maintainer decides on architecture, priorities, contribution acceptance, versioning, releases, and binding changes.

### Contributors

Contributors are responsible for technical correctness, tests, documentation, license compliance, and secure implementation of their contributions.

### Users

Users are responsible for installation, target selection, legal authorization, secure storage, and professional assessment of results.

---

## 8. Quality Criteria

A result is considered professional when it:

- is documented clearly and completely
- works reproducibly
- contains no known critical defects
- passes the existing tests
- introduces no unnecessary dependencies
- uses secure defaults
- handles errors in a controlled manner
- safely processes special characters and dynamic content
- considers database and export compatibility
- is consistently available in German and English

---

## 9. Security and Privacy

Security-relevant information must not be disclosed unnecessarily.

The following require particular protection:

- target addresses and internal systems
- scan results
- technical evidence
- API keys
- local database files
- exported reports
- personal data
- unpublished vulnerabilities
- build and release artifacts

Assessments may only be performed against owned or explicitly authorized systems.

---

## 10. Compatibility and Changes

Changes must be reviewed for their impact on:

- Python version
- Windows version
- PySide6
- SQLite schema
- data models
- export formats
- PyInstaller build
- stored scan history
- settings
- external APIs

Incompatible changes must be documented and identified through an appropriate version change.

---

## 11. Validation and Approval

Depending on the scope of the change, the following must be performed before approval:

- Python syntax validation
- Ruff
- pytest
- scanner tests
- database tests
- statistics tests
- export tests
- manual application startup
- Windows build
- visual review of the German and English user interface

Final approval is granted by the project maintainer.


## Reference Structure


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

## 12. Maintenance of This File

This file is updated when project scope, architecture, processes, dependencies, security requirements, or contact methods change.

The current version must be published in the official repository.

---

## 13. Contact

**Project maintainer:**  
Thorsten Bylicki | BylickiLabs

**GitHub profile:**  
https://github.com/bylickilabs

**Project repository:**  
https://github.com/bylickilabs/BylickiLabs-Web-Security-Inspector

Confidential security reports must not be published as public issues.

---

## 14. Final Provision

The requirements in this file are intended to ensure professional, secure, traceable, and maintainable project operations.

Quality, security, and technical traceability take priority over the speed or size of a change.

---

Copyright © 2026 Thorsten Bylicki | BylickiLabs.  
All rights reserved.
