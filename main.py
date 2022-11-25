import concurrent.futures
import flask
from flask import abort


def main(request):
    return request


def func_main(request: flask.Request) -> dict:
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    request_json = request.get_json()
    try:
        response = main(request_json)
        return response
    except concurrent.futures.TimeoutError:
        return flask.abort(504)