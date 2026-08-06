<div align="center">

|<img src="assets/bwsi.png" alt="BylickiLabs Web Security Inspector" width="1280" height="960">|
|---|

# BylickiLabs Web Security Inspector

### Enterprise Website Security Analytics

|bilingual|desktop|application for structured website|configuration|performance|security analyses|
|---|---|---|---|---|---|

| [![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)](https://github.com/bylickilabs/BylickiLabs-Web-Security-Inspector) | [![Python](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/) | 
|---|---|

| [![PySide6](https://img.shields.io/badge/UI-PySide6-green.svg)](https://doc.qt.io/qtforpython-6/) | [![NumPy](https://img.shields.io/badge/Analytics-NumPy-blue.svg)](https://numpy.org/) |  [![SciPy](https://img.shields.io/badge/Statistics-SciPy-blue.svg)](https://scipy.org/) |
|---|---|---|

| [![Matplotlib](https://img.shields.io/badge/Charts-Matplotlib-orange.svg)](https://matplotlib.org/) | [![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)](https://www.microsoft.com/windows) | ![License](https://img.shields.io/badge/License-All%20Rights%20Reserved-red.svg) |
|---|---|---|

</div>

<br>

---

<br>

## Overview

> The **BylickiLabs Web Security Inspector 2.0.0** is a completely newly developed desktop application for the structured analysis of websites, domains, and web-based services.

> The application combines technical testing procedures with a professional user interface, a consistent risk model, local scan history, statistical evaluations, and exportable reports.

> The focus is on a transparent and centralized assessment of security-relevant configurations. Results are not only recorded, but also classified by severity, category, and confidence level, statistically evaluated, and clearly visualized.

> The application is fully usable in **German and English**.

<br>

---

<br>

## Core Features

### Professional User Interface

> The application is divided into clearly separated work areas:

- **Dashboard** with central key figures and overall assessment
- **Scan Center** for configuring and performing analyses
- **Findings** with search, filtering, and detailed view
- **Statistics** with numerical evaluations and charts
- **History** for previous analyses and historical comparisons
- **Log** for technical status and error messages
- **Settings** for language, timeouts, measurements, and optional services
- **About Dialog** with complete application information
- **GitHub Button** with a direct link to the BylickiLabs profile

### Dashboard

> After an analysis is completed, the dashboard displays, among other things:
  - risk score from 0 to 100
  - security rating
  - total number of findings
  - number of checks performed
  - average response time
  - total scan duration
  - severity distribution
  - categories of detected findings
  - technical summary of the current scan

<br>

---

<br>

## Scan Profiles

| Profile | Description |
|---|---|
| **Quick** | Fast check of central HTTP, TLS, DNS, content, and performance characteristics |
| **Standard** | Extended check including CORS, HTTP methods, and additional configuration analyses |
| **Extended** | Comprehensive profile with additional resource, deployment, and detailed checks |

> The profiles allow controlled adjustment of the scope of testing to the target system, time requirements, and analysis purpose.

<br>

---

<br>

## Integrated Testing Areas

### HTTP and Transport

- HTTP status codes
- redirect chains
- HTTP version
- response size
- response times
- server information
- transport encryption
- HTTPS usage
- technical response characteristics

### HTTP Security Headers

- Content Security Policy
- Strict Transport Security
- X-Content-Type-Options
- X-Frame-Options
- Referrer Policy
- Permissions Policy
- Cross-Origin-Opener-Policy
- Cross-Origin-Resource-Policy
- Cross-Origin-Embedder-Policy
- protection against MIME sniffing
- frame protection
- policy quality and configuration notes

### Cookies

- Secure
- HttpOnly
- SameSite
- cookie lifetimes
- cookie configurations
- security-relevant deviations
- detected session and tracking properties

### CORS

- Access-Control-Allow-Origin
- reflected origin values
- wildcard configurations
- credential combinations
- security-relevant cross-origin settings

### Forms

- form methods
- target addresses
- HTTPS transmission
- password fields
- external form targets
- visible token indicators
- possible CSRF protection characteristics
- unusual input configurations

### Content and Resources

- Mixed Content
- external resources
- external domains
- HTML comments
- generator metadata
- JavaScript library indicators
- publicly accessible standard resources
- typical deployment artifacts
- robots.txt
- sitemap.xml
- security.txt

### TLS and Certificates

- certificate validity
- remaining validity period
- issuer
- Subject Alternative Names
- TLS protocol used
- Cipher Suite
- certificate information
- hostname and certificate relationship
- basic transport assessment

### DNS and Mail Security

- A Records
- AAAA Records
- MX Records
- NS Records
- TXT Records
- CAA Records
- SPF
- DMARC
- mail security configuration
- name server and domain information

### HTTP Methods

- available HTTP methods
- OPTIONS evaluation
- TRACE behavior
- unusual or unnecessary method permissions
- server-side method configuration

### Performance

- multiple response time measurements
- mean values
- median
- percentiles
- fluctuations
- outliers
- time-based progression of measured values

<br>

---

<br>

## Statistics with NumPy and SciPy

> The statistics area processes scan results and measurement series with **NumPy** and **SciPy**.

### NumPy

> NumPy is used, among other things, for:
  - numerical data series
  - mean calculation
  - median calculation
  - standard deviation
  - percentiles
  - risk weighting
  - aggregated key figures
  - vectorized evaluations
  - preparation of chart data

### SciPy

> SciPy extends the analysis with:
  - Shannon entropy
  - linear regression
  - trend calculations
  - skewness of distributions
  - Z-score-based outlier detection
  - statistical evaluation of historical measurement series
  - advanced distribution and relationship analyses

### Matplotlib

> The results are visualized directly in the application:
  - severity distribution
  - findings by category
  - response time progression
  - historical risk development
  - comparison of previous scans
  - statistical trends

<br>

---

<br>

## Risk Model

> Each finding is classified based on several characteristics:
  - severity
  - confidence level
  - category
  - technical evidence
  - affected address
  - description
  - recommended action
  - optional CWE mapping
  - scanner source

Severity levels used:

| Severity | Meaning |
|---|---|
| **Critical** | Very high risk requiring immediate action |
| **High** | Significant risk with high priority |
| **Medium** | Relevant finding requiring assessment |
| **Low** | Lower risk or optimization potential |
| **Info** | Technical note without immediate risk rating |

> The overall score summarizes the weighted results into a consistent assessment. The score is intended for prioritization and does not replace a manual professional review.

<br>

---

<br>

## Scan History and SQLite

> Completed analyses can be stored locally in an SQLite database.
  - This provides the following functions:
    - loading previous results
    - redisplaying all findings
    - historical risk trends
    - statistical comparisons
    - development of ratings over time
    - deleting individual entries
    - completely clearing the history
    - optionally disabling local storage

> The local data is stored by default within the project directory:

```text
data/scan_history.sqlite3
```

> Application settings are stored locally:

```text
data/settings.json
```

<br>

---

<br>

## Reports and Exports

> Scan results can be exported in several formats:

| Format | Intended Use |
|---|---|
| **JSON** | Complete structured data for further processing and archiving |
| **HTML** | Standalone browser-based business report |
| **CSV** | Table-based analysis and import into office or BI tools |
| **PDF** | Management overview, archiving, and distribution |
| **SARIF 2.1.0** | Integration into security, development, and CI platforms |

> Depending on the format, the reports contain:
  - target address
  - scan time
  - risk score
  - overall assessment
  - scan profile
  - key figures
  - response times
  - severity distribution
  - complete list of findings
  - technical evidence
  - recommendations
  - categories and references

> Exported reports are stored by default in the `reports` directory.

<br>

---

<br>

## Optional External Services

> External integrations are disabled by default and can be enabled within the settings.

### Google PageSpeed Insights

> The integration can provide additional Lighthouse categories:
  - Performance
  - Accessibility
  - Best Practices
  - SEO

> A personal API key can be stored for more frequent requests.

### MDN HTTP Observatory

> The Observatory integration supplements the local analysis with an external assessment of security-relevant HTTP configurations.
  - When external services are enabled, the target information required for the respective analysis is transmitted to the selected service.

<br>

---

<br>

## System Requirements

### Recommended Platform

- Windows 10 or Windows 11
- 64-bit system
- at least 4 GB of memory
- internet access for public targets and external APIs
- Python 3.11 or newer when using the source code

### Main Components Used

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

## Installation on Windows

### Automatic Installation

1. Download the repository or extract the ZIP archive.
2. Run `INSTALL.bat`.
3. Wait until the virtual environment and all dependencies have been set up.
4. Run `START.bat`.

> The installation automatically creates a virtual Python environment in the `.venv` directory.

### Installation via Command Prompt

```bat
INSTALL.bat
START.bat
```

### Installation via the Prepared Scripts

```bat
scripts\setup.cmd
scripts\run.cmd
```

### Manual Installation

```powershell
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe main.py
```

<br>

---

<br>

## Start the Application

> After the one-time installation:

```bat
START.bat
```

> Alternatively:

```bat
scripts\run.cmd
```

> Or directly through the virtual environment:

```powershell
.\.venv\Scripts\python.exe main.py
```

<br>

---

<br>

## Perform the First Analysis

1. Start the application.
2. Select the language.
3. Switch to the **Scan Center** area.
4. Enter the complete target address.
5. Select the scan profile.
6. Check the timeout and number of measurements.
7. Start the analysis.
8. Review the results in the dashboard.
9. Filter findings by severity, category, or confidence level.
10. Open statistical evaluations in the statistics area.
11. Export the result as HTML, JSON, CSV, PDF, or SARIF if required.

Example of a valid target address:

```text
https://example.com
```

<br>

---

<br>

## Automatic Windows Build

> The application contains prepared build scripts for automatically creating an executable Windows application.

### Set Up the Development Environment

```bat
scripts\setup_dev.cmd
```

### Start the EXE Build

```bat
scripts\build_exe.cmd
```

> The build process:
  - checks the existing development environment
  - uses the prepared PyInstaller configuration
  - collects required Python modules
  - integrates resources and application icons
  - cleans previous build artifacts
  - compiles the application reproducibly
  - creates an executable Windows version

The result is created here by default:

```text
dist/BylickiLabsWebSecurityInspector/
```

> The compiled version can then be started without a separate Python installation.

<br>

---

<br>

## Quality Assurance

### Install Development Dependencies

```bat
scripts\setup_dev.cmd
```

### Run the Complete Quality Check

```bat
scripts\quality.cmd
```

> The quality run includes:
  - Python syntax check
  - compilation of the Python modules
  - Ruff code analysis
  - automated pytest tests
  - validation of central models
  - scanner tests
  - database tests
  - statistics tests
  - export tests
  - input validation

### Run Tests Directly

```powershell
.\.venv\Scripts\python.exe -m pytest
```

### Run Ruff Directly

```powershell
.\.venv\Scripts\python.exe -m ruff check app tests main.py
```

<br>

---

<br>

## Project Structure

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

## Technical Architecture

> The application has a modular structure.

### User Interface

> The PySide6 interface manages navigation, tables, dialogs, charts, settings, and user interactions.

### Scan Engine

> The central scan engine coordinates:
  - target validation
  - profile selection
  - individual testing modules
  - status messages
  - result aggregation
  - risk calculation
  - statistics
  - database storage

### Scanner Modules

> Each testing area is organized as a separate module. This allows functions to be extended, tested, and maintained without having to restructure the entire application.

### Data Models

> Consistent data models ensure that findings, measured values, scan metadata, and export data are processed consistently.

### Database

> SQLite stores scan histories locally and supports historical evaluations.

### Reporting

> The export component creates structured reports in several formats.

### Internationalization

> Texts and labels are managed centrally so that the interface can be switched completely between German and English.

<br>

---

<br>

## Performance Optimizations

Version 2.0.0 contains several technical optimizations:

- more efficient scan processes
- reduced redundant processing
- optimized result aggregation
- improved database access
- controlled response sizes
- configurable timeouts
- configurable number of measurements
- structured module communication
- optimized chart updates
- more stable export processing
- safer handling of dynamic content
- improved processing of IP targets and DNS edge cases

<br>

---

<br>

## Settings

Within the application, the following can be configured, among other things:

- language
- network timeout
- number of performance measurements
- local storage
- PageSpeed integration
- PageSpeed API key
- MDN Observatory integration
- scan options
- report settings

<br>

---

<br>

## Troubleshooting on Windows

### PowerShell Blocks Scripts

> The CMD and BAT files can be used without changing the PowerShell execution policy:

```bat
INSTALL.bat
START.bat
```

### Virtual Environment Is Missing

> Run the installation again:

```bat
INSTALL.bat
```

### Python Was Not Found

> Install Python 3.11 or newer and enable the **Add Python to PATH** option during installation.
  - Then reopen the command prompt and check:

```bat
py --version
```

or:

```bat
python --version
```

### Application Does Not Start

> Start directly with a visible error message:

```powershell
.\.venv\Scripts\python.exe main.py
```

### Build Script Cannot Find PyInstaller

> Install the development environment:

```bat
scripts\setup_dev.cmd
```

> Then run again:

```bat
scripts\build_exe.cmd
```

### Old Build Files Cause Problems

> The build script uses the `--clean` option and automatically removes outdated temporary PyInstaller data.

<br>

---

<br>

## Data Protection and Local Processing

> The application stores scan histories and settings locally by default.
  - The following data may be processed locally:
    - target address
    - scan time
    - scan profile
    - findings
    - technical evidence
    - response times
    - risk score
    - statistical values
    - exported reports
    - optional API settings

> The local scan history can be disabled.
  - When using external services, their respective data processing terms also apply.

<br>

---

<br>

## Responsible Use

> The application is intended for proprietary systems, proprietary development environments, and explicitly authorized testing targets.

> The respective user is solely responsible for selecting the target system, the scope of testing, the required authorizations, and compliance with legal or organizational requirements.

> Automated results must be reviewed professionally. No scanner can reliably detect every vulnerability or completely exclude false positives.


<br>

---

<br>

## Status

**Version:** 2.0.0  
**Development Status:** Active development and optimization  
**Build Target:** Native Windows application  
**Languages:** German and English

<br>

---

<br>

## License

Copyright © 2026 Thorsten Bylicki | BylickiLabs.
[LICENSE](LICENSE)
