
from quart import Blueprint

name_f = Blueprint("email_update", __name__)

@name_f.route(string_route, methods=["POST"])
def function_name1():
    pass


@name_f.route(string_route1, methods=["GET"])
def function_name2():
    pass