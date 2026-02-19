from flask import Flask
from flask_cors import CORS
from routes.auth_routes import auth_bp
from routes.resume_routes import resume_bp
import os
import nltk

nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")
app = Flask(__name__)
CORS(app)

app.register_blueprint(auth_bp, url_prefix="/api/auth")
app.register_blueprint(resume_bp, url_prefix="/api/resume")

@app.route("/")
def home():
    return {"message": "Resume Analyzer & Job Recommender API running"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

