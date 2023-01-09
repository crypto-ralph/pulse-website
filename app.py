from flask import render_template, request

from website import create_app
from website.content_loader import load_content

app = create_app()
projects = load_content()


@app.route("/", methods=["GET", "POST"])
def index():
    global projects
    results = None
    site_params = {
        "hot_only": False,
        "has_contract": False,
        "search_phrase": "find project",
        "sorting": "A-Z",
    }
    num_of_pages = 0

    if request.method == "POST":
        search_phrase = request.form.get("search_phrase")

        if search_phrase != "":
            results = [
                project for project in projects if search_phrase.lower() in project.name.lower()
            ]
        else:
            results = projects
        site_params["search_phrase"] = search_phrase if search_phrase != "" else "find project"

        if "hot_only" in request.form:
            results = [project for project in results if project.is_hot]
            site_params["hot_only"] = True

        if "has_contract" in request.form:
            results = [
                project for project in results if project.contract
            ]
            site_params["has_contract"] = True

        if request.form.get("sorting") == "Z-A":
            results.sort(reverse=True)
            site_params["sorting"] = "Z-A"
        elif request.form.get("sorting") == "Twitter desc":
            results = [project for project in results if project.twitter_followers is not None]
            results.sort(key=lambda x: int(x.twitter_followers), reverse=True)
            site_params["sorting"] = "Twitter desc"
        elif request.form.get("sorting") == "Twitter asc":
            results = [project for project in results if project.twitter_followers is not None]
            results.sort(key=lambda x: int(x.twitter_followers))
            site_params["sorting"] = "Twitter asc"

    found_projects = results if results is not None else projects

    posts_per_page = 10

    # paginate
    if request.method == "GET":
        page = request.args.get("page")
        page = int(page) if page and page.isdigit() else 1
        num_of_projects = len(found_projects)
        num_of_pages = num_of_projects // posts_per_page
        if num_of_projects % posts_per_page != 0:
            num_of_pages += 1

        end_proj = page * posts_per_page
        beg_proj = end_proj - posts_per_page
        found_projects = found_projects[beg_proj:end_proj]

    medias = [
        {
            "link": "https://twitter.com/pulsechaincom",
            "img": "pulse_twitt.png",
            "text": "Pulsechain",
        },
        {
            "link": "https://twitter.com/pulsexcom",
            "img": "pulsex_twitt.png",
            "text": "PulseX",
        },
        {
            "link": "https://twitter.com/RichardHeartWin",
            "img": "richard_twitt.png",
            "text": "Richard Heart",
        },
    ]

    return render_template(
        "index.html",
        projects=found_projects,
        num_of_projects=len(projects),
        num_of_pages=num_of_pages,
        media_links=medias,
        in_progress_flag=False,
        site_params=site_params,
        paginate=True if request.method == "GET" else False,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0")
