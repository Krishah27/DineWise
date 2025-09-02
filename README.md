# 🍽️ DineWise — Smart Restaurant Recommender

Discover restaurants you’ll love!
DineWise is an intelligent content-based restaurant recommendation system.
It recommends restaurants based on cuisine, city, and ratings, with a clean dark-themed UI and Google Maps integration.

✨ Features

🎯 Personalized Recommendations — Pick a restaurant you like & get smart similar suggestions.

🏙️ Filter Options — Search by city, cuisine, or minimum rating.

⭐ Hybrid Scoring — Combines cuisines + location + ratings for accuracy.

🗺️ Google Maps Integration — Open restaurants directly on Google Maps.

🎨 Modern Dark UI — Sleek, responsive, and user-friendly frontend.

⚡ Flask Backend — Python Flask serving dataset & powering recommendations.

🛠️ Tech Stack

Frontend: HTML, CSS, JavaScript

Backend: Flask (Python), Flask-CORS

Dataset: JSON (200+ curated Indian restaurants)

Version Control: Git + GitHub

📂 Project Structure
DineWise/
│── backend/
│    ├── app.py                         # Flask backend
│    └── indian_restaurants_realistic.json
│
│── frontend/
│    ├── index.html                     # Main UI
│    └── style.css                      # Styling (dark theme)
│
│── README.md

🚀 Getting Started

Follow these steps to set up the project locally.

1️⃣ Clone the repository
git clone https://github.com/Krishah27/DineWise
cd DineWise

2️⃣ Create a virtual environment (recommended)
python -m venv venv


Activate it:

Windows (PowerShell):

venv\Scripts\activate


macOS/Linux:

source venv/bin/activate

3️⃣ Install dependencies
pip install flask flask-cors pandas

4️⃣ Run the backend server
cd backend
python app.py


Server will start at:
👉 http://127.0.0.1:5000

5️⃣ Open the frontend

Go to the frontend folder.

Open index.html in your browser.

Now you can use DineWise 🎉

📚 Academic Angle

DineWise demonstrates:

Content-based filtering

TF-IDF style token overlap

Hybrid recommendation logic

Practical UI integration with Maps

🤝 Contributing

Pull requests are welcome!
For major changes, please open an issue first to discuss what you’d like to change.

📜 License

This project is licensed under the MIT License.

⭐ If you like this project, don’t forget to give it a star on GitHub!
