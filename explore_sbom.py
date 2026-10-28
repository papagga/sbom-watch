import json
import httpx

def ask_osv(name, version, purl):
    print("Библиотека", name, "с версией", version, "имеет следующие уязвимости:")
    print()
    body = {"package": {"purl": purl}}
    response = httpx.post("https://api.osv.dev/v1/query", json=body, timeout=10)
    answer = response.json()

    for i in answer["vulns"]:
        i1 = i["id"]
        i2 = i["aliases"]
        print(f"id={i1}")
        print(f"aliases={i2}")
        print()


with open("sbom.json", encoding="utf-8") as f:
    data = json.load(f)

for i in data.keys():
    if i == "components":
        l = len(data[i])
        for j in range(l):
            ask_osv(data[i][j]["name"], data[i][j]["version"], data[i][j]["purl"])