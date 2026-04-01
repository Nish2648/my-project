@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/")
def home():
    return jsonify({"message": "Hello CI/CD"})

@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return jsonify({"result": a + b})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)