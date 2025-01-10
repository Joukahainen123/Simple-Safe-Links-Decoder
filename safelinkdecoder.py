# Simple Safe Links Decoder for Python3
# 0.5 / 10.1.2025 / Joukahainen123

from urllib import parse 
def normalize_atpsafelink(safelink_url):
    """
    Normalize and extract original URL from SafeLink wrapper.
    """
    try:
        # Validate if URL has the expected structure
        if "=" not in safelink_url:
            print("Invalid Safe Link format. Please provide a proper Safe Link URL.")
            return safelink_url
        # Extract and decode URL
        safelink_url = safelink_url.split("=")[1]
        safelink_url = parse.unquote(safelink_url)
        # Remove SafeLink tracking parameters
        safelink_url = safelink_url.split('&data=')[0].split('&amp')[0]
        return safelink_url
    except Exception as e:
        print(f"Error normalizing Safe Link: {e}")
        return safelink_url
def main():
    RED = '\033[91m'
    END = '\033[0m'
    GREEN = '\033[92m'
    while True:
        safelink = input("Give Safe Link URL (or 'e' to exit): ").strip()
        if safelink.lower() == 'e':
            print("Thanks and goodbye.")
            break
        if not safelink:
            print("Input cannot be empty. Please provide a Safe Link URL.")
            continue
        if not safelink.startswith("https"):
            print("URL must start with 'https'. Please provide a valid Safe Link URL.")
            continue
        finalurl = normalize_atpsafelink(safelink)
        print(f"\n{RED}Active, unsanitized link:{END}\n{RED}{finalurl}{END}\n")
        print(f"{GREEN}Sanitized link:{END}\n{GREEN}{finalurl.replace('http', 'hxxp').replace('.', '[.]')}{END}\n")
        exit_input = input("Press ENTER to continue or input 'e' to exit: ")
        if exit_input.lower() == 'e':
            print("Thanks and goodbye.")
            break
if __name__ == "__main__":
    main()
 