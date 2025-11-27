from flask import Flask
from flask_cors import CORS

import config

from routes_auth import auth_bp
from routes_profiles import profiles_bp
from routes_content import content_bp
from routes_admin import admin_bp

app = Flask(__name__)
app.config["SECRET_KEY"] = config.SECRET_KEY
CORS(app)

# Register routes
app.register_blueprint(auth_bp, url_prefix="/api")
app.register_blueprint(profiles_bp, url_prefix="/api")
app.register_blueprint(content_bp, url_prefix="/api")
app.register_blueprint(admin_bp, url_prefix="/api/admin")

if __name__ == "__main__":
    app.run(debug=True)
