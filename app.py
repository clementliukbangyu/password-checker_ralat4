from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def check_password_rules(pw: str):
    issues = []
    if len(pw) < 8:
        issues.append("At least 8 characters required")
    if not any(c.isupper() for c in pw):
        issues.append("Add uppercase letter")
    if not any(c.islower() for c in pw):
        issues.append("Add lowercase letter")
    if not any(c.isdigit() for c in pw):
        issues.append("Add number")
    if not any(c in "!@#$%^&*()-_=+[]{};:'\",.<>?/|\\`~" for c in pw):
        issues.append("Add special symbol (!@#$)")
    return issues

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check():
    data = request.get_json() or {}
    pw = data.get("password", "")
    issues = check_password_rules(pw)
    return jsonify({"syarat": issues})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
