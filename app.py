#imports for website
from flask import Flask, render_template, request, session, redirect, flash, send_from_directory
from flask_session import Session
# import os
# #imports for password hashing
# from werkzeug.security import check_password_hash, generate_password_hash
# from werkzeug.exceptions import abort
# from functools import wraps
# #imports for SQL
# from cs50 import SQL
# #imports for OCR
# import cv2
# import numpy as np
# import pytesseract
# from PIL import Image
# from io import BytesIO
# from spellchecker import SpellChecker
# import string

# Configure application
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["STATIC_FOLDER"] = "static"

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# # Configure CS50 Library to use SQLite database
# db = SQL("sqlite:///finalProject.db")

# #Login Requirement Parameter Function
# def login_required(view_func):
#     @wraps(view_func)
#     def wrapped_view(*args, **kwargs):
#         if 'user_id' not in session:
#             return redirect('/login')
#         return view_func(*args, **kwargs)
#     return wrapped_view

# def check_username(username):
#     userData = db.execute("SELECT * FROM users")
#     for user in userData:
#         if user["username"] == username:
#             return True

# def check_password(password):
#     if len(password) < 8:
#         return False
#     else:
#         if not any(char.isdigit() for char in password):
#             return False
#         elif not any(char.isupper() for char in password):
#             return False
#         elif not any(char.islower() for char in password):
#             return False
#         else:
#             return True

# def check_same_password(password):
#     userData = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
#     if check_password_hash(userData[0]["password"], password):
#         return True
#     else:
#         return False

# def image_preprocessing(image):
#     # Convert the image to grayscale
#     gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     # Apply Gaussian blur to reduce noise and smooth the image
#     blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

#     # Apply adaptive thresholding to binarize the image
#     threshold_image = cv2.adaptiveThreshold(
#         blurred_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2
#     )

#     # Perform morphological operations to further clean the image
#     kernel = np.ones((3, 3), np.uint8)
#     processed_image = cv2.erode(threshold_image, kernel, iterations=1)
#     processed_image = cv2.dilate(processed_image, kernel, iterations=1)

#     return processed_image

# # Custom spell checking function that retains capitalization
# def custom_spell_check(text):
#     spell = SpellChecker()
#     words = text.split()
#     corrected_words = [spell.correction(word) if word.islower() else word for word in words]
#     corrected_text = " ".join(corrected_words)
#     return corrected_text


@app.route("/")
@login_required
def index():
    return render_template("index.html")


# @app.route("/login", methods=["GET", "POST"])
# def login():
#     #Login Logic from Finance Problem Set
#     if request.method == "POST":
#         loginUsername = request.form.get("username")
#         loginPassword = request.form.get("password")
#         #Check if forms is empty
#         if loginUsername == "" or loginPassword == "":
#             return abort(403,'Please fill in all fields')
#         database=db.execute("SELECT * FROM users WHERE username = ?", loginUsername)
#         if len(database) != 0 and check_password_hash(database[0]["password"], loginPassword):
#             session["user_id"] = database[0]["id"]
#             return redirect("/")
#         else :
#             return abort(403,'Incorrect username or password')
#     else:
#         return render_template("login.html")

# @app.route("/logout", methods=["GET", "POST"])
# @login_required
# def logout():
#     session.clear()
#     return redirect("/login")

# @app.route("/register", methods=["GET", "POST"])
# def register():
#     #Inserting new user into database
#     if request.method == "POST":
#         registerFullName = request.form.get("fullname")
#         registerUsername = request.form.get("username")
#         registerPassword = generate_password_hash(request.form.get("password"))
#         #Check if forms is empty
#         if registerFullName == "" or registerUsername == "" or registerPassword == "":
#             return abort(403,'Please fill in all fields')
#         #Check if username already exists
#         if check_username(registerUsername):
#             return abort(403,'Username already exists')
#         #Check if password is valid
#         if not check_password(request.form.get("password")):
#             return abort(403,'Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter and one number')

#         db.execute("INSERT INTO users (username, password, full_name) VALUES (?, ?, ?)",registerUsername, registerPassword, registerFullName)
#         return redirect("/login")
#     else:
#         return render_template("register.html")

# import pytesseract
# from spellchecker import SpellChecker

# # ...

# @app.route("/transcribe", methods=["GET", "POST"])
# @login_required
# def transcribe():
#     if request.method == "POST":
#         # Get data from the HTML form
#         filename = request.form.get("filename")
#         description = request.form.get("description")
#         fileTranscribe = request.files["fileTranscribe"]

#         # Check if the filename is empty
#         if filename == "":
#             return abort(403, "Please enter a filename")

#         # Check if the file is empty
#         if fileTranscribe.filename == "":
#             return abort(403, "Please select a file to upload")

#         # Check if the file is a valid image
#         if not fileTranscribe.filename.endswith(".jpg") and not fileTranscribe.filename.endswith(".jpeg") and not fileTranscribe.filename.endswith(".png") and not fileTranscribe.filename.endswith(".bmp"):
#             return abort(403, "Please upload a valid image file")

#         # Check if description is empty
#         if description == "":
#             return abort(403, "Please enter a description")
#         # Preprocess the image
#         image = cv2.imdecode(np.frombuffer(fileTranscribe.read(), np.uint8), cv2.IMREAD_COLOR)
#         processed_image = image_preprocessing(image)

#         # Convert the processed image back to binary data
#         _, processed_image_data = cv2.imencode(".jpg", processed_image)
#         processed_image_bytes = BytesIO(processed_image_data)

#         # Convert the binary data to a PIL Image object
#         image_pil = Image.open(processed_image_bytes)

#         # Perform OCR on the image
#         recognized_text = pytesseract.image_to_string(image_pil, lang="eng")
#         print(recognized_text)

#         # Check if OCR output is empty
#         if recognized_text == "":
#             return abort(403, "Unable to recognize text in the image")

#         # Perform spell checking on the OCR output with line breaks
#         corrected_text = custom_spell_check(recognized_text)
#         corrected_text_with_linebreaks = ""
#         for char in corrected_text:
#             corrected_text_with_linebreaks += char
#             if char in string.punctuation:
#                 corrected_text_with_linebreaks += "\n"
#         print(corrected_text_with_linebreaks)

#         # Check if spell checking output is empty
#         if corrected_text_with_linebreaks == "":
#             return abort(403, "Unable to correct the text")

#         # Set the output file path with the desired filename and folder
#         output_file_path = f"transcribed_notes/{filename}.txt"

#         # Save the recognized text to the text file in the "transcribed_notes" folder
#         with open(output_file_path, "w", encoding="utf-8") as file:
#             file.write(corrected_text_with_linebreaks)

#         # Insert the transcription details into the database
#         db.execute("INSERT INTO transcription (user_id, file_name, description) VALUES (?, ?, ?)",
#                     session["user_id"], filename, description)

#         flash("File successfully uploaded and transcribed!")
#         return redirect("/")
#     else:
#         return render_template("ocr.html")


# @app.route("/profile", methods=["GET", "POST"])
# @login_required
# def profile():

#     if request.method == "POST":
#         return redirect("/")
#     else:
#         transcriptionData = db.execute("SELECT * FROM transcription WHERE user_id = ?", session["user_id"])
#         userData = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
#         return render_template("profile.html",transcriptions=transcriptionData,userData=userData)

# @app.route("/account", methods=["GET", "POST"])
# @login_required
# def account():
#     if request.method == "POST":
#         # Get data from the HTML form
#         newUsername = request.form.get("username")
#         oldPassword = request.form.get("oldPassword")
#         newPassword = request.form.get("newPassword")
#         newFullName = request.form.get("fullname")
#         #Check if forms is empty
#         if newUsername == "" or newPassword == "" or newFullName == "":
#             return abort(403,'Please fill in all fields')
#         #Check if old password is correct
#         if check_same_password(oldPassword) == False:
#             return abort(403,'Incorrect password')
#         #Check if username already exists
#         if check_username(newUsername):
#             return abort(403,'Username already exists')
#         #Check if password is valid
#         if not check_password(newPassword):
#             return abort(403,'Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter and one number')
#         # Update the user's details in the database
#         db.execute("UPDATE users SET username = ?, password = ?, full_name = ? WHERE id = ?",
#                     newUsername, generate_password_hash(newPassword), newFullName, session["user_id"])
#         return redirect("/")
#     else:
#         userData = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
#         return render_template("account.html",userData=userData)

# @app.route("/transcripted", methods=["POST"])
# @login_required
# def transcripted():
#     if request.method == "POST":
#         # Get data from the HTML form
#         fileId = int(request.form.get("transcription_id"))  # Convert to integer
#         # Check database for the filename
#         userFile = db.execute("SELECT file_name FROM transcription WHERE user_id = ? AND id = ?", session["user_id"], fileId)
#         if userFile:
#             filename = userFile[0]["file_name"]  # Access the first row's "file_name" column
#             try:
#                 # Read the text file
#                 with open(f"transcribed_notes/{filename}.txt", 'r') as file:
#                     text = file.read()
#                 # Render HTML and pass the text to the template
#                 return render_template("transcripted.html", text=text, file_name=filename)
#             except FileNotFoundError:
#                 return abort(404, 'File not found')
#             except Exception as e:
#                 return abort(500, f"Error reading the file: {str(e)}")
#         else:
#             return abort(404, 'File not found')
#     else:
#         return abort(403, 'Method not allowed')

# @app.route('/download/<filename>', methods=['GET'])
# @login_required
# def download_file(filename):
#     # Set the directory path where the files are saved
#     directory = 'transcribed_notes'
#     try:
#         return send_from_directory(directory, f"{filename}.txt", as_attachment=True)
#     except FileNotFoundError:
#         return abort(404, 'File not found')
#     except Exception as e:
#         return abort(500, f"Error downloading the file: {str(e)}")

# @app.route("/about", methods=["GET"])
# def about():
#     return render_template("about.html")

# @app.route("/deleteTranscription", methods=["POST"])
# @login_required
# def deleteTranscription():
#     if request.method == "POST":
#         # Get data from the HTML form
#         fileId = int(request.form.get("transcription_id"))  # Convert to integer
#         # Check database for the filename
#         userFile = db.execute("SELECT file_name FROM transcription WHERE user_id = ? AND id = ?", session["user_id"], fileId)
#         if userFile:
#             filename = userFile[0]["file_name"]  # Access the first row's "file_name" column
#             try:
#                 # Delete the text file
#                 db.execute("DELETE FROM transcription WHERE user_id = ? AND id = ?", session["user_id"], fileId)
#                 # Remove the file from the directory
#                 file_path = os.path.join("transcribed_notes", filename + ".txt")
#                 if os.path.exists(file_path):
#                     os.remove(file_path)
#                 else:
#                     return abort(404, 'File not found')
#                 # Redirect to the profile page after successful deletion
#                 return redirect("/profile")
#             except FileNotFoundError:
#                 return abort(404, 'File not found')
#             except Exception as e:
#                 return abort(500, f"Error deleting the file: {str(e)}")
#         else:
#             return abort(404, 'File not found')
#     else:
#         return abort(403, 'Method not allowed')