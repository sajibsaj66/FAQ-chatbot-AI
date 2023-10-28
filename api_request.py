import requests

if __name__ == '__main__':
    while True:
        response = requests.get("http://127.0.0.1:5000/chat_bot_train")
        if response.status_code == 200:
            print("Training successful.")
        else:
            print("Training failed.")

        text = input("user:")
        if text == '':
            break

        text = {"text": text}
        api_url = "http://127.0.0.1:5000/chat_bot"
        response = requests.post(api_url, json=text)

        print(response.json())

        if response.status_code == 200:
            data = response.json()
            text = data.get("response", "No response")
            print(text)

        else:
            print(f"response-----------{response.status_code}")
