<small>Copyright Brandibur Tudor 2023-2024</small>

<small> Observatie! 
		In momentul participarii la cursul IA1 faceam parte din grupa 313CA. Acum, am depus cerere la secretariat sa fiu transferat de la grupa 323CA la grupa 322CA, prin urmare s-ar putea sa apar in catalogul lor.</small>

# Tema Informatica Aplicata 1

## Task - Photo gallery website

### 1. Tools used
* Html + CSS (for the base template and basic design)
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

Carefull, there might be somone else trying to login ;)

### 3. Routing functions

The most important routing functions are `gallery()`, `upload_file()`, `login()`.

The `gallery()` function goes through every directory in the parent directory '/uploads' and saves the URL of each photo in the corresponding array. After that a for loop is used in `gallery.html` to display the photos from each directory.


The `upload_file()` function is responsible for checking if a file has been selected, creating its URL based on the category selected by the user and saving the file in the designated folder.


Lastly, the `login()` function thkes the credentials of the user, matches them with the ones in the "ALLOWED_USERS" dictionary and decides if one can login or not.


### 4. 

The command to run the website is:

		docker build -t iap1-tema .
		docker run -p 5000:5000 -it iap1-tema