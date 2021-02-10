import json
import os
import tempfile
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--key')
parser.add_argument('--val')
args = parser.parse_args()
key = args.key
val = args.val


def set(data, key, val):
    if key not in data:
        data[key] = []
    data[key].append(val)


def get(data, key):
    return data[key] if key in data else []


storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
mode = 'r+' if os.path.exists(storage_path) else 'w+'

with open(storage_path, mode) as f:
    content = f.read()
    data = json.loads(content) if content else {}

    if val is None:
        print(', '.join(get(data, key)))
    else:
        set(data, key, val)
        f.seek(0)
        f.write(json.dumps(data))
