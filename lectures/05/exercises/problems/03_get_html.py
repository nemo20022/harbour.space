"""Problem 03: GET request for HTML content.

Task:
1. Send GET to https://example.com
2. Print:
   - status code
   - Content-Type header
   - HTML body (response.text)
3. Verify content type contains text/html
4. Add raise_for_status()
"""

import requests

URL = "https://example.com"

def main() -> None:
    try:
        response = requests.get(URL, verify=False)
        response.raise_for_status()

        print(response.status_code)
        content_type = response.headers.get("Content-Type")
        print(content_type)
        print(response.text)

        print("text/html" in content_type)

    except requests.exceptions.RequestException as e:
        print(e)


if __name__ == "__main__":
    main()
    