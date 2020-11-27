import monitor
import login
from app import app

from login import login as login_blueprint
app.register_blueprint(login_blueprint)

from monitor import monitor_bp as monitor_blueprint
app.register_blueprint(monitor_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
