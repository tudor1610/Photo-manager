<small>Copyright Brandibur Tudor 2023-2024</small>

# Photo gallery website

### 1. Tools used
* HTML + CSS (for the base template and basic design)
* Flask + Jinja2 (for secondary pages' templates and routing functions)
* Docker

### 2. Functionality
The website consists of 5 different pages ('Home', 'Gallery', 'Upload', 'About Us', 'Login'), each one serving a distinct role.

The `Gallery` is where all photos are displayed, each one under one of the categories:
* Animals
* People
* Nature
* Travel

Everyone who opens the website will be able to see all of the uploaded photos, but in order to upload you have to be logged in. 

In the current version of the website you can login using two different accounts:
		
		Username:			Password:
		Admin				top_secret
		UserOne				One123

Careful, there might be someone else trying to login ;)

### 3. Routing functions

The most important routing functions are `gallery()`, `upload_file()`, `login()`.

The `gallery()` function goes through every directory in the parent directory '/uploads' and saves the URL of each photo in the corresponding array. After that a for loop is used in `gallery.html` to display the photos from each directory.


The `upload_file()` function is responsible for checking if a file has been selected, creating its URL based on the category selected by the user and saving the file in the designated folder.


Lastly, the `login()` function takes the credentials of the user, matches them with the ones in the "ALLOWED_USERS" dictionary and decides if one can login or not.


### 4. 

The command to run the website is:

		docker build -t photo .
		docker run -p 5000:5000 -it photo
