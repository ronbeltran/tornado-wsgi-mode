from app.handlers import BaseHandler


class HomeHandler(BaseHandler):
    def get(self):
        self.write("Hello, world!")
