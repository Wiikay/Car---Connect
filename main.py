import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__, static_url_path='')

@app.route("/")
def index():
    """Serve the index.html file."""
    return send_from_directory('.', 'index.html')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))