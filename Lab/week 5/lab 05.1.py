# Question 1
# Test to see if CURL is working from my command line

C:\Users\karolina
λ curl google.com
<HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
<TITLE>301 Moved</TITLE></HEAD><BODY>
<H1>301 Moved</H1>
The document has moved
<A HREF="http://www.google.com/">here</A>.
</BODY></HTML>


# Question 2
# Check -i option

C:\Users\karolina
λ curl -i google.com
HTTP/1.1 301 Moved Permanently
Location: http://www.google.com/
Content-Type: text/html; charset=UTF-8
Date: Sun, 01 Nov 2020 17:21:36 GMT
Expires: Tue, 01 Dec 2020 17:21:36 GMT
Cache-Control: public, max-age=2592000
Server: gws
Content-Length: 219
X-XSS-Protection: 0
X-Frame-Options: SAMEORIGIN

<HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
<TITLE>301 Moved</TITLE></HEAD><BODY>
<H1>301 Moved</H1>
The document has moved
<A HREF="http://www.google.com/">here</A>.
</BODY></HTML>


# Queston 3 a
# Look at http://andrewbeatty.pythonanywhere.com/
# How would I get all books?

C:\Users\karolina
λ curl http://andrewbeatty1.pythonanywhere.com/books
[{"Author":"34","Price":34,"Title":"34","id":10},
{"Author":"234","Price":214,"Title":"ee'234'","id":11},
{"Author":"FA","Price":4000,"Title":"myBook","id":12},
{"Author":"rt","Price":1999,"Title":"I DID IT","id":19},
{"Author":"xxx","Price":2000,"Title":"xxx","id":21},
{"Author":"Chris C","Price":999,"Title":"Curl For Dummies","id":27},
{"Author":"Chris C","Price":777,"Title":"Acing The Curl Class An Autobiography of Chris Collins 2","id":29},
{"Author":"Eoin Dowling","Price":20,"Title":"Testing the Mighty Curl","id":34},
{"Author":"blah blah","Price":2000,"Title":"blah","id":36},
{"Author":"Mount","Price":3000,"Title":"Curl Programming Bible","id":42},
{"Author":"Eoin","Price":10000001,"Title":"Getting Q4 to work","id":46},
{"Author":"Donal","Price":3000,"Title":"Curl Unfurled","id":52},
{"Author":"GeethaK","Price":1750,"Title":"Bhagavad Gita","id":62}]


# Queston 3 b
# Look at http://andrewbeatty.pythonanywhere.com/
# How would I get all the book with id 9?

C:\Users\karolina
λ curl http://andrewbeatty1.pythonanywhere.com/books/9
{}


# Question 4
# For the same website how would you use curl to create book, 
# NOTE the id of the book you made. You can test if your book is there using the find by id.

# Windows (windows only has “ (no ‘) so the data needs to be between “ “ and all the
# inverted commas in the JSON need to be escaped \”. 

C:\Users\karolina
λ curl -i -H "Content-Type:application/json" -X POST -d "{\"Title\":\"The Shadow of the Wind\",\"Author\":\"Carlos Zafon\",\"Price\":599}" http://andrewbeatty1.pythonanywhere.com/books
HTTP/1.1 200 OK
Date: Sun, 01 Nov 2020 17:06:51 GMT
Content-Type: application/json
Content-Length: 79
Connection: keep-alive
Access-Control-Allow-Origin: *
X-Clacks-Overhead: GNU Terry Pratchett
Server: PythonAnywhere

{"Author":"Carlos Zafon","Price":599,"Title":"The Shadow of the Wind","id":65}


# Question 5
# For the same website how would you use curl to update a book (use your book)

C:\Users\karolina
λ curl -i -H "Content-Type:application/json" -X PUT -d "{\"Price\":29900}" http://andrewbeatty1.pythonanywhere.com/books/65
HTTP/1.1 200 OK
Date: Sun, 01 Nov 2020 17:10:43 GMT
Content-Type: application/json
Content-Length: 81
Connection: keep-alive
Access-Control-Allow-Origin: *
X-Clacks-Overhead: GNU Terry Pratchett
Server: PythonAnywhere

{"Author":"Carlos Zafon","Price":29900,"Title":"The Shadow of the Wind","id":65}


# Question 6
# For the same web site how would you use curl to delete the book you just made.

C:\Users\karolina
λ curl -X DELETE http://andrewbeatty1.pythonanywhere.com/books/65
{"done":true}

