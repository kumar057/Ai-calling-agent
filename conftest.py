import io

import pytest
from openpyxl import Workbook

from admissions_calling_agent.backend.persistence import database

TOKEN = "test-token"


@pytest.fixture(autouse=True)
def env(tmp_path, monkeypatch):
    monkeypatch.setenv("DATABASE_URL", f"sqlite:///{tmp_path/'t.sqlite3'}")
    monkeypatch.setenv("DEV_AUTH_TOKEN", TOKEN)
    monkeypatch.setenv("AUTO_CREATE_TABLES", "true")
    monkeypatch.delenv("LIVE_CALLS_ENABLED", raising=False)
    monkeypatch.delenv("CALLING_MODE", raising=False)
    database.reset_engine()
    yield
    database.reset_engine()


@pytest.fixture
def client():
    from fastapi.testclient import TestClient
    from admissions_calling_agent.backend.app import app
    return TestClient(app)


def headers(role="admin", token=TOKEN):
    return {"X-Dev-Token": token, "X-Dev-Role": role}


def make_xlsx(rows, header=("Name", "Phone", "Source", "Contact Permission", "Course")) -> bytes:
    wb = Workbook()
    ws = wb.active
    ws.append(list(header))
    for r in rows:
        ws.append(list(r))
    buf = io.BytesIO()
    wb.save(buf)
    return buf.getvalue()
