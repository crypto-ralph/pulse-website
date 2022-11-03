from flask import render_template, request

from website import create_app
from website.content_loader import load_content

app = create_app()


@app.get("/")
def index():
    posts_per_page = 10
    projects = load_content()
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
    num_of_projects = len(projects)
    num_of_pages = num_of_projects // posts_per_page
    if num_of_projects % posts_per_page != 0:
        num_of_pages += 1

    end_proj = page * posts_per_page
    beg_proj = end_proj - posts_per_page

    return render_template(
        "index.html",
        projects=projects[beg_proj:end_proj],
        num_of_projects=num_of_projects,
        num_of_pages=num_of_pages,
        media_links=medias
    )


if __name__ == '__main__':
    app.run(debug=True)
