from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Hello, Backend!"
    })

@app.route("/about")
def about():
    return jsonify({
        "name": "Adan Ahmed",
        "role": "Backend AI Engineer",
        "skills": ["Python", "Flask", "Git"]
    })


if __name__ == "__main__":
    app.run(debug=True)