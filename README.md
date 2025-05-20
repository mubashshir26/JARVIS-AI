Jarvis AI Assistant
A Python-based AI assistant with a polished GUI, built using Tkinter. Jarvis handles text and voice commands to perform tasks like opening websites, playing music, fetching news, and more.
Features

Website Navigation: Open websites like Google, LinkedIn, and YouTube with simple voice or text commands.
Music Playback: Play songs via YouTube links using a predefined music library (e.g., "Jhol", "Fakira", "Mere Mehboob Qayamat Hogi").
News Updates: Fetch the latest news headlines from India using the NewsAPI.
Polished GUI: User-friendly interface built with Tkinter, featuring text and voice input options.
Voice Interaction: Interact with Jarvis using voice commands for a seamless experience.

Tech Stack

Python: Core programming language.
Tkinter: For building the graphical user interface (GUI).
SpeechRecognition: For voice input processing.
pyttsx3: For text-to-speech functionality.
Requests: For fetching news via the NewsAPI.
webbrowser: For opening websites and playing music on YouTube.

Installation
Follow these steps to set up and run the project on your local machine:

Clone the Repository:
git clone https://github.com/<your-username>/Jarvis-AI-Assistant.git
cd Jarvis-AI-Assistant


Install Dependencies:Ensure you have Python installed. Then, install the required libraries using the requirements.txt file:
pip install -r requirements.txt

If you don't have requirements.txt, install the following manually:
pip install SpeechRecognition pyttsx3 PyAudio requests


Set Up the Music Library:Ensure the musiclibrary.py file exists in the project directory with a dictionary of songs and their YouTube links. Example:
music = {
    "jhol": "https://www.youtube.com/watch?v=-2RAq5o5pwc&list=RD-2RAq5o5pwc&start_radio=1",
    "fakira": "https://www.youtube.com/watch?v=eJuoi13hbBc",
    "mere mehboob qayamat hogi": "https://www.youtube.com/watch?v=M6Ul3ASaFLU"
}


Set Up NewsAPI Key:

Obtain an API key from NewsAPI.
Store the API key securely in a .env file in the project directory:NEWS_API_KEY=your_newsapi_key_here


Note: The current code uses a hardcoded API key for simplicity. For production, modify the code to load the key from the .env file using a library like python-dotenv:pip install python-dotenv

Then, in jarvis_with_gui.py:from dotenv import load_dotenv
import os
load_dotenv()
newsapi = os.getenv("NEWS_API_KEY")




Run the Application:
python jarvis_with_gui.py



Usage

Launch the App: Run the script, and a GUI window will open with the title "Jarvis AI Assistant".
Text Commands: Type commands in the input box and press "Send" or hit Enter.
Examples: open google, play jhol, news


Voice Commands: Click the "Speak to Jarvis" button and speak your command.
Examples: Say "open youtube", "play fakira", or "news".


Exit: Type or say "exit" to close the application.

Project Structure

jarvis_with_gui.py: Core logic for voice and text commands with Tkinter GUI.
musiclibrary.py: Handles music playback with a dictionary of songs and YouTube links.
client.py: (Optional) Client-side utilities (sensitive data removed).
requirements.txt: List of dependencies for easy installation.
screenshots/: Folder containing GUI screenshots for documentation.



Add weather API integration for real-time weather updates.
Enhance voice recognition accuracy for better command detection.
Implement .env file support for securely storing API keys.
Add more interactive GUI features like themes or animations.

Contributing
Contributions are welcome! If you'd like to contribute:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes and commit (git commit -m "Add new feature").
Push to your branch (git push origin feature-branch).
Create a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.
Contact
For any questions or suggestions, feel free to reach out:📧 mohd.mubashshir256@gmail.com🔗 LinkedIn
