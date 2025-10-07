# Threat Intelligence Aggregator

A Python-based cybersecurity project that scrapes the latest threat intelligence data from public sources like ThreatPost and BleepingComputer. 

### 🔍 Features
- Pulls latest security news from ThreatPost (RSS) and BleepingComputer (HTML)
- Displays top headlines and links
- Extensible to add more sources (e.g., CVE feeds, malware IOCs)

---

### 🚀 How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/YOUR_USERNAME/threat-intel-aggregator.git
   cd threat-intel-aggregator

2. Install dependencies:
    pip install -r requirements.txt

3. Run the aggregator:
    python aggregator.py

### 📈 Example Output

=== Today's Threat Intelligence ===

[ThreatPost]
[July 11, 2025] New Exploit Targets Apache - https://threatpost.com/example-link
...

[BleepingComputer]
Ransomware attack hits US hospitals - https://bleepingcomputer.com/example
...