import json
from datetime import datetime
from flask import Flask, render_template, request, redirect, flash, url_for

from utilities import create_booking_details, update_booking_details


def load_clubs():
    with open("clubs.json") as c:
        list_of_clubs = json.load(c)["clubs"]
        return list_of_clubs


def load_competitions():
    with open("competitions.json") as comps:
        list_of_competitions = json.load(comps)["competitions"]
        return list_of_competitions


app = Flask(__name__)
app.secret_key = "something_special"

competitions = load_competitions()
clubs = load_clubs()
booking_details = create_booking_details(clubs, competitions)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/showSummary", methods=["POST"])
def show_summary():
    user_input = request.form["email"]
    try:
        club = [club for club in clubs if club["email"] == user_input][0]
        return render_template("welcome.html", club=club, competitions=competitions)
    except IndexError:
        if user_input == "":
            flash("Please enter a valid email.", "error")
            # if an email id isn't supplied in the request, return a 400 bad request
            status = 400
        else:
            flash("Sorry, that email wasn't found.", "error")
            # if an email id is not found in the database, return a 401 unauthorized
            status = 401
        return render_template("index.html"), status


@app.route("/book/<competition>/<club>")
def book(competition, club):
    try:
        found_club = [c for c in clubs if c["name"] == club][0]
        found_competition = [c for c in competitions if c["name"] == competition][0]
        competition_date = datetime.strptime(
            found_competition["date"], "%Y-%m-%d %H:%M:%S"
        )
        if competition_date > datetime.now():
            flash("You have successfully landed in the booking page !", "success")
            return render_template(
                "booking.html", club=found_club, competition=found_competition
            )
        else:
            flash("Sorry, this competition is over !", "error")
            return (
                render_template("welcome.html", club=club, competitions=competitions),
                400,
            )
    except IndexError:
        flash("Something went wrong-please try again", "error")
        return (
            render_template("welcome.html", club=club, competitions=competitions),
            500,
        )


@app.route("/purchasePlaces", methods=["POST"])
def purchase_places():
    competition = [c for c in competitions if c["name"] == request.form["competition"]][
        0
    ]
    club = [c for c in clubs if c["name"] == request.form["club"]][0]
    places_required = request.form["places"]
    if places_required.isnumeric():
        places_required = int(places_required)
    else:
        flash("Please enter a valid number", "error")
        return render_template("booking.html", club=club, competition=competition), 500

    if places_required + booking_details[competition["name"]][club["name"]] <= 12:
        competition["numberOfPlaces"] = (
            int(competition["numberOfPlaces"]) - places_required
        )
        club["points"] = int(club["points"]) - places_required
        update_booking_details(
            booking_details, club["name"], competition["name"], places_required
        )
        flash("Great-booking complete!", "success")
        return (
            render_template("welcome.html", club=club, competitions=competitions),
            200,
        )
    else:
        flash("Sorry, you cannot book more than 12 places for a competition!", "error")
        return render_template("booking.html", club=club, competition=competition), 400


# TODO: Add route for points display


@app.route("/logout")
def logout():
    return redirect(url_for("index"))
