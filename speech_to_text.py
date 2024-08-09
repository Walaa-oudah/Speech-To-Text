import speech_recognition as sr
import mysql.connector
import os

# Initialize the recognizer
recognizer = sr.Recognizer()

def record_and_transcribe():
    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source, duration=3)
        print("Listening...")
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_sphinx(audio)
            print("You said:", text)
            return text
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except sr.UnknownValueError:
            print("Could not understand audio")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    return None

def save_text_to_file(text):
    if text:
        with open("output.txt", "a") as file:
            file.write(text + "\n")
        print("Text written to output.txt")

def insert_text_to_database(text):
    """Insert text into the database."""
    if text:
        try:
            # Connect to the MySQL database
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',  # Replace with your MySQL password
                database='speech_to_text'  # Replace with your database name
            )
            cursor = conn.cursor()

            # Insert the text into the output_txt table
            cursor.execute('INSERT INTO output_txt (output) VALUES (%s)', (text,))
            conn.commit()
            print("Text inserted into the database")

        except mysql.connector.Error as e:
            print(f"Database error: {e}")
        finally:
            if conn:
                conn.close()
                print("Database connection closed")

if __name__ == "__main__":
    print("Starting speech recognition. Press Ctrl+C to exit.")
    try:
        while True:
            transcribed_text = record_and_transcribe()
            save_text_to_file(transcribed_text)
            insert_text_to_database(transcribed_text)
    except KeyboardInterrupt:
        print("\nExiting...")
