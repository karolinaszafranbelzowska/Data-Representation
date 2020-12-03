from flask import Flask, url_for, request, redirect, abort, jsonify

app = Flask(__name__)

books = [
    {"id":1, "Title":"Harry Poter", "Author":"JKR", "Price":1000},
    {"id":2, "Title":"The Twilight Saga", "Author":"Stephenie Meyer", "Price":2000},
    {"id":3, "Title":"Cien wiatru", "Author":"Carlos Ruiz Zafon", "Price":3000},
]
nextid = 4

@app.route('/')
def index():
    return"Hello, World!"

@app.route('/books')
def getAll():
    return"Served by getAll!"

@app.route('/books/<int:id>')
def findById(id):
    return"Served by findById with it!" + str(id)

@app.route('/books',methods=['POST'])
def create():
    return"Served by Create" 

@app.route('/books/<int:id>', methods=["PUT"])
def update(id):
    return"Served by update with it " + str(id)

@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
    return"Served by delete with it " + str(id)

if __name__ == "__main__":
    print("in if")
    app.run(debug=True)

