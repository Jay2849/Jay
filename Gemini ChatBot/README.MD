# Gemini ChatBot

A simple and interactive chatbot application that utilizes the Gemini API to provide natural language processing capabilities. This project allows users to engage in conversations with an AI model, making it suitable for various applications such as customer support, information retrieval, and more.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [API Integration](#api-integration)
- [Contributing](#contributing)
- [License](#license)

## Features

- Interactive chat interface for seamless user experience.
- Utilizes the Gemini API for generating responses.
- Maintains conversation context for better interaction.
- Responsive design for various screen sizes.

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask
- **API**: Google Gemini API
- **Deployment**: Flask server

## Installation

To set up the project locally, follow these steps:

1. **Clone the Repository**
  
   git clone https://github.com/Jay2849/Jay.git
   cd Jay/Gemini ChatBot

2. Set Up Environment
  
   Create a virtual environment (optional but recommended):
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install Dependencies

   Install the required packages using pip:
   pip install -r requirements.txt

4. Configure API Key

  Obtain your Gemini API key and set it in an environment variable or directly in the code (not recommended for production):

  export GEMINI_API_KEY="your_api_key_here"  # For Linux/Mac
  set GEMINI_API_KEY="your_api_key_here"     # For Windows

                                                                                            
Usage
                                                                                            
1. Run the Application

Start the Flask application:    
python app.py

2. Access the Chat Interface

Open your web browser and navigate 'to http://localhost:5000' to interact with the chatbot.


API Integration
                                                                                            
The application communicates with the Gemini API to send user messages and receive responses. The backend handles the API requests and responses, ensuring a smooth interaction between the user and the AI model.

Example of API Request
                                                                                          
response = model.generate_content(user_input)

                                                                                            
Contributing
                                                                                            
Contributions are welcome! If you have suggestions for improvements or new features, please fork the repository and submit a pull request.
