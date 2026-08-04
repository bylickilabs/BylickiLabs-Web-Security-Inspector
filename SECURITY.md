# Security Policy

## BylickiLabs Web Security Inspector

**Version:** 1.0  
**Effective date:** August 4, 2026  
**Project:** BylickiLabs Web Security Inspector 2.0.0  
**Responsible party:** Thorsten Bylicki | BylickiLabs  

---

## 1. Purpose of this Security Policy

This Security Policy describes the responsible handling of security reports, vulnerabilities, confidential technical information, and security-related contributions to BylickiLabs Web Security Inspector.

It defines:

- which versions are supported
- which types of security issues should be reported
- which information a report should contain
- how confidential reports must be submitted
- how security reports are reviewed and handled
- which rules apply to security research and disclosure
- which information must not be published publicly
- which limitations and responsibilities apply to users

This policy is intended to protect the project, its users, the development environment, and potentially affected third parties.

---

## 2. Supported Versions

Security fixes are generally provided for the currently maintained major version.

| Version | Supported |
|---|---|
| 2.0.x | Yes |
| 1.x | No |
| older versions | No |

Unsupported versions are not guaranteed to receive security fixes, bug fixes, or compatibility updates.

Users should always use the latest published version.

---

## 3. Scope

This Security Policy applies to:

- the BylickiLabs Web Security Inspector source code
- the desktop application
- the scan engine
- the user interface
- the SQLite database
- export functions
- report formats
- build scripts
- installation and startup scripts
- GitHub Actions workflows
- configuration files
- optional external API integrations
- repository files
- releases and distributed binaries

The following are outside the scope of this policy:

- third-party systems assessed with the application
- external services and platforms
- third-party libraries outside the direct control of the project
- operating systems and local security configurations of users
- networks or servers not operated by BylickiLabs

Security issues in third-party components may still be reported if they directly affect the project.

---

## 4. Security Issues That Should Be Reported

The following types of security issues are particularly relevant:

- unintended disclosure of sensitive data
- unprotected storage of credentials or API keys
- insecure processing of configuration data
- vulnerabilities in the local database
- SQL injection within the application
- path traversal vulnerabilities
- insecure file handling
- uncontrolled file write operations
- insufficient input validation
- server-side request forgery within the scan engine
- insecure URL handling
- missing restrictions for target addresses
- unintended access to local or internal resources
- insecure processing of HTML or report data
- cross-site scripting in generated HTML reports
- code injection
- command injection
- insecure use of external processes
- manipulation of build or installation scripts
- insecure update or release artifacts
- incorrect permissions
- insufficient separation of security-relevant components
- insecure logging
- disclosure of confidential scan results
- unprotected export files
- insecure deserialization
- vulnerabilities introduced by third-party libraries
- manipulation of risk scores or finding data
- security-relevant errors in the internationalized user interface
- methods of bypassing intended safeguards

Reproducible crashes or denial-of-service conditions may also be security-relevant if they can be triggered through crafted input or manipulated target systems.

---

## 5. Issues That Do Not Require a Confidential Security Report

The following topics can generally be submitted as regular GitHub issues:

- display errors
- translation errors
- spelling mistakes
- general feature requests
- non-security-related performance problems
- usage questions
- installation problems
- missing documentation
- known limitations of third-party APIs
- incomplete or incorrect scan results without security impact
- false positives
- false negatives
- minor errors in charts or statistics
- non-confidential build problems

If it is unclear whether an issue is security-relevant, it should first be reported confidentially.

---

## 6. Confidential Vulnerability Reporting

Security vulnerabilities must not be published as public GitHub issues, discussions, pull requests, comments, or social media posts.

Confidential reports must be submitted using the contact method listed on the BylickiLabs GitHub profile.

**GitHub profile:**  
https://github.com/bylickilabs

**Project repository:**  
https://github.com/bylickilabs/BylickiLabs-Web-Security-Inspector

The report should be clearly identified as a security report.

Recommended subject:

```text
Security Report: BylickiLabs Web Security Inspector
```

There is no entitlement to a specific contact method, response time, or processing deadline.

---

## 7. Required Information in a Security Report

A complete report should include, where possible:

- name or identifier of the reporting person
- preferred contact method
- affected version
- affected file or component
- operating system and environment
- clear technical description
- prerequisites for reproduction
- exact reproduction steps
- expected behavior
- actual observed behavior
- potential impact
- severity assessment
- available logs
- error messages
- screenshots
- proof of concept without destructive payloads
- possible mitigation
- known workarounds
- information on whether the vulnerability has already been published
- information on whether third parties are affected
- information on whether sensitive data was accessed

Incomplete reports may still be reviewed if the issue is described clearly enough to understand.

---

## 8. Prohibited Content in Security Reports

The following content must not be transmitted unnecessarily:

- real credentials
- production API keys
- private keys
- complete personal data records
- data belonging to uninvolved third parties
- confidential third-party documents
- malware
- ransomware
- destructive exploits
- automated attack tools
- instructions for unauthorized attacks
- information not required to validate the report

Where evidence contains sensitive data, it must be redacted or anonymized where possible.

---

## 9. Responsible Security Research

Security research related to this project must be conducted responsibly, in a controlled manner, and lawfully.

Permitted activities include:

- testing systems owned by the researcher
- testing in a personal laboratory environment
- testing explicitly authorized target systems
- static code analysis
- local analysis of the source code
- safe reproduction in isolated environments
- non-destructive proofs of concept
- dependency analysis
- analysis of published build artifacts

The following activities are not permitted:

- unauthorized testing of third-party systems
- access to third-party data
- disruption of production services
- denial-of-service attacks
- social engineering
- phishing
- manipulation of third-party accounts
- bypassing authentication
- permanent modification of data
- publication of confidential information
- exploitation beyond what is necessary to confirm the issue

The person conducting the research is responsible for legality, authorization, target systems, and the consequences of testing.

---

## 10. Safe Harbor Principles

BylickiLabs does not intend to pursue legal action against persons who:

- act in good faith
- test only their own or explicitly authorized systems
- comply with this Security Policy
- do not damage or modify data
- do not unnecessarily access personal or confidential information
- do not disrupt services
- report the vulnerability confidentially
- allow reasonable time for review and remediation
- do not use extortion or coercion

This statement is not a legal guarantee, contract, or general authorization for security testing.

It does not apply to testing third-party systems, violations of law, breaches of contract, or actions outside the control of BylickiLabs.

---

## 11. Handling Incoming Security Reports

After a security report is received, the following steps may be taken:

1. record receipt of the report
2. review plausibility
3. identify the affected version
4. assess reproducibility
5. evaluate impact
6. determine severity
7. review existing safeguards
8. develop a fix or workaround
9. perform testing
10. prepare a release or patch
11. coordinate disclosure
12. close the report

Not every report automatically results in a change.

A report may be closed if:

- the behavior is intentional
- there is no security impact
- the issue cannot be reproduced
- the affected version is unsupported
- the root cause lies in a third-party component
- required information is missing
- the issue is already known
- the report violates this policy

---

## 12. Response and Processing Times

Security reports will be reviewed as promptly as reasonably possible.

No binding deadlines are guaranteed.

Processing time depends on factors including:

- completeness of the report
- reproducibility
- technical scope
- potential impact
- availability of the project maintainer
- dependency on third parties
- required testing effort
- release planning requirements

Critical issues are generally prioritized over minor or theoretical risks.

---

## 13. Severity Classification

The following levels may be used for assessment:

| Level | Description |
|---|---|
| Critical | immediate risk to sensitive data, code execution, or complete compromise |
| High | significant security impact with a realistic attack path |
| Medium | relevant vulnerability requiring additional conditions or having limited impact |
| Low | low risk, restricted attack path, or hardening recommendation |
| Informational | technical note without immediate security impact |

CVSS, CWE, OWASP, or comparable standards may be used for additional classification.

The final assessment is determined by the project maintainer.

---

## 14. Coordinated Disclosure

Security issues should be disclosed in a coordinated manner and only after appropriate review.

Publication before a fix is available may expose users to unnecessary risk.

The following is therefore expected:

- confidential initial reporting
- coordination of technical details
- reasonable time for analysis and remediation
- no publication of working exploits before a patch
- no disclosure of confidential information to third parties
- coordination of any possible public acknowledgment

The timing and scope of public disclosure are determined by the project maintainer.

---

## 15. Recognition of Security Reports

Public acknowledgment of reporting persons may be provided at the discretion of the project maintainer.

Possible requirements include:

- responsible reporting
- compliance with this Security Policy
- verifiable technical information
- no prior uncoordinated disclosure
- consent to public attribution

There is no entitlement to:

- public acknowledgment
- compensation
- rewards
- bug bounty payments
- certificates
- references
- prioritization
- implementation of a proposed fix

The project does not operate a public bug bounty program.

---

## 16. Security Updates and Releases

Security fixes may be provided as:

- patch release
- minor release
- updated binary
- corrected build script
- updated dependency
- configuration change
- documented workaround
- security notice in the repository
- GitHub Security Advisory

A security update may modify functionality, settings, data formats, or dependencies.

Users should review and install new releases promptly.

---

## 17. Release Integrity

Official releases are published exclusively through the project repository:

https://github.com/bylickilabs/BylickiLabs-Web-Security-Inspector

Users should:

- obtain releases only from official sources
- verify checksums where available
- avoid modified binaries from unknown sources
- keep local security software active
- review build scripts before execution
- avoid installing unknown dependencies without review
- read release notes

BylickiLabs is not responsible for modified, unofficial, or third-party versions.

---

## 18. Dependencies and Third-Party Components

The project uses several third-party libraries.

These may include:

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

Security issues in third-party components should also be reported to the respective upstream project where possible.

The project may update, replace, restrict, or remove affected dependencies.

Complete freedom from defects in third-party components cannot be guaranteed.

---

## 19. External APIs and Services

The application may use optional external services.

These may include:

- Google PageSpeed Insights
- MDN HTTP Observatory

When enabled, target addresses and technically required information may be transmitted to the selected service.

Users are responsible for:

- enabling external services
- reviewing their privacy terms
- storing API keys securely
- complying with usage limits
- avoiding accidental transmission of confidential targets

Security issues affecting an external service are outside the direct responsibility of the project.

---

## 20. Protection of API Keys and Credentials

API keys and credentials must not:

- be published in issues
- be included in pull requests
- be embedded in source code
- be visible in screenshots
- appear as real values in example configurations
- be stored in logs
- be included in exported reports
- remain in commit history

If a key is accidentally published, it must be revoked and replaced immediately.

Removing it from the current file is not sufficient if it remains in Git history.

---

## 21. Database and File Security

The application uses a local SQLite database and local configuration files.

Users should:

- protect the project directory
- configure appropriate file permissions
- avoid storing sensitive reports publicly
- encrypt backups
- delete unnecessary scan data
- avoid transferring confidential results to public repositories
- review export files before sharing
- secure local user accounts

The application does not guarantee complete encryption of all local data.

---

## 22. Report Security

Exported reports may contain sensitive technical information.

This may include:

- target addresses
- server information
- security headers
- certificate data
- DNS information
- vulnerabilities
- technical evidence
- internal paths
- risk assessments
- recommendations

Reports must be handled according to their confidentiality.

They must not be published or shared with unauthorized third parties.

---

## 23. Logging and Error Data

Logs and error messages may contain technical details.

Before publication, the following information should be removed:

- usernames
- local paths
- internal hostnames
- IP addresses
- credentials
- API keys
- personal data
- confidential target addresses
- complete response content

Only information required for troubleshooting should be shared.

---

## 24. Security-Related Pull Requests

Pull requests addressing an unpublished security vulnerability must not be submitted publicly without prior coordination.

A confidential security report is required first.

A security-related pull request should:

- clearly describe the root cause
- avoid sensitive exploit details
- include tests for the fix
- avoid unnecessary changes to existing functionality
- consider backward compatibility
- document security-relevant side effects

Acceptance of a pull request is solely at the discretion of the project maintainer.

---

## 25. Automated Scanners and Analysis Tools

Automated scanners may be used to analyze the source code or personal test environments.

Results from automated tools must be manually reviewed before reporting.

The following are not welcome:

- unreviewed mass reports
- automatically generated issues without technical assessment
- duplicates
- version warnings without actual impact
- misleading severity ratings
- incomplete scanner output without context

Quality and traceability are more important than the number of reported findings.

---

## 26. Security-Relevant Changes

Changes with potential security impact require additional review.

This particularly includes changes to:

- URL validation
- network access
- file system access
- export functions
- HTML generation
- database queries
- configuration
- API keys
- external processes
- build scripts
- installation routines
- dependencies
- logging
- risk scoring
- permissions

Such changes should be accompanied by tests and a verifiable technical explanation.

---

## 27. Security Limitations of the Application

BylickiLabs Web Security Inspector is an analysis tool and cannot guarantee complete security.

The application may:

- miss vulnerabilities
- generate false positives
- evaluate configurations incompletely
- fail to fully capture dynamic content
- be limited by protective mechanisms
- depend on third-party APIs
- produce time-dependent results
- not replace a complete manual security assessment

Results must always be evaluated professionally.

---

## 28. User Responsibilities

Users are responsible for:

- selecting the target system
- obtaining legal authorization
- determining the assessment scope
- controlling load on the target system
- protecting results
- secure storage
- evaluating findings
- implementing measures
- updating the application
- complying with internal policies
- complying with legal requirements

Use of the application is at the user's own risk.

---

## 29. Changes to this Security Policy

This Security Policy may be amended if any of the following change:

- project scope
- supported versions
- technical architecture
- contact methods
- legal requirements
- external services
- release processes
- security requirements

The current version will be published in the repository.

---

## 30. Contact

**Project maintainer:**  
Thorsten Bylicki | BylickiLabs

**GitHub profile:**  
https://github.com/bylickilabs

**Project repository:**  
https://github.com/bylickilabs/BylickiLabs-Web-Security-Inspector

Confidential security reports must be submitted through the contact method listed on the GitHub profile.

Security vulnerabilities must not be published as public issues.

---

## 31. Final Provision

This Security Policy is intended to ensure responsible, transparent, and coordinated handling of security issues.

Confidential disclosure, technical precision, and protection of affected users take precedence over public attention or rapid publication.

---

Copyright © 2026 Thorsten Bylicki | BylickiLabs.  
All rights reserved.
