"""Main App File"""
####################### CLI COPY PASTA ##################################################
# litestar run -r
# npx tailwindcss -i ./src/static/css/input.css -o ./src/static/css/styles.css --watch
# poetry export -f requirements.txt --output requirements.txt
#########################################################################################

from litestar import Litestar, Request, get
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.response import Template
from litestar.static_files import StaticFilesConfig
from litestar.template import TemplateConfig


@get("/")
async def serveHomepage(request: Request) -> Template:
    return Template(
        template_name="index.html.j2",
        context={
            "request": request,
        },
    )


app = Litestar(
    debug=True,
    route_handlers=[serveHomepage],
    template_config=TemplateConfig(
        directory="src/templates", engine=JinjaTemplateEngine
    ),
    static_files_config=[
        StaticFilesConfig(
            directories=["src/static"],
            path="/src/static",
            opt={"skip_rate_limiting": True},
            name="static",
        ),
    ],
)
