from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend to communicate with backend

# Sample data: diseases and their top 4 countries
diseases = {
    "Malaria": ["Nigeria", "Democratic Republic of Congo", "Uganda", "Mozambique"],
    "Diabetes": ["China", "India", "USA", "Brazil"],
    "Tuberculosis": ["India", "China", "Indonesia", "Philippines"],
    # Add more diseases and countries
}

# Track selected combinations
selected_combinations = set()

@app.route("/diseases", methods=["GET"])
def get_diseases():
    return jsonify(list(diseases.keys()))

@app.route("/countries/<disease>", methods=["GET"])
def get_countries(disease):
    return jsonify(diseases.get(disease, []))

@app.route("/select", methods=["POST"])
def select_combination():
    data = request.json
    disease = data.get("disease")
    country = data.get("country")
    combination = f"{disease}:{country}"

    if combination in selected_combinations:
        return jsonify({"error": "This combination is already taken"}), 400

    selected_combinations.add(combination)
    return jsonify({"success": True})

if __name__ == "__main__":
    app.run(debug=True)
