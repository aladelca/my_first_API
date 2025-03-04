from datetime import datetime
from flask import make_response, abort
def get_timestamp():
    return datetime.now().strftime(('%Y-%m-%d %H:%M:%S'))

PEOPLE = {
    "Smith": {
        "fname": "John",
        "lname": "Smith",
        "timestamp": get_timestamp()
    },
    "Doe": {
        "fname": "Jane",
        "lname": "Doe",
        "timestamp": get_timestamp()
    },
    "Johnson": {
        "fname": "James",
        "lname": "Johnson",
        "timestamp": get_timestamp()
    }
}

def read_all():
    return [PEOPLE[key] for key in PEOPLE.keys()]

def create(person):
    lname = person.get("lname", None)
    fname = person.get("fname", None)
    if lname not in PEOPLE and lname is not None:
        PEOPLE[lname] = {
            "lname": lname,
            "fname": fname,
            "timestamp": get_timestamp()
        }
        return make_response(
            "{lname} was created successfully".format(lname=lname), 201
        )
    else:
        abort(
            406,
            "Person with name {lname} already exists".format(lname=lname),
        )

def read_one(lname):
    if lname in PEOPLE:
        person = PEOPLE.get(lname)
    else:
        abort(
            404, "Person with last name {lname} not found".format(lname=lname)
        )
    return person

def update(lname, person):
    if lname in PEOPLE:
        PEOPLE[lname]["fname"] = person.get("fname")
        PEOPLE[lname]["timestamp"] = get_timestamp()
        return PEOPLE[lname]
    else:   
        abort(
            404, "Person with last name {lname} not found".format(lname=lname)
        )

def delete(lname):
    if lname in PEOPLE:
        del PEOPLE[lname]
        return make_response(
            "{lname} was deleted successfully".format(lname=lname), 200
        )
    else:
        abort(
            404, "Person with last name {lname} not found".format(lname=lname)
        )