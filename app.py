from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/simulation")
def simulation():
    return render_template("simulation.html")

@app.route("/health")
def health():
    return jsonify({"status": "ok", "application": "Campus Maintenance Simulation"})

@app.route("/api/project-info")
def project_info():
    return jsonify({
        "name": "Campus Maintenance Simulation",
        "purpose": "Compare a paper-style maintenance register with a rule-enforcing database workflow.",
        "features": [
            "Live hour-by-hour simulation",
            "Manual register vs database comparison",
            "Request priority and SLA tracking",
            "Technician capacity and leave handling",
            "Charts, event logs, and workload indicators"
        ]
    })

if __name__ == "__main__":
    app.run(debug=True)
