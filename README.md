# TestPilot
An End-to-End Automation Test Dashboard, Its a Python-based automation framework (UI + API testing) with an integrated web dashboard to display test results, execution history, logs, and screenshots.


# Structure

TestPilot/
├── automation/              # Your automation framework
│   ├── tests/               # UI and API tests
│   ├── utils/               # Reusable test utils (logs, screenshots)
│   ├── reports/             # Allure reports or JSON output
│   ├── requirements.txt
│   └── pytest.ini
│
├── dashboard/               # Django web dashboard
│   ├── testpilot/           # Django main project
│   ├── testresults/         # Django app to display results
│   ├── db.sqlite3
│   ├── manage.py
│   └── requirements.txt
│
├── .gitignore
└── README.md

# Tech Stack Summary

Layer	Tool
UI/API Testing	Python + PyTest + Selenium + Requests
Reports	Allure / JSON (optional integration)
Backend (Dashboard)	Django
Database	SQLite (dev) / PostgreSQL (prod-ready)
Frontend	Django Templates + Bootstrap + Chart.js
CI/CD	GitHub Actions / Jenkins
Bonus (Optional)	Dockerize the setup
