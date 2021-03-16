## Nutrition-Tracker
Database app to track users meals and nutrition intake

# Start server

Clone the repo

    git clone https://github.com/ClusterberrySquirrels/Nutrition-Tracker.git

From outside the project folder, create and activate the virtual Python environment. You'll have to install required packages in the virtual environment from

    python3 -m venv env
    source env/bin/activate
    pip install -r requirements.txt

Run the follwing command to set your environment variables for the Flask app:

    export FLASK_APP=NutritionTracker
    export FLASK_DEBUG=1

Run the program

    flask run

# Running Tests

Disable Flask debug mode

    export FLASK_DEBUG=0

Run pytest with coverage

    pytest -cov=NutritionTracker

Then go to your navigation browser of your choice and enter 
the following URL: http://127.0.0.1:5000/

## Building and running Docker image
An alternative, and somewhat easier, way to run the server is to build and run a Docker image for the app.

From the project directory, run this command to build the image:

    docker build -t cberrys2021/nutritiontracker:<tag> .
    #Replace tag with the version you're uploading

Run this command to run the image:

    docker run -dp 5000:5000 cberrys2021/nutritiontracker:<tag>

To confirm that the image is running:

    docker ps -a

To stop the image:

    # Swap <container-id> with the contained id from the running process
    docker stop <container-id>

If you want to replace the image to test your changes, simple delete it and build a new one:

    docker rm <container-id

