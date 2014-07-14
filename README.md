This is a [Tornado Web][Tornado Web] project template that is configured
to run as a WSGIApplication. Hence, you cannot use self.flush() or any
asynchronous methodsprovided by the tornado web framework.

###Integrated Third Party Libraries:

- [SQLAlchemy][SQLAlchemy]

### Initialize the db

    $python
    Python 2.7.6 (default, Mar 22 2014, 22:59:56) 
    [GCC 4.8.2] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from app.models import create_all
    >>> create_all()
    >>> 

[SQLAlchemy]: http://www.sqlalchemy.org/
[Tornado Web]: http://www.tornadoweb.org/
