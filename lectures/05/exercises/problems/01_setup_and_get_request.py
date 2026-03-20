"""Problem 01 (merged): setup + first GET request.

Install dependencies (once):
    pip install requests fastapi uvicorn

Task:
1. Send a GET request to https://jsonplaceholder.typicode.com/todos/1
2. Print:
   - status code
   - Content-Type header
   - raw body (response.text)
   - parsed JSON (response.json())
3. Read and print: id, title, completed
4. Add error handling with raise_for_status()

Expected result:
- You can explain the difference between raw text and parsed JSON.
"""

import requests

URL = "https://jsonplaceholder.typicode.com/todos/1"

def main() -> None:
    try:
        response = requests.get(URL)
        response.raise_for_status()

        print(response.status_code)
        print(response.headers.get("Content-Type"))
        print(response.text)

        data = response.json()
        print(data)

        print(data["id"])
        print(data["title"])
        print(data["completed"])

    except requests.exceptions.RequestException as e:
        print(e)


if __name__ == "__main__":
    main()
    