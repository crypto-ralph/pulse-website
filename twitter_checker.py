import requests

from data_manipulation import load_projects_json, save_projects_json

# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
# bearer_token = os.environ.get("BEARER_TOKEN")
bearer_token = "AAAAAAAAAAAAAAAAAAAAAKTRjAEAAAAATezftaDQxat7ZNz%2FW3LWtQI%2FysE%3DZ0DQtPLHOFGTciM2zaf4dT5Eu7GgDwqqzzqSLhlnR9UqPVR8ph"


def create_url(users_string: str):
    # Specify the usernames that you want to lookup below
    # You can enter up to 100 comma-separated values.
    usernames = f"usernames={users_string}"
    print(usernames)
    user_fields = "user.fields=public_metrics"
    # User fields are adjustable, options include:
    # created_at, description, entities, id, location, name,
    # pinned_tweet_id, profile_image_url, protected,
    # public_metrics, url, username, verified, and withheld
    url = "https://api.twitter.com/2/users/by?{}&{}".format(usernames, user_fields)
    return url


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2UserLookupPython"
    return r


def connect_to_endpoint(url):
    response = requests.request("GET", url, auth=bearer_oauth, )
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def main():
    projects = load_projects_json()

    users_string = ""
    for x in projects["projects"]:

        twitter_account = x.get("Twitter")
        if twitter_account is not None:
            users_string += twitter_account
            users_string += ","

    users_string = users_string[:-1]

    url = create_url(users_string)
    json_response = connect_to_endpoint(url)
    # print(json.dumps(json_response, indent=4, sort_keys=True))

    for project in projects["projects"]:
        proj_twitter = project.get("Twitter")
        if proj_twitter is not None:
            for response in json_response["data"]:
                # print(response["username"])
                # print(project["name"])

                if response["username"].lower() == project["Twitter"].lower():
                    if project["twitter_followers"] is not None:
                        project["twitter_followers_prev"] = project["twitter_followers"]
                    project["twitter_followers"] = response["public_metrics"]["followers_count"]

    save_projects_json(projects, "new")


if __name__ == "__main__":
    main()
