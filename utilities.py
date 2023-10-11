def create_booking_details(list_of_clubs, list_of_competitions):
    """Returns a dictionary with competition names as keys and booking details as values.
    In which, booking_details is a dictionary with club names as keys and corresponding
    number of places booked as values.
    Exemple of return value : {"some competition" : {"club1": 0, "club2": 2}}"""
    booking_details = {}
    for item in range(len(list_of_competitions)):
        clubs_dict = {}
        for i in range(len(list_of_clubs)):
            clubs_dict.update({list_of_clubs[i]["name"]: 0})
            booking_details.update({list_of_competitions[item]["name"]: clubs_dict})
    return booking_details


def update_booking_details(
    booking_details, name_of_club, name_of_competition, number_of_booked_places
):
    total_booked_places = (
        booking_details[name_of_competition][name_of_club] + number_of_booked_places
    )
    booking_details[name_of_competition].update({name_of_club: total_booked_places})
    return booking_details
