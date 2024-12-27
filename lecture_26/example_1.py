import requests

# Send a GET request to Google
response = requests.get("https://www.google.com", headers={"X-Test": "true"})

# Print request details
print("Request Details:")
print(f"Request URL: {response.request.url}")
print(f"Request Headers: {response.request.headers}")

# Print response details
print("\nResponse Details:")
print(f"URL: {response.url}")
print(f"Status Code: {response.status_code}")
print(f"Headers: {response.headers}")
print(f"Body:\n{response.text[:500]}...")  # Print first 500 characters of the body


