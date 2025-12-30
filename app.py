from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/issue", methods=["POST"])
def receive_issue():
    data = request.json

    issue_title = data.get("title", "No title received")

    print("===================================")
    print("📌 GitHub Issue Title Received:")
    print(issue_title)
    print("===================================")
    print("Testing Pull Requests")
    print("Testing Pull Request 2")

    return jsonify({"status": "received"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
