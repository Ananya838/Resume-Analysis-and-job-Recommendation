# Smart Resume Analyzer & Job Recommender

## 📌 Overview

Smart Resume Analyzer & Job Recommender is an AI-driven web application that helps users analyze their resumes and receive personalized job recommendations. The system extracts key information such as skills, education, and experience from uploaded resumes (PDF/DOCX), evaluates the content to highlight strengths and identify skill gaps, and suggests relevant job opportunities based on the user’s profile.

---

## 🚀 Key Features

1. **User Authentication**
   - Secure user sign-up and login
   - Authentication handled using JSON Web Tokens (JWT)

2. **Resume Upload**
   - Upload resumes in **PDF** or **DOCX** format
   - Secure storage and processing

3. **AI-Powered Resume Analysis**
   - Extracts skills, education, and experience using NLP
   - Identifies strengths and potential skill gaps
   - Helps users improve resume quality

4. **Job Recommendations**
   - Suggests job roles tailored to user skills and experience
   - Considers career goals and preferred work location

---

## 🛠️ Tech Stack

### Frontend
- HTML5, CSS3, JavaScript
- Tailwind CSS (via CDN for styling)

### Backend
- Python (Flask) – RESTful API
- MongoDB (PyMongo) – Stores user data and resume details
- PyJWT – Secure authentication using JSON Web Tokens

### Natural Language Processing (NLP)
- nltk
- spacy
- scikit-learn

### Document Processing
- pdfminer.six – PDF resume parsing
- docx2txt – DOCX resume parsing
- pandas – Data manipulation and processing

---

## ⚙️ How the System Works

1. User registers and logs into the application.
2. The user uploads a resume in PDF or DOCX format.
3. Resume text is extracted using document parsing libraries.
4. NLP techniques analyze the resume to extract skills and experience.
5. The system evaluates the resume to identify strengths and skill gaps.
6. Job recommendations are generated based on the analyzed profile.
7. Results are displayed on the user dashboard.

---

project-root/
|
|-- backend/
|   |-- app.py              # Main Flask application
|   |-- requirements.txt   # Backend dependencies
|   |-- routes/             # API routes (auth, resume, jobs)
|   |-- models/             # Database models
|   |-- utils/              # NLP and resume processing logic
|   |-- .env                # Environment variables
|
|-- frontend/
|   |-- index.html          # Landing page
|   |-- login.html          # Login page
|   |-- signup.html         # Signup page
|   |-- dashboard.html     # User dashboard
|   |-- css/                # Styles (Tailwind)
|   |-- js/                 # Client-side JavaScript

---

## 🔐 Environment Variables

Create a `.env` file inside the `backend` directory and add the following:

```env
PORT=5000
MONGO_URI=your_mongodb_connection_string
JWT_SECRET=your_secret_key



# Setup Instructions

### Prerequisites
* Python 3.x
* MongoDB (Local or Atlas)

### Backend Setup
1. Navigate to the `backend` directory:
   ```bash
   cd backend
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure the environment variables:
   * Create a `.env` file in the `backend` directory.
   * Add necessary variables:
     ```env
     PORT=5000
     MONGO_URI=your_mongodb_connection_string
     JWT_SECRET=your_secret_key
     ```
5. Run the Flask application:
   ```bash
   python app.py
   ```
   The API will start running on `http://localhost:5000` (or your configured port).

### Frontend Setup
1. The frontend relies on plain HTML, CSS, and JS (no build step required).
2. Simply open `frontend/index.html` in your web browser.
3. Alternatively, serve the directory using a simple static file server:
   ```bash
   cd frontend
   # Using Python's built-in server
   python -m http.server 8000
   ```
   Then navigate to `http://localhost:8000`.

## Directory Structure
- `backend/`: Contains the Flask server, routes, models, and utility scripts for ML and text extraction.
- `frontend/`: Contains the HTML views (`index.html`, `login.html`, `signup.html`, `dashboard.html`), styling, and client-side JavaScript.








