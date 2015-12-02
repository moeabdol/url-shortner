from flask import Flask, render_template, request, redirect
import models

app = Flask(__name__, template_folder="views")

@app.route("/")
def index():
    return render_template("main_page.html")

@app.route("/shorten/")
def shorten():
    full_url = request.args.get("url")
    if not full_url:
        raise request.BadRequest()

    url_model = models.Url.shorten(full_url)
    url_model.short_url

    short_url = request.host + "/" + url_model.short_url
    return render_template("success.html", short_url=short_url)

@app.route("/<path:path>")
def redirect_to_full(path=""):
    url_model = models.Url.get_by_short_url(path)
    if not url_model:
        raise request.NotFound()
    return redirect(url_model.full_url)

if __name__ == "__main__":
    app.run(debug=True)
