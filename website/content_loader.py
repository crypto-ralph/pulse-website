import json
import os

from flask import url_for
from werkzeug.routing import BuildError


class Project:
    def __init__(self, name: str, media: dict, description: str, contract: str = None):
        self.name = name
        self.media = media
        self.description = description

        logo = f"{name}.png"
        if os.path.exists(f'website/static/proj_img/{logo}'):
            self.logo = logo

        self.contract = contract if contract else "Currently no contract adress"

    def __str__(self):
        return self.name


def load_content() -> tuple:
    try:
        path = url_for('static', filename='data/projects.json')
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
                    "twitter": project.get("Twitter")},
                description=project.get("description")
            ) for project in data['projects']]
    return tuple(proj_list)
