# ICAV_Book_Retrieval
API to retrieve Books based on some requests from csv file.

How to run

docker build -t dockerpython .
docker run -p 5000:5000 dockerpython

how to get the data

localhost:5000/book/<no. of rows want to retrieve>
localhost:5000/book_filter/filter_you_want(author_name or id or year etc.)
