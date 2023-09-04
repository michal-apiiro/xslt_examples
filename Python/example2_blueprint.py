from quart import Blueprint, Quart

app = Quart(__name__)
name_f = Blueprint("email_update", __name__)

class EmailUpdateView:
    def __init__(self, name_f):
        self.name_f = name_f

    @name_f.route("/update_email", methods=["POST"])
    async def update_email(self):
        return "Update Email"

    @name_f.route("/get_email", methods=["GET"])
    async def get_email(self):
        return "Get Email"

email_update_view = EmailUpdateView(name_f)

if __name__ == "__main__":
    app.register_blueprint(name_f)
    app.run()




