import requests
import json

# Set the target URL
url = "http://example.com"

# Set the API endpoint and API key for a vulnerability scanner
api_endpoint = "https://scanner.example.com/scan"
api_key = "your_api_key"

# Set the headers for the API request
headers = {
  "Content-Type": "application/json",
  "Authorization": "Bearer {}".format(api_key)
}

# Set the data for the API request
data = {
  "url": url
}

# Send the API request to start the scan
response = requests.post(api_endpoint, headers=headers, data=json.dumps(data))

# Check the status code of the response
if response.status_code == 200:
  # Print the scan ID
  scan_id = response.json()["scan_id"]
  print("Scan started successfully. Scan ID:", scan_id)
else:
  # Print the error message
  print("Error starting scan:", response.json()["error"])
