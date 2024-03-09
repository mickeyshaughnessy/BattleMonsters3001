from prompts import generate_monster

import requests
import json

resp = requests.post(
        "http://localhost:11434/api/generate", 
        json={"model" : "mistral", "prompt" : generate_monster % input()},
        stream=False)

_text = ""
for r in resp.iter_lines():
    r = json.loads(r)
    _text += r.get("response")

print(_text)
print(json.loads(_text))
