import json

PATH_FOR_INPUT_FILE = "INPUT_FILE.json"

PATH_FOR_OUTPUT_FILE = "OUTPUT_FILE.txt"

with open(PATH_FOR_INPUT_FILE, 'r', encoding='utf-8') as file:
    data = json.load(file)

with open(PATH_FOR_OUTPUT_FILE, 'w', encoding='utf-8') as outfile:
    for message in data["messages"]:
        if 'text' in message and 'from' in message:
            text = str(message['text'])
            if text:
                text = text.replace('\n', ' ')
                outfile.write(f"{message['date']} | {message['from']} | {text}\n")

print("The file was successfully created.")
