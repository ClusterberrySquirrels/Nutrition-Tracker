## Nutrition-Tracker
Database app to track users meals and nutrition intake

# Running in Flask

Clone the repo

    git clone https://github.com/ClusterberrySquirrels/Nutrition-Tracker.git

From outside the project folder, create and activate the virtual Python environment. You'll have to install required packages in the virtual environment from

    python3 -m venv env
    Linux: source env/bin/activate
    Windows: env\bin\activate
    pip install flask flask-sqlalchemy flask-login flask-moment flask-bootstrap flask-wtf

Run the following command to set your environment variables for the Flask app:
    
    Windows: 
    set FLASK_APP=nutritiontracker
    set FLASK_DEBUG=1
    
    Linux:
    export FLASK_APP=nutritiontracker
    export FLASK_DEBUG=1

Run the program

    flask run

Then go to your navigation browser of your choice and enter 
the following URL: http://127.0.0.1:5000/

## Building and running Docker image
An alternative and somewhat easier, way to run the server is to build and run a Docker image for the app.

From the project directory, run this command to build the image:

    docker build -t cberrys2021/nutritiontracker:<tag> .

    #Replace tag with the version you're uploading

    current version:
    docker build -t cberrys2021/nutritiontracker:v2 .

Run this command to run the image:

    docker run -dp 5000:5000 cberrys2021/nutritiontracker:<tag>

    current image:
    docker run -dp 5000:5000 cberrys2021/nutritiontracker:v2

Then go to your navigation browser of your choice and enter
the following URL: http://127.0.0.1:5000/

To confirm that the image is running:

    docker ps -a

To stop the image:

    # Swap <container-id> with the contained id from the running process
    docker stop <container-id>

If you want to replace the image to test your changes, simple delete it and build a new one:

    docker rm <container-id

