
from flask import Flask, request, Response
import os

app = Flask(__name__)

@app.route("/")
def get_lab():
    lab_no = request.args.get("labno")

    if not lab_no or not lab_no.isdigit():
        return "Invalid lab number", 400

    path = os.path.join("labs", f"lab{lab_no}.py")

    if not os.path.isfile(path):
        return "Lab not found", 404

    with open(path, encoding="utf-8") as f:
        return Response(f.read(), mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
