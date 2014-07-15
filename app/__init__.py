import os

import tornado.wsgi
from sqlalchemy.orm import scoped_session, sessionmaker
from jinja2 import Environment, FileSystemLoader

from app.models import engine
from app.handlers.home import HomeHandler


class Application(tornado.wsgi.WSGIApplication):
    def __init__(self):
        handlers = [
            (r"/", HomeHandler),
        ]
        template_path = os.path.join(os.path.dirname(__file__), "templates")
        static_path = os.path.join(os.path.dirname(__file__), "static")
        settings = dict(
            cookie_secret="super-secret-cookie-string",
            login_url="/login",
            template_path=template_path,
            static_path=static_path,
            xsrf_cookies=True,
            debug=True,
        )
        tornado.wsgi.WSGIApplication.__init__(self, handlers, **settings)
        # Have one global connection.
        self.db = scoped_session(sessionmaker(bind=engine))
        self.jinja_env = Environment(loader=FileSystemLoader(template_path))
