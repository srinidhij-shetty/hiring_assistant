import json

def save_candidate(data):
    with open("candidates.json", "a") as f:
        json.dump(data, f)
        f.write("\n")