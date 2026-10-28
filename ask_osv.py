# Учебный файл

import httpx

body = {"package": {"purl": "pkg:pypi/requests@2.19.0"}}
response = httpx.post("https://api.osv.dev/v1/query", json=body, timeout=10)
answer = response.json()

for i in answer["vulns"]:
    print("id=", i["id"])
    print("aliases=", i["aliases"])
    print()