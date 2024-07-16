# Simple Safe Links Decoder for Python3
# 0.4 / 16.7.2024 / Joukahainen123

from urllib import parse

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

    RED = '\033[91m'
    END = '\033[0m'
    GREEN = '\033[92m'

    def normalize_atpsafelink(safelink_url):
        safelink_url = safelink_url.split("=")[1]
        safelink_url = parse.unquote(safelink_url)
        safelink_url = safelink_url.split('&amp')[0]
        return safelink_url

    def main(url):
        print()
        finalurl = normalize_atpsafelink(url)[:-5]
        print(RED + "Active, unsanitized link:" + END)
        print()
        print(RED + finalurl + END)
        print()
        print(GREEN + "Sanitized link:" + END)
        print()
        modified_url = finalurl.replace("http", "hxxp").replace(".", "[.]")
        print(GREEN + modified_url + END)
        print()

    main(safelink)

    exit_input = input("Press ENTER to continue or input 'e' to exit: ")
    if exit_input.lower() == 'e':
        print("Thanks and goodbye.")
        break
