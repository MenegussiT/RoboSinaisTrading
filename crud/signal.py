from sqlalchemy.orm import Session
from database.models import Signal
from datetime import datetime

def create_signal(db: Session, data: dict):
    new_signal = Signal(
        ativo=data['ativo'],
        horario_entrada=data['horario_entrada'],
        ordem=data['ordem'],
        reentrada_1=data.get('reentrada_1'),
        reentrada_2=data.get('reentrada_2'),
        status='Pendente',
        resultado=None
    )
    db.add(new_signal)
    db.commit()
    db.refresh(new_signal)
    return new_signal

def update_signal_status(db: Session, signal_id: int, status: str, resultado: float = None):
    signal = db.query(Signal).filter(Signal.id == signal_id).first()
    if signal:
        signal.status = status
        signal.resultado = resultado
        db.commit()
        db.refresh(signal)
    return signal

def get_pending_signals(db: Session):
    return db.query(Signal).filter(Signal.status == 'Pendente').all()
