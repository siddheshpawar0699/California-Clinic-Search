from flask import Flask, render_template, request
import subprocess as sp
import re 
from pymongo import MongoClient
from gridfs import GridFS
from bson.objectid import ObjectId
from flask import send_file

app = Flask("myapp")

client = MongoClient()
db = client.clinic
myCollection = db.info
fs = GridFS(db)

@app.route("/")
def my_home():
    date = sp.getoutput("date /t")
    return render_template("front.html", date=date)

@app.route("/query")
def insert_val():
    find = request.args.get("find")
    regex = re.compile(find,re.IGNORECASE)
    cursor = myCollection.find({"ClinicName" : regex})
    result = []
    for record in cursor:
        result.append(record)
        print(record)
        
    return render_template("response.html", res = result)

@app.route("/geosearch")
def geosearch():
    find = request.args.get("find")
    lat = float(request.args.get("StandardLatitude"))
    lon = float(request.args.get("StandardLongitude"))
    radius = 1000  # define a default radius in meters
    regex = re.compile(find, re.IGNORECASE) if find else re.compile('', re.IGNORECASE)
    cursor = myCollection.find({
        "$and": [
            {"ClinicName": regex},
            {
                "location": {
                    "$nearSphere": {
                        "$geometry": {
                            "type": "Point",
                            "coordinates": [lon, lat]
                        },
                        "$maxDistance": radius
                    }
                }
            }
        ]
    })
    result = []
    print(regex)
    print(cursor)
    for record in cursor:
        result.append(record)
        print(record)

    return render_template("response.html", res=result)

@app.route('/details/<id>')
def details(id):
    record = myCollection.find_one({'_id': ObjectId(id)})
    if record is None:
        return "Record not found"
    return render_template('details.html', record=record)

@app.route('/image/<image_id>')
def image(image_id):
    # Retrieve an image from the database and return it as a Flask response
    image_id = ObjectId(image_id)
    file = fs.get(image_id)
    return send_file(file, mimetype='image/png')

@app.route('/add_comment/<id>', methods=['POST'])
def add_comment(id):
    comment = request.form['comment']
    myCollection.update_one({'_id': ObjectId(id)}, {'$push': {'comments': comment}})
    record = myCollection.find_one({'_id': ObjectId(id)})
    if record is None:
        return "Record not found"
    return render_template('details.html', record=record)


