# CS50 Final Project: NoteKeepers


## Description
NoteKeepers is a web application made to digitalize documents and notes. This is my Final Project requirement for the CS50: Introduction to Computer Science course.

## Table of Contents
- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)

## Features
- Login / Register Accounts
- Image/Documents to Text file Conversion
- Text File Viewer
- Edit Account Information
- Preprocessing of the Image before AI OCR Conversion
- User separated text files
- Login Session

## Demo
Youtube Demo: https://www.youtube.com/watch?v=f-KjO366cqU

## Installation
First, download the project file.

Then, install Tesseract for the OCR capabilities
https://tesseract-ocr.github.io/tessdoc/Installation.html

Then, install the necessary libraries used in this project.
`pip install -r requirements.txt`

Then go to the project directory, using cd command

Then lastly, use 'flask run' to start the server and open up the url.

## Usage
### User Registration and Login
First, the user must register an account. Then, they should login to access the full functionalities of the web application. Their account credentials will be saved on a database. Don't worry since the passwords will be hashed and will only be decoded when you're logging in again.

### Landing Page
In the landing page, the user will see cards that briefly explain the function and a button that redirects the user to that function. There are four main functions here: Transcribe, Profile, About NoteKeepers and Account. The website also used simple css design and used the wavy pattern from [Fireship's tutorial](https://youtu.be/lPJVi797Uy0)


### Transcribe Functionality
In the transcribe page, the user can enter their desired file name, a description for organizing the files, and an image file or a pdf file.
This page first process the image using the OpenCV library. Then, Tesseract library will analyze the photo for the texts using AI OCR. After that, spellchecker will check the spelling of the recognized characters. Finally, the results of Tesseract will be written on a text file. An SQL query will also be made to list who owns the said file, its description, and its file name.


### User Profile Page
In this page, you can access buttons to logout as well as edit your account information. On the right side of the page, you can view all the transcriptions you've made. Their File Name and Descriptions will be shown here in a table format. Each entry have a button for viewing and deleting.
Logout button will clear the session and when you try to reload the page, it will redirect you to the login page. Edit Account button will redirect you to the account management page. Pressing the View button of a record of a transcribed file will redirect you to a page the displays the txt file's contents. Lastly, delete button will query the SQL to delete the records of that file as well as delete the file itself.


### Text View Functionality
This page displays the results of the transcription. You can download it and use it. Be wary that Tesseract AI OCR is not perfect. Errors in transcription may happen especially in handwritten notes. Another limitation of the transcription is it cannot detect white space. Line breaks are done when a punctuation marks occur.


### Managing Accounts
This page allows the user to edit their username, full name and password. SQL UPDATE query will be made when the user clicked the submit button. This will change their login credentials.


### About Page
This page is a brief description of the NoteKeepers web app and its goals.


## Technologies Used
- Tesseract
Tesseract is used for Optical Character Recognition. This does most of the heavy lifting in the transcription functionality.
- OpenCV
OpenCV is used to process images so that Tesseract can recognize it easier and more accurate.
- CS50 Library
CS50 Library is used for convenient functions as well as the SQLite3.
- Werkzeug
Werkzeug is used for security. It hashes the passwords and makes the accounts secure.
- Flask
Flask is the primary framework of the web application.
- Jinja
Jinja is used as a templating service to transfer data between the backend and frontend.
- SQLite3
SQLite3 is used to store information to a database such as account information and transcriptions.
- Pillow
Pillow is used to read images.
- Numpy
Numpy is used to help in processing the images.

## Contributing
You can contribute by pointing out errors in the code and suggestions for better implementation and additional features.
I am still a beginner in programming so patience and understanding would be appreciated.


## Acknowledgements
I would like to express my gratitude to the following resources and individuals who have contributed to the development of NoteKeepers:


- [CS50 - Introduction to Computer Science](https://cs50.harvard.edu/) - This project was inspired by the concepts and skills I learned in the CS50 course offered by Harvard University.
- [OpenCV](https://opencv.org/) - The Open Source Computer Vision Library provided essential tools for image preprocessing and manipulation in NoteKeepers.
- [Tesseract](https://github.com/tesseract-ocr/tesseract) - The Tesseract OCR Engine made it possible to extract text from images and documents with high accuracy.
- [Flask](https://flask.palletsprojects.com/) - Flask allowed me to build the backend of the web application.
- [Jinja](https://jinja.palletsprojects.com/) - The Jinja templating engine simplified the process of integrating dynamic content into the web pages.
- [SQLite](https://www.sqlite.org/) - SQLite served as the database system for storing user information and transcribed text files.
- [GitHub](https://github.com/) - Hosting my code on GitHub allowed for version control.

Special thanks to My course instructor, David Malan, for his valuable feedback and support throughout the development of this project.

Without the support of these resources and individuals, NoteKeepers would not have been possible. I am grateful for their assistance and guidance in bringing this project to life.

## Contact
For further inquiries, you can email me at [urmatamsimon@gmail.com](mailto:urmatamsimon@gmail.com).


