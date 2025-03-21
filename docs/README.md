# Netra

<p align="center">
  <img src="/docs/images/netra-logo.png">
</p>

<p align="center">
  <b>An IP lookup tool that returns detailed geographic and network data for any IP address with ease</b>
</p>

<p align="center">
  <a href="#installation">Installation</a>
  &nbsp;&nbsp;&nbsp;•&nbsp;&nbsp;&nbsp;
  <a href="#usage">Usage</a>
  &nbsp;&nbsp;&nbsp;•&nbsp;&nbsp;&nbsp;
</p>

<br><br>


<p align="center">
  <img src="/docs/images/demo.png">


---

### Installation

**Clone the repository**

```bash
git clone https://github.com/nativevoid/Netra
cd Netra
```

**Install requirements**

```bash
pip install -r requirements.txt
```

### Usage

**Lookup an IP address**

```bash
python netra.py --target 178.157.253.24
```

**Export results to a .txt or .md file**

```bash
python netra.py --target 178.157.253.24 --output test.txt
```

```bash
python netra.py --target 178.157.253.24 --output test.md
```

&nbsp;
```console


$$\   $$\            $$\
$$$\  $$ |           $$ |
$$$$\ $$ | $$$$$$\ $$$$$$\    $$$$$$\  $$$$$$\
$$ $$\$$ |$$  __$$\_$$  _|  $$  __$$\ \____$$\
$$ \$$$$ |$$$$$$$$ | $$ |    $$ |  \__|$$$$$$$ |
$$ |\$$$ |$$   ____| $$ |$$\ $$ |     $$  __$$ |
$$ | \$$ |\$$$$$$$\  \$$$$  |$$ |     \$$$$$$$ |
\__|  \__| \_______|  \____/ \__|      \_______|



===============================================================================================
usage: netra.py [-h] [--version] -trg TARGET [-o OUTPUT]

Netra: A tool for IP lookup and network information gathering (Version: 0.1.0)

options:
  -h, --help            show this help message and exit
  --version             Display version information.
  -trg, --target TARGET
                        IP address for location and network info lookup.
  -o, --output OUTPUT   Output file to save results (.txt or .md only).
```

<br>

### Feature Requests & Bug Reporting

Want to suggest a new feature? Open a request using our [Feature Request Template](../.github/ISSUE_TEMPLATE/feature-request.yaml).

Found a bug? Report it using our [Bug Report Template](../.github/ISSUE_TEMPLATE/bug-report.yaml).

<br>

### Disclaimer

This tool is for educational purposes only and is intended to help with IP lookups. Users are responsible for complying with applicable laws.

By using this tool, you accept all risks associated with its use. Nativevoid is not liable for any consequences resulting from using this tool.


