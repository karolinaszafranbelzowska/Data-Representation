from flask import Flask, url_for, request, redirect, abort, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return"Hello, World!"

if __name__ == "__main__":
    print("in if")
    app.run(debug=True)

