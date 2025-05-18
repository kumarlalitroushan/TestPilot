import django
import os
import sys
from datetime import datetime

# Setup Django environment
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'dashboard')))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "testpilot.settings")
django.setup()

from dashboard.testresults.models import TestRun, TestCaseResult

def save_results(results):
    run_id = f"Run-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
    run = TestRun.objects.create(run_id=run_id)
    for test in results:
        TestCaseResult.objects.create(
            test_run=run,
            test_name=test['name'],
            status=test['status'],
            log=test.get('log', '')
        )

# Simulated example usage
test_results = [
    {"name": "test_google_title", "status": "passed"},
    {"name": "test_dummy_api", "status": "passed"}
]
save_results(test_results)