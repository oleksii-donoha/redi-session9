# Base data for demo
GOOD_RESPONSE = {"type": "fighter", "model": "F-16"}
BAD_RESPONSE = {"type": "Ikarus"}


class IkarusException(Exception):
    """Custom exception for Ikarus"""


# Base functions for demo
def get_aircraft_model(aircraft_data: dict) -> str:
    """
    Returns the aircraft model from the given data.
    :param aircraft_data: aircraft data
    :return: model name
    """
    return aircraft_data["model"]


# Demo test cases
def get_aircraft_type(aircraft_data: dict) -> str:
    """
    Returns the aircraft type from the given data.
    :param aircraft_data: aircraft data
    :return: type name
    """
    return aircraft_data["type"]


def this_succeeds():
    print(get_aircraft_model(GOOD_RESPONSE))


def this_fails():
    print(get_aircraft_model(BAD_RESPONSE))


def this_catches_exception():
    try:
        print(get_aircraft_model(BAD_RESPONSE))
    except KeyError as e:
        print(e)
        print("Received Ikarus response")


def this_catches_multiple_exceptions():
    try:
        model = get_aircraft_model(GOOD_RESPONSE)
        print(int(model))
    except KeyError as e:
        print(e)
        print("Received Ikarus response")
    except ValueError as e:
        print(e)


def this_uses_else_clause():
    try:
        model = get_aircraft_model(GOOD_RESPONSE)
    except KeyError as e:
        print(e)
    else:
        print(model)


def this_uses_finally_clause():
    response = GOOD_RESPONSE
    # response = BAD_RESPONSE
    try:
        model = get_aircraft_model(response)
    except KeyError as e:
        print(e)
    else:
        print(model)
    finally:
        aircraft_type = get_aircraft_type(response)
        print(aircraft_type)


def this_raises_custom_exception():
    try:
        model = get_aircraft_model(BAD_RESPONSE)
    except KeyError as e:
        raise IkarusException from e
    else:
        print(model)


if __name__ == "__main__":
    this_succeeds()
    # this_fails()
    # this_catches_exception()
    # this_catches_multiple_exceptions()
    # this_uses_else_clause()
    # this_uses_finally_clause()
    # this_raises_custom_exception()
