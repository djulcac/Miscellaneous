import datetime
import random

from flask import Flask, request, g, redirect, url_for, session, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session

from .settings import Settings

engine = create_engine(Settings.config['db']['uri'],echo=False, future=True)
# engine = create_engine(Settings.config['postgres']['uri'])
Base = declarative_base()
db = Session(engine)

def init_app(debug=False):
    """Init application"""
    print('init_app',__name__)

    app = Flask(__name__)
    app.debug = debug
    app.config['SECRET_KEY'] = Settings.config['flask']['SECRET_KEY']

    # crear el modelo en caso que no existe
    from . import models
    # Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    
    # from .settings import Api
    # app.register_blueprint(Api.app_routes)
    from .settings import Routes
    app.register_blueprint(Routes.app_routes)

    @app.before_request
    def before_request():
        try:
            g.vg = {
                # 'alerts' : [],
                # 'login' : res['login'],
                # 'endpoints' : res['endpoints'],
                # 'user' : res['user'],
                'log': str(int(datetime.datetime.now().timestamp()*1000))+'-'+str(random.randrange(123456789))
            }
            # print('ok')
        except Exception as errors:
            return render_template('error.html')

    # despues de la consulta si todo va bien
    @app.after_request
    def after_request(response):
        print('after_request 2')
        return response

    # despues de la consulta aunque falla
    @app.teardown_request
    def teardown_request(response):
        print('teardown_request 3')
        return response
    
    return app