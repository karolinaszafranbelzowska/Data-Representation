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
    return jsonify(books)

@app.route('/books/<int:id>')
def findById(id):
    foundBooks = list(filter (lambda t : t["id"] == id, books))
    if len(foundBooks) == 0:
        return jsonify({}) , 204
    return jsonify(foundBooks[0])
    
@app.route('/books',methods=['POST'])
def create():
    global nextid
    if not request.json:
        abort(400)
    
    book = {
        "id": nextid,
        "Title": request.json["Title"],
        "Author": request.json["Author"],
        "Price": request.json["Price"]
    }
    books.append(book)
    nextid += 1
    return jsonify(book)

    # return"Served by Create" 

@app.route('/books/<int:id>', methods=["PUT"])
def update(id):
    foundBooks = list(filter(lambda t: t["id"] == id, books))
    if len(foundBooks) == 0:
        return jsonify({}), 404
    currentBook = foundBooks[0]
    if 'Title' in request.json:
        currentBook['Title'] = request.json['Title']
    if 'Author' in request.json:
        currentBook['Author'] = request.json['Author']
    if 'Price' in request.json:
        currentBook['Price'] = request.json['Price']

    return jsonify(currentBook)

@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
    foundBooks = list(filter(lambda t: t["id"] == id, books))
    if len(foundBooks) == 0:
        return jsonify({}), 404
    books.remove(foundBooks[0])
    
    return jsonify({"done":True})
    

if __name__ == "__main__":
    print("in if")
    app.run(debug=True)

