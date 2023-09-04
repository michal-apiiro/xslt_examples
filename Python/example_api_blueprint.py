from quart import Blueprint

name_f = Blueprint("email_update", __name__)

string_route = "/update_email"
string_route1 = "/get_email"

@name_f.route(string_route, methods=["POST"])
def function_name1():
    pass

@name_f.route(string_route1, methods=["GET"])
def function_name2():
    pass