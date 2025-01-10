# Simple Safe Links Decoder for Python3
# 0.6 / 10.1.2025 / Joukahainen123

import subprocess
from urllib import parse

def normalize_atpsafelink(safelink_url):
    """Normalize and extract the original URL from SafeLink wrapper."""
    try:
        # Extract and decode the URL
        if "=" in safelink_url:
            safelink_url = parse.unquote(safelink_url.split("=")[1])
            # Only remove '&data' if it's at the end of the URL
            if safelink_url.endswith("&data"):
                safelink_url = safelink_url.split('&data')[0]
            return safelink_url
        print("Invalid Safe Link format.")
        return safelink_url
    except Exception as e:
        print(f"Error: {e}")
        return safelink_url

def toggle_canonic_mode(enable=True):
    """Toggle between canonical and non-canonical modes."""
    mode = 'icanon' if enable else '-icanon'
    subprocess.run(['stty', mode, 'echo'], check=True)  # Ensure echo is enabled so input is visible

def main():
    RED, GREEN, END = '\033[91m', '\033[92m', '\033[0m'

    toggle_canonic_mode(enable=False)  # Disable canonical mode for long inputs but keep echo

    try:
        while True:
            safelink = input("Give Safe Link URL (or 'e' to exit): ").strip()
            if safelink.lower() == 'e': break
            if safelink.startswith("https"):
                finalurl = normalize_atpsafelink(safelink)
                print(f"\n{RED}Active, unsanitized link:{END}\n{RED}{finalurl}{END}\n")
                print(f"{GREEN}Sanitized link:{END}\n{GREEN}{finalurl.replace('http', 'hxxp').replace('.', '[.]')}{END}\n")
            else:
                print("Invalid Safe Link. Please provide a valid URL.")
            
            if input("Press ENTER to continue or input 'e' to exit: ").lower() == 'e': break
    finally:
        toggle_canonic_mode(enable=True)  # Restore canonical mode

if __name__ == "__main__":
    main()
