from flask import Flask
import json

app = Flask(__name__)

def csv_to_json():
    import csv
    import json

    # Define the header names so we can specify them when reading the CSV
    fieldnames = (
        "id", "title", "author", "authors", "isbn13", "isbn10", "price", "publisher", "pubyear",
        "subjects", "lexile", "pages", "dimensions"

    )

    #read and write the files
    with open('./books.csv', 'r') as csvfile:
        with open('./books.json', 'w') as jsonfile:
            #next will simply skip over the header row in the csvfile
            next(csvfile)

            reader = csv.DictReader(csvfile, fieldnames)

            final_data = {"books": []}
            #iterate the csv
            for row in reader:
                #restructure data to be represented as dictionary
                final_data['books'].append({
                    "id": row["id"],
                    "title": row["title"],
                    "author": row["author"],
                    "authors": row["authors"],
                    "isbn13": row["isbn13"],
                    "isbn10": row["isbn10"],
                    "price": row["price"],
                    "publisher": row["publisher"],
                    "pubyear": row["pubyear"],
                    "subjects": row["subjects"],
                    "lexile": row["lexile"],
                    "pages": row["pages"],
                    "dimensions": row["dimensions"]

                })
                """
                final_data[row['id']] = {
                    "id": row["id"],
                    "title": row["title"],
                    "author": row["author"],
                    "authors": row["authors"],
                    "isbn13": row["isbn13"],
                    "isbn10": row["isbn10"],
                    "price": row["price"],
                    "publisher": row["publisher"],
                    "pubyear": row["pubyear"],
                    "subjects": row["subjects"],
                    "lexile": row["lexile"],
                    "pages": row["pages"],
                    "dimensions": row["dimensions"]

                }"""
            #write to json file
            json.dump(final_data, jsonfile)
            #write to new line
            jsonfile.write('\n')


@app.route('/book/<row>')
def book(row):
    output_val = []
    with open('./books.json', 'r') as jsonfile:
        file_data = json.loads(jsonfile.read())

    for i in range(int(row)):
        output_val.append(file_data["books"][i])
    return json.dumps(output_val)

@app.route('/book_filter/<filter_val>')
def filter_book(filter_val):
    output_val = []
    with open('./books.json', 'r') as jsonfile:
        file_data = json.loads(jsonfile.read())
    for i in range(len(file_data["books"])):
        for key, val in file_data["books"][i].items():
            print(key, val)
            if val == filter_val and file_data["books"][i] not in output_val:
                output_val.append(file_data["books"][i])

    return json.dumps(output_val)


if __name__ == '__main__':
    csv_to_json()
    app.run(debug=True, host='0.0.0.0', port=5000)
