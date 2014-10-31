import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    @property
    def jinja_env(self):
        return self.application.jinja_env

    @property
    def db(self):
        return self.application.db

    def get_current_user(self):
        user_id = self.get_secure_cookie("user")
        if not user_id:
            return None
        return self.db.query(User).get(user_id)

    def render(self, tmpl, **kwargs):
        template = self.jinja_env.get_template(tmpl)
        self.jinja_env.globals['static_url'] = self.static_url
        self.write(template.render(kwargs))
