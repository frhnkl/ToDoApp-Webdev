# modul
from flask import Flask, render_template
from config import Config
from app.extension import db, migrate, jwt
from app.frontend import frontendBp
from app.task import taskBp
from app.user import userBp
from app.auth import authBp

# init config untuk db, jwt, dan bp


def create_app(config_class=Config):
    app = Flask(__name__)

    app.config.from_object(config_class)

    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(frontendBp, url_prefix="/")
    app.register_blueprint(taskBp, url_prefix='/api/tasks')
    app.register_blueprint(userBp, url_prefix='/api/users')
    app.register_blueprint(authBp, url_prefix='/api/auth')

    return app
