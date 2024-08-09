# Speech-To-Text 

This repository is a python code contains all the supporting project files necessary to work through the speech to text project from start to finish.


# About the Project

This project is centered around building a Python application that converts spoken language into text using speech recognition library and stores this transcribed text into a MySQL database from an outputfile that records everything that has been said by the user . The project is divided into two main functionalities:

1- Recording and Transcribing Speech: Capturing audio from the user and transcribing it into text.

2- Storing the Transcribed Text: Saving the text both locally in a file and in a MySQL database.


### Speech Recognition Purpose:

The purpose of the speech recognition component is to capture spoken words from the user and convert them into text. This text is then processed further for storage.


### Structure:

#### 1. Python Script ('record_and_transcribe' function):

- Audio Capture: Utilizes the speech_recognition library to record audio from a microphone.

- Noise Adjustment: The script adjusts for ambient noise to improve the accuracy of transcription.
  
- Transcription: Converts the recorded audio into text using the Sphinx recognition engine, providing a printed output of what the user said.
  
- Error Handling: Includes robust handling of common errors such as unrecognized speech or connection issues with the speech recognition service.


### Text Storage Purpose:

Once the speech is transcribed into text, the application saves this text in two places: a local file and a MySQL database. This dual-storage ensures data persistence and accessibility.


### Structure:

#### 1. File Storage (save_text_to_file function):

- Local File Output: The transcribed text is appended to a file named output.txt, creating a continuous log of all transcribed speech.

#### 2. Database Storage (insert_text_to_database function):

- MySQL Database Interaction: Connects to a MySQL database named speech_to_text and inserts the transcribed text into a table named output_txt.
  
- Error Handling: Manages potential database connection issues and ensures that the data is correctly inserted and the connection is properly closed.


## Instructions and Navigation

- Install a web server (Apache).

- Install a database (MySQL).

- Use a server-side scripting language (Python).

### [Download and Install XAMPP]: (https://www.apachefriends.org/download.html)

### [Download and Install Visual Studio Code]: (https://code.visualstudio.com/download)


### Step 1: Install Required Libraries:

- Install the speech_recognition library for handling speech-to-text conversion.
  
- Install mysql-connector-python to enable communication with the MySQL database.

### Step 2: Database Configuration:

- Create a MySQL database called speech_to_text.
  
- Define a table named output_txt within this database to store the transcribed speech.


### Step 3: Python Script Execution:

- Run the main Python script to start the speech recognition process. The application will continuously listen for speech, transcribe it, and save the results.

### Step 4: Testing:

- Speak into the microphone and verify that the transcribed text appears both in the output.txt file and in the output_txt table of the MySQL database.


#### The run code will be as shown in the pictures below:

<div> 
   
<img src="https://github.com/user-attachments/assets/13891624-bab9-4723-bb39-7bfb8c6a8c77" width="400" height="200">

<img src="https://github.com/user-attachments/assets/af897491-0fb8-4099-b9a9-68b639f978f2" width="400" height="200">

</div>
   
   
# Summary:

In the Speech-to-Text project, Python is used to convert spoken language into text, which is then stored both locally and in a MySQL database. This project demonstrates the seamless integration of speech recognition and database management, enabling efficient transcription and secure storage of spoken input. The dual-storage approach ensures that all transcriptions are preserved and can be easily retrieved for future use.


### Technologies Used:

•	Python

•	SpeechRecognition Library

•	MySQL

•	XAMPP (for local server and MySQL database)

•	Visual Studio Code


## Thank You!

