import os

import tornado.wsgi
from sqlalchemy.orm import scoped_session, sessionmaker

from app.models import engine
from app.handlers.home import HomeHandler


class Application(tornado.wsgi.WSGIApplication):
    def __init__(self):
        handlers = [
            (r"/", HomeHandler),
        ]
        settings = dict(
            cookie_secret="super-secret-cookie-string",
            login_url="/login",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies=True,
            debug=True,
        )
        tornado.wsgi.WSGIApplication.__init__(self, handlers, **settings)
        # Have one global connection.
        self.db = scoped_session(sessionmaker(bind=engine))

