from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
import os, json

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)

COMMENT_DIR = "comments"
os.makedirs(COMMENT_DIR, exist_ok=True)

@app.route("/disk01")
def disk01_page():
    return render_template("disk01.html")

@app.route("/disk02")
def disk02_page():
    return render_template("disk02.html")

@app.route("/disk03")
def disk03_page():
    return render_template("disk03.html")

@app.route("/disk04")
def disk04_page():
    return render_template("disk04.html")

@app.route("/disk05")
def disk05_page():
    return render_template("disk05.html")

@app.route("/disk06")
def disk06_page():
    return render_template("disk06.html")

@app.route("/disk07")
def disk07_page():
    return render_template("disk07.html")

@app.route("/disk08")
def disk08_page():
    return render_template("disk08.html")

@app.route("/disk09")
def disk09_page():
    return render_template("disk09.html")

@app.route("/disk10")
def disk10_page():
    return render_template("disk10.html")

@app.route("/disk11")
def disk11_page():
    return render_template("disk11.html")

@app.route("/disk12")
def disk12_page():
    return render_template("disk12.html")


@app.route("/comments", methods=["GET", "POST"])
def comments():
    disk = request.args.get("disk")
    if not disk:
        return jsonify({"error": "Missing 'disk' parameter"}), 400

    path = os.path.join(COMMENT_DIR, f"comments_{disk}.json")

    if request.method == "POST":
        data = request.get_json()
        name = data.get("name", "匿名")
        content = data.get("content", "").strip()
        timestamp = data.get("timestamp")

        if not content:
            return jsonify({"error": "Empty comment"}), 400

        comment = {"name": name, "content": content, "timestamp": timestamp}
        comments = []
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                comments = json.load(f)

        comments.append(comment)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(comments, f, ensure_ascii=False, indent=2)

        return jsonify({"success": True}), 201

    else:
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                return jsonify(json.load(f))
        return jsonify([])

@app.route("/main")
def main_page():
    return render_template("main.html")

@app.route("/popular")
def popular_page():
    return render_template("popular.html")

@app.route("/index.html")
def index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
