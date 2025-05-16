import os

from flask import Flask




def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    UPLOAD_FOLDER = "./upload"
    app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)


    from . import home
    app.register_blueprint(home.bp)
    app.add_url_rule('/', endpoint='index')

    from . import admin
    app.register_blueprint(admin.bp)

    from . import about
    app.register_blueprint(about.bp)

    from . import contact_us
    app.register_blueprint(contact_us.bp)

    from . import services
    app.register_blueprint(services.bp)

    from . import testimonials
    app.register_blueprint(testimonials.bp)

    from . import dashboard
    app.register_blueprint(dashboard.bp)

    from . import store
    app.register_blueprint(store.bp)

    from . import resources
    app.register_blueprint(resources.bp)

    from . import faq
    app.register_blueprint(faq.bp)

    from . import support
    app.register_blueprint(support.bp)

    from . import community
    app.register_blueprint(community.bp)

    return app