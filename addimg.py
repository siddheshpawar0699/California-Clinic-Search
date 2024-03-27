from pymongo import MongoClient
from gridfs import GridFS

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['clinic']

# Get a reference to the GridFS collection
fs = GridFS(db)

# List of image filenames and clinic names
image_clinic_list = [
    ('/home/student/Desktop/images/images/Afc-urgent-care.jpeg', 'AFC URGENT CARE OF SAN DIEGO'),
    ('/home/student/Desktop/images/images/Alfa-surgery-center.jpeg', 'Alfa Surgery Center'),
    ('/home/student/Desktop/images/images/Bolsa-center.jpeg', 'Bolsa Outpatient Surgery Center'),
    ('/home/student/Desktop/images/images/capitol-city-surgery-center.jpeg', 'Capitol City Surgery Center'),
    ('/home/student/Desktop/images/images/Diamond-neighborhood-family-center.jpeg', 'DIAMOND NEIGHBORHOODS FAMILY HEALTH CENTER'),
    ('/home/student/Desktop/images/images/Elica-health-center.jpeg', 'ELICA HEALTH CENTERS'),
    ('/home/student/Desktop/images/images/la-maestra-community-center.jpeg', 'LA MAESTRA COMMUNITY HEALTH CENTER BROADWAY CLINIC'),
    ('/home/student/Desktop/images/images/Neighborhood-healthcare.jpeg', 'NEIGHBORHOOD HEALTHCARE- EL CAJON'),
    ('/home/student/Desktop/images/images/One-community-health.jpeg', 'ONE COMMUNITY HEALTH'),
    ('/home/student/Desktop/images/images/Peach-tree-healthcare.jpeg', 'PEACH TREE HEALTHCARE')

]

# Loop over the list and update each clinic document with the image _id
for image_name, clinic_name in image_clinic_list:
    # Retrieve the clinic document
    clinic = db.info.find_one({'ClinicName': clinic_name})

    # Get the _id of the image in GridFS
    image_id = db.fs.files.find_one({'filename': image_name})['_id']

    # Update the clinic document with the image _id
    if clinic:
        db.info.update_one(
            {'_id': clinic['_id']},
            {'$set': {'image_id': image_id}}
        )
    else:
        print(f'Clinic {clinic_name} not found')

# Retrieve clinics that don't have an image
clinics_without_image = db.info.find({'image_id': {'$exists': False}})

# Get the _id of the default image in GridFS
default_image_id = db.fs.files.find_one({'filename': 'hospital.jpg'})['_id']

# Update the clinics without an image with the default image _id
for clinic in clinics_without_image:
    db.info.update_one(
        {'_id': clinic['_id']},
        {'$set': {'image_id': default_image_id}}
    )


