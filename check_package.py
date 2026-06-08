import requests

def check_package(package_name):
    url = f"https://play.google.com/store/apps/details?id={package_name}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    try:
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code == 200:
            return True, "Package exists"
        elif r.status_code == 404:
            return False, "Package not found"
        else:
            return False, f"Unexpected status: {r.status_code}"
    except requests.exceptions.RequestException as e:
        return False, f"Error: {e}"

# Test it
packages = ["com.zezo.pingme.user"]

for pkg in packages:
    found, msg = check_package(pkg)
    print(f"{pkg}: {msg}")
