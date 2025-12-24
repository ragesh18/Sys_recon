# System Information & Security Recon Script
A cross-platform Python system reconnaissance script used to gather operating system, kernel information, user privilege level verification, as well as the installation of security solutions like EDR tool presence analysis in both Windows, macOS, and Linux operating systems in general.


---

## 🔍 Features

- Collects OS and platform details (system, version, architecture)
- Retrieves kernel information (Linux & macOS)
- Checks current user privilege level (root/admin detection)
- Detects common security tools and EDR solutions
- Supports **Linux**, **macOS**, and **Windows**

---

## 🛠️ Technologies Used

- Python 3
- Standard libraries:
  - `platform`
  - `os`
  - `subprocess`
  - `sys`

No external dependencies required.

---

## 🚀 Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/system-recon-script.git
   cd system-recon-script
2. Run the script
   ```bash
   python3 sys_recon.py
