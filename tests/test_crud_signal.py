# tests/test_crud_signal.py
from crud import signal as crud_signal
from database.models import Signal
from datetime import datetime


def test_create_signal(db_session):
    data = {
        "ativo": "AMAZON",
        "horario_entrada": datetime.strptime("2025-04-05 16:27", "%Y-%m-%d %H:%M"),
        "ordem": "Compra"
    }
    new_signal = crud_signal.create_signal(db_session, data)

    assert new_signal.id is not None
    assert new_signal.ativo == "AMAZON"
