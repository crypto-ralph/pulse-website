from flask import render_template, request

from website import create_app
from website.content_loader import load_content

app = create_app()
projects = load_content()


def is_hot(elem):
    return 1 if elem.is_hot else 0


@app.route("/", methods=['GET', 'POST'])
def index():
    global projects
    result = None
    request_data = request.form.get('search_phrase')
    if request.method == 'POST' and request_data is not None:
        result = [project for project in projects if
                  request_data.lower() in project.name.lower()]

    found_projects = result if result is not None else projects

    found_projects.sort(key=is_hot, reverse=True)

    posts_per_page = 10
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
        {
            "link": "Template",
            "img": "pulse_twitt.png",
            "text": "Template",
        },
    ]

    page = request.args.get("page")
    page = int(page) if page and page.isdigit() else 1
    num_of_projects = len(found_projects)
    num_of_pages = num_of_projects // posts_per_page
    if num_of_projects % posts_per_page != 0:
        num_of_pages += 1

    end_proj = page * posts_per_page
    beg_proj = end_proj - posts_per_page

    return render_template(
        "index.html",
        projects=found_projects[beg_proj:end_proj],
        num_of_projects=len(projects),
        num_of_pages=num_of_pages,
        media_links=medias,
        in_progress_flag=False,
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0')
