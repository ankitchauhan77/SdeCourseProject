import requests
import lxml.html
import sys
import json
import requests

search_term = "refactoring"
page_no = 5

for page in range(1,page_no+1):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Origin": "https://ieeexplore.ieee.org",
        "Content-Type": "application/json",
    }
    payload = {
        "newsearch": True,
        "queryText": search_term,
        "highlight": True,
        "returnFacets": ["ALL"],
        "returnType": "SEARCH",
        "pageNumber": page_no
    }
    r = requests.post(
            "https://ieeexplore.ieee.org/rest/search",
            json=payload,
            headers=headers
        )
    page_data = r.json()
    tot = 0
    for record in page_data["records"]:
        tot += 1
    print("Total", tot, " articles found on IEEE:\n")
    for record in page_data["records"]:
        print(record["articleTitle"])
        print('https://ieeexplore.ieee.org'+record["documentLink"], end="\n----\n")
    print()
    print("End of page", page)
    print("----------------------------------------------------------------------")

