import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
os.environ.setdefault("DATABASE_URL", "sqlite:////tmp/demo.sqlite3")  # ephemeral demo storage
os.environ.setdefault("AUTO_CREATE_TABLES", "true")

from admissions_calling_agent.backend.app import app  # noqa: E402,F401
