import main
from users_map import build_map
from flask import Flask, redirect, render_template, request, url_for
from urllib.error import HTTPError
app = Flask(__name__)


def before_request():
    app.jinja_env.cache = {}


app.before_request(before_request)


@app.route("/", methods=["GET", "POST"])
def index():
    print("INDEX")
    if request.method == "GET":
        print("GET")
        return render_template("index.html")

    if request.method == "POST":
        print("POST")
        try:
            f_year = request.form['first_year']
            l_year = request.form['last_year']
            if f_year.isdigit() and l_year.isdigit():
                f_year = int(f_year)
                l_year = int(l_year)
            else:
                raise HTTPError
            years = [year for year in range(f_year, l_year+1)\
                     if f_year >= 1980 and l_year <= 2017 and f_year<=l_year]
            countries = main.check_web_input(request.form['country'])
            if not countries:
                raise HTTPError
            result = main.Countries(years, countries)
            result.fill_the_array()
            build_map(result.result)
        except TypeError:
            return render_template("index.html")
        except HTTPError:
            pass
        return redirect(url_for('map'))


@app.route("/map", methods=["GET"])
def map():
    return render_template("users.html")

if __name__ == "__main__":
    app.run(debug = True)