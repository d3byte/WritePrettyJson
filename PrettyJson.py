import json


def load_data(filepath):
    with open(filepath) as json_file:
        json_data = json.load(json_file)
        json_data = json.dumps(json_data, ensure_ascii=False, sort_keys=True, indent=4)
        return json_data


def rewrite_json(filepath, json_to_write):
    with open(filepath, "w", encoding="utf-8") as json_file:
        json_file.write(json_to_write)


if __name__ == '__main__':
    path_to_json = input("Enter the path to your json file: \n")
    json_file = load_data(path_to_json)
    path_to_new_file = input("Enter the path to your new json file: \n")
    rewrite_json(path_to_new_file, json_file)
    
