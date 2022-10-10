from app import app
from app.controllers import test

app.route("/", methods=["GET"])(test.index) #flask biasanya pake gate
app.route("/create", methods=["POST"])(test.create)
