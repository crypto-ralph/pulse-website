import json
import os


def load_projects_json():
    print(os.getcwd())
    with open("website/static/data/projects.json") as file:
        data = json.load(file)
    return data


def save_projects_json(data: dict, name: str):
    with open(f"website/static/data/{name}.json", "w") as outfile:
        json.dump(data, outfile, indent=4)


if __name__ == "__main__":

    data = load_projects_json()

    for project in data['projects']:
        if project.get('contract') is None:
            project['contract'] = None
        if project.get('contract_chain') is None:
            project['contract_chain'] = None
        if project.get('description') is None:
            project['description'] = None
        if project.get('is_hot') is None:
            project['is_hot'] = False
        if project.get('personal_mark') is None:
            project['personal_mark'] = False
        if project.get("Twitter") is not None:
            project["Twitter"] = project["Twitter"].split("/")[-1]

    save_projects_json(data)
