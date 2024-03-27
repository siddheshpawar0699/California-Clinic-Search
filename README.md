[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=10442999&assignment_repo_type=AssignmentRepo)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=10442999&assignment_repo_type=AssignmentRepo)

## Technologies Used - 

* MongoDB
* Flask
* Python 
* HTML 
* CSS
## Dataset -
   California Clinics Dataset - https://healthdata.gov/dataset/State-of-California-Geocoded-Providers-2019-Califo/yg3r-d5zt
   ### Attributes:
   * ID
   * Clinic
   * Address
   * City
   * Phone
   * ClinicServiceType
   * StandardLatitude
   * StandardLongitude

# Overview
* This is a Flask application that connects to a MongoDB database and performs various operations such as inserting values, querying data, and retrieving images. It also includes templates for displaying data and forms for searching and adding comments.

* The app.py file contains the main Flask application. It starts by importing necessary modules such as Flask, render_template, request, subprocess, re, MongoClient, and GridFS. It then creates an instance of the Flask class and connects to the MongoDB database.

* The first route, my_home(), renders the front.html template and passes the current date to it. The front.html template is a simple HTML form with two search fields.

* The second route, insert_val(), queries the MongoDB database using a regular expression and returns the results as a list of records. It then renders the response.html template and passes the results to it.

* The third route, geosearch(), performs a geospatial query on the MongoDB database using the $nearSphere operator. It searches for records within a certain radius of a specified location. It also uses a regular expression to filter the results based on a search term. The results are returned as a list of records and rendered using the response.html template.

* The fourth route, details(), retrieves a single record from the MongoDB database using its ID and renders the details.html template, passing the record as a parameter.

* The fifth route, image(), retrieves an image from the MongoDB database using its ID and returns it as a Flask response.

* The sixth route, add_comment(), adds a comment to a record in the MongoDB database using its ID and renders the details.html template, passing the updated record as a parameter.

* The front.html template contains two forms for searching the database. The first form searches for records that match a specified term using the insert_val() route. The second form searches for records that are within a certain radius of a specified location using the geosearch() route.

* The response.html template displays the results of a search. If no results are found, it displays a message indicating that no results were found. If results are found, it displays a link to each record found.

* The details.html template displays the details of a single record, including its name, address, phone number, comments, and an image if one exists. It also contains a form for adding comments to the record.


## Steps - 

1. Make sure you have Python installed on your system. If not, download and install it from the official website (https://www.python.org/downloads/).

2. Install Flask and its dependencies. You can do this by running the following command in your command prompt or terminal:
   pip install Flask pymongo gridfs

3. create a venv to run flask.

4. Save the app.py file and the templates folder containing the HTML files in a directory of your choice.

5. Open a command prompt or terminal window, enter the JSR venv and navigate to the directory where the app.py file is saved.

6. Run the following command to start the Flask application:
   ```
   export FLASK_APP=app.py
   flask run
   ```

## You should see output similar to this -

   ```
   Running on http://127.0.0.1:9000/ (Press CTRL+C to quit)
   Open your web browser and go to the URL http://localhost:9000/ (or http://127.0.0.1:9000/). 
   ```
- You should see the home page of the application.
- Use the search forms to query the database and view the search results.
