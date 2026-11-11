
from flask import Flask, request, Response
from pathlib import Path
import re

app = Flask(__name__)
LABS_DIR = Path(__file__).parent / "lab"

@app.route("/")
def get_lab():
    lab_id = request.args.get("labno", "")

    if not re.fullmatch(r"[a-zA-Z0-9]+", lab_id):
        return "Invalid lab ID", 400

    file_path = LABS_DIR / f"{lab_id}.py"

    if not file_path.is_file():
        return f"Lab not found: {lab_id}", 404

    code = file_path.read_text(encoding="utf-8")
    return Response(code, mimetype="text/plain")

@app.route("/health")
def health():
    return "Server is running", 200
