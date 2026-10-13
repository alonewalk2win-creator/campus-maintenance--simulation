# CampusCare — Campus Maintenance Simulation

A Flask-based project website for a campus maintenance simulation. It introduces the project and hosts the interactive simulator comparing a paper-style maintenance register with a database-oriented workflow.

## Features

- Responsive project landing page
- Interactive hour-by-hour simulation
- Side-by-side manual register vs database comparison
- Request priority, service-level agreement (SLA), technician workload, and event-log views
- Workload surge and technician-leave scenarios
- JSON health and project-information endpoints

> **Important:** The simulator is a randomized educational model. It does not connect to a live database and is not intended for real campus operations. Its displayed metrics are simulation results, not measured real-world performance.

## Requirements

- Python 3.9 or newer
- pip
- VS Code (recommended) or any Python editor

## Run locally in VS Code

1. Extract this ZIP file.
2. Open the extracted `campus-maintenance-project` folder in VS Code.
3. Open a terminal in that folder.
4. Create a virtual environment:

   **Windows**
   ```powershell
   py -m venv .venv
   .venv\\Scripts\\activate
   ```

   **macOS/Linux**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

5. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

6. Start the server:

   ```bash
   python app.py
   ```

7. Open `http://127.0.0.1:5000` in your browser.

The interactive simulation is at `http://127.0.0.1:5000/simulation`.

## Project structure

```text
campus-maintenance-project/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── Procfile
├── runtime.txt
├── templates/
│   ├── index.html
│   └── simulation.html
└── static/
    └── css/
        └── style.css
```

## Routes

| Route | Purpose |
|---|---|
| `/` | Main project website |
| `/simulation` | Interactive simulation |
| `/health` | Simple health check returning JSON |
| `/api/project-info` | Project description and feature list as JSON |

## Push to GitHub

Create an empty repository on GitHub, then run these commands from this project folder:

```bash
git init
git add .
git commit -m "Add CampusCare maintenance simulation website"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```

Replace the example repository URL with your own GitHub repository URL. Do not commit your virtual environment or secrets.

## Deployment notes

The included `Procfile` supports common Python hosting platforms that use Gunicorn. For deployment, install dependencies and start with `gunicorn app:app`. GitHub itself stores the code; it does not run a Flask server. For a live website, deploy the Flask app to a Python-capable host. The standalone simulation HTML can also be hosted as a static page, but the Flask landing page and API routes require a Python-capable host.

## Customization

- Edit the landing page in `templates/index.html`.
- Edit colors and layout in `static/css/style.css`.
- Edit Flask routes in `app.py`.
- The simulator logic is in `templates/simulation.html`.
