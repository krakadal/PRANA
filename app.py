from flask import Flask, render_template, jsonify, make_response
from flask_cors import CORS
import json
import os
import random
import statistics
import sys

app = Flask(__name__)
CORS(app)

# =========================
# PATHS & DIR CHECK
# =========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATE_DIR = os.path.join(BASE_DIR, "state")
STATE_PATH = os.path.join(STATE_DIR, "state.json")

# Автоматично създаване на папка, ако липсва
if not os.path.exists(STATE_DIR):
    os.makedirs(STATE_DIR)
    print(f"[*] Created directory: {STATE_DIR}")

# =========================
# HELPERS
# =========================
def clamp01(x: float) -> float:
    return max(0.0, min(1.0, x))

def inject_neural_drift(data: dict):
    system = data.get("system", {})
    stress = system.get("stress", 0.0)
    if stress < 0.01: return data
    
    data["perceptual_layer"] = {}
    # drift_amplitude e local tuk за сигурност
    drift_amplitude = 0.08
    monte_carlo_samples = 64

    for key in ["fear_index", "entropy"]:
        if key in data:
            val = data[key]
            spread = drift_amplitude * (0.5 + stress)
            samples = [clamp01(val + random.uniform(-spread, spread)) for _ in range(monte_carlo_samples)]
            data["perceptual_layer"][key.split('_')[0]] = {
                "mean": statistics.mean(samples),
                "stdev": statistics.pstdev(samples),
                "samples": samples[:12]
            }
            data[key] = statistics.mean(samples)
    return data

# =========================
# ROUTES
# =========================
@app.route("/")
def index():
    try:
        response = make_response(render_template("monitor.html"))
        response.headers["ngrok-skip-browser-warning"] = "true"
        return response
    except Exception as e:
        return f"Грешка: monitor.html не е намерен в папка templates! ({str(e)})", 404

@app.route("/data")
def get_data():
    if not os.path.exists(STATE_PATH):
        # Създаваме празен стейт, ако го няма, за да не спира работата
        default_state = {"system": {"stress": 0.1}, "fear_index": 0.2, "entropy": 0.1}
        return jsonify(default_state)
    
    try:
        with open(STATE_PATH, "r", encoding="utf-8") as f:
            raw_data = json.load(f)
        processed = inject_neural_drift(raw_data)
        response = jsonify(processed)
        response.headers["ngrok-skip-browser-warning"] = "true"
        return response
    except Exception as e:
        return jsonify({"status": "corrupted", "error": str(e)})

if __name__ == "__main__":
    print("[!] PRANA CORE STARTING ON PORT 7777...")
    app.run(host="0.0.0.0", port=7777, debug=False)