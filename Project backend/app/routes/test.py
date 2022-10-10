from app import app
from app.controllers import test

#app.route("/", methods=["GET"])(test.index) #flask biasanya pake gate
app.route("/create", methods=["POST"])(test.Create)
app.route("/list", methods=["GET"])(test.List)
app.route("/update/<tableId>", methods=["PUT"])(test.Update)
app.route("/delete/<tableId>", methods=["DELETE"])(test.Delete)
app.route("/detail/<tableId>", methods=["GET"])(test.Detail)