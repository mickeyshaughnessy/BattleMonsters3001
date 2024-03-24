import requests, json
import json

#model = "mistral:7b-text-q3_K_S"
model = "mistral"

def execute_completion(prompt):

    resp = requests.post(
            "http://localhost:11434/api/generate",
            json={"model" : model, "prompt" : prompt},
            stream=False)

    _text = ""
    for r in resp.iter_lines():
        r = json.loads(r)
        _text += r.get("response")
    return _text


