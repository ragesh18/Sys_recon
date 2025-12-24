import platform
import os
import subprocess
import sys

def get_os_info():
    """Collect OS name, version, and platform information."""
    print("OS Information:")
    print(f"System: {platform.system()}")
    print(f"Node Name: {platform.node()}")
    print(f"Release: {platform.release()}")
    print(f"Version: {platform.version()}")
    print(f"Platform: {platform.platform()}")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor()}")
    print(f"Architecture: {platform.architecture()}")
    print(f"OS Name: {platform.system()} {platform.release()}")
    print("-" * 50)

def get_kernel_info():
    """Collect kernel version and related details."""
    print("Kernel Information:")
    try:
        
        if platform.system() == "Linux":
            result = subprocess.run(['uname', '-a'], capture_output=True, text=True)
            print(f"Kernel: {result.stdout.strip()}")
        elif platform.system() == "Darwin":
            result = subprocess.run(['uname', '-a'], capture_output=True, text=True)
            print(f"Kernel: {result.stdout.strip()}")
        else:
            print("Kernel info not available on this platform.")
    except Exception as e:
        print(f"Error retrieving kernel info: {e}")
    print("-" * 50)

def get_user_privileges():
    """Check current user privileges."""
    print("User Privileges:")
    try:
        if platform.system() == "Windows":
            # Use Windows-specific method
            import ctypes
            if ctypes.windll.shell32.IsUserAnAdmin():
                print("User has administrative privileges.")
            else:
                print("User does not have administrative privileges.")
        else:
            uid = os.getuid()
            if uid == 0:
                print("User has root privileges.")
            else:
                print(f"User UID: {uid}, not root.")
    except Exception as e:
        print(f"Error checking privileges: {e}")
    print("-" * 50)

def get_installed_security_tools():
    """Check for installed security tools and EDR hints."""
    print("Installed Security Tools & EDR Hints:")
    
    edr_tools = [
        "SentinelOne", "CrowdStrike", "Microsoft Defender", "Symantec", 
        "McAfee", "Bitdefender", "Trend Micro", "FireEye", "Carbon Black"
    ]
    
    security_bins = [
        "avast", "clamav", "chkrootkit", "rkhunter", "tripwire", "osquery",
        "sysmon", "wmi", "ps", "lsof", "netstat", "ss", "iptables", "ufw"
    ]

    
    for tool in edr_tools:
        try:
            result = subprocess.run(['which', tool], capture_output=True, text=True)
            if result.returncode == 0:
                print(f"EDR/Security Tool Found: {tool}")
        except Exception:
            pass

    
    for bin_name in security_bins:
        try:
            result = subprocess.run(['which', bin_name], capture_output=True, text=True)
            if result.returncode == 0:
                print(f"Security Binary Found: {bin_name}")
        except Exception:
            pass

    
    if platform.system() == "Linux":
        
        try:
            result = subprocess.run(['ps', 'aux'], capture_output=True, text=True)
            output = result.stdout
            for tool in edr_tools:
                if tool.lower() in output.lower():
                    print(f"EDR Process Detected: {tool}")
        except Exception:
            pass

        
        edr_paths = [
            "/opt/sentinelone", "/opt/crowdstrike", "/opt/microsoft/defender",
            "/etc/sentinelone", "/etc/crowdstrike", "/etc/defender"
        ]
        for path in edr_paths:
            if os.path.exists(path):
                print(f"EDR Configuration Path Found: {path}")

    elif platform.system() == "Darwin":
       
        edr_paths = [
            "/Library/SentinelOne", "/Library/CrowdStrike", "/Library/Defender"
        ]
        for path in edr_paths:
            if os.path.exists(path):
                print(f"EDR Configuration Path Found: {path}")

    elif platform.system() == "Windows":
        
        try:
            
            result = subprocess.run(['sc', 'query'], capture_output=True, text=True)
            output = result.stdout
            for tool in edr_tools:
                if tool.lower() in output.lower():
                    print(f"EDR Service Detected: {tool}")
        except Exception:
            pass

        
        registry_keys = [
            "HKLM\\SOFTWARE\\SentinelOne",
            "HKLM\\SOFTWARE\\CrowdStrike",
            "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Microsoft Defender Antivirus"
        ]
        for key in registry_keys:
            try:
                result = subprocess.run(['reg', 'query', key], capture_output=True, text=True)
                if result.returncode == 0:
                    print(f"EDR Registry Key Found: {key}")
            except Exception:
                pass

    print("-" * 50)

def main():
    """Main function to run all collection functions."""
    print("System Information Collection Script")
    print("=" * 60)
    get_os_info()
    get_kernel_info()
    get_user_privileges()
    get_installed_security_tools()
    print("Collection complete.")

if __name__ == "__main__":
    main()   
