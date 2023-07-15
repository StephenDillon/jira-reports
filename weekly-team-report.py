import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://agile-reporting.atlassian.net/rest/api/3/search"

auth = HTTPBasicAuth("EMAIL", "KEY")

headers = {
  "Accept": "application/json"
}

query = {
  'query': 'query'
}

body={
  "expand": [
    "changelog"
  ],
  "fields": [
    "summary",
    "status",
    "assignee"
  ],
  "fieldsByKeys": "false",
  "jql": "status != Closed and project = \"Test Project\"",
  "maxResults": 15,
  "startAt": 0
}


response = requests.request(
   "POST",
   url,
   headers=headers,
   params=query,
   auth=auth, 
   json=body
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

# issues = json.loads(response.text)["issues"]
# for issue in issues:
#   print(issue)