import json
import os

from werkzeug.routing import BuildError


class Project:
    def __init__(
            self,
            name: str,
            media: dict,
            description: str,
            contract: str,
            is_hot: bool,
            contract_chain: str
    ):
        self.name = name
        self.media = media
        self.description = description
        self.is_hot = is_hot
        self.contract_chain = contract_chain

        logo = f"{name}.png"
        if os.path.exists(f'website/static/proj_img/{logo}'):
            self.logo = logo

        self.contract = contract if contract else "Currently no contract adress"

    def __str__(self):
        return self.name


def load_content() -> tuple:
    try:
        path = 'static/data/projects.json'
    except BuildError as e:
        print(e)
        return tuple()

    try:
        with open(f'website/{path}', 'r') as file:
            data = json.load(file)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return tuple()

    proj_list = [Project(
        name=project['name'],
        media={
            "website": project.get("Website"),
            "twitter": project.get("Twitter"),
            "telegram": project.get("Telegram")
        },
        description=project.get("description") if project.get("description") else project.get(
            "text"),
        contract=project.get("contract"),
        contract_chain=project.get("contract_chain"),
        is_hot=project.get("is_hot")
    ) for project in data['projects']]
    return tuple(proj_list)
