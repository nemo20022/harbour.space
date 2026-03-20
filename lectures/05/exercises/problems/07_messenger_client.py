"""Problem 07 (part B): messenger sender client.

Task:
1. Split into pairs
2. Write an infinite loop reading message text from terminal
3. Send each message to partner API endpoint /messages
4. Show send status in terminal


Partner setup:
- Partner gives you ngrok public URL
- You set TARGET_BASE_URL to that URL
"""

import requests

TARGET_BASE_URL = "https://unabsorptive-flatly-erminia.ngrok-free.dev"
SENDER_NAME = "nemo"

def main() -> None:
    while True:
        try:
            text = input("> ")
            payload = {
                "sender": SENDER_NAME,
                "text": text
            }

            response = requests.post(f"{TARGET_BASE_URL}/messages", json=payload)
            response.raise_for_status()

            print(response.status_code)

        except requests.exceptions.RequestException as e:
            print(e)


if __name__ == "__main__":
    main()
