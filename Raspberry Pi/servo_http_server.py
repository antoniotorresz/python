from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import event
import servo_hardware

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Action(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime, nullable=True)
    is_activated = db.Column(db.Boolean, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'start_time': self.start_time.isoformat() if self.start_time else None,
            'is_activated': self.is_activated
        }
    
with app.app_context():
    db.create_all()

@event.listens_for(Action.is_activated, 'set')
def on_is_activated_change(target, value, oldvalue, initiator):
    if value:
        print('Activating servo')
        # servo_hardware.move_servo()
    else:
        print('Deactivating servo')
        #servo_hardware.stop_servo()

@app.route('/switch-action', methods=['POST'])
def switch_action():
    last_row = Action.query.order_by(Action.id.desc()).first()
    new_action = Action(is_activated=not last_row.is_activated, start_time=datetime.now())
    db.session.add(new_action)
    db.session.commit()
    return {
        "message": "Action switched",
        "action": new_action.to_dict()
    
    }

@app.route('/init', methods=['GET'])
def init_action_database():
    new_action = Action(is_activated=False, start_time=datetime.now())
    db.session.add(new_action)
    db.session.commit()
    return {
        "message": "Action initialized",
        "action": new_action.to_dict()
    }

@app.route('/')
def home():
    return {
        "total_actions": Action.query.count(),
        "last_action": Action.query.order_by(Action.id.desc()).first().to_dict(),
        "actions": [action.to_dict() for action in Action.query.all()],
        "server_time": f"{datetime.now()}"
    }

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    if not Action.query.first():
        init_action_database()