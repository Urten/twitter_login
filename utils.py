import json

def cookie_cleaner():
    with open("cookies.json") as f:
        raw = json.load(f)

        cookies = {
            c["name"]: c["value"]
            for c in raw
            if "name" in c and "value" in c
        }

        with open("cookies.json", "w") as f:
            json.dump(cookies, f, indent=4)
            
if __name__ == "__main__":
    cookie_cleaner()