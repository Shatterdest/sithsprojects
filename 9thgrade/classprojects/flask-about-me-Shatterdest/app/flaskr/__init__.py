import os
from flaskr.static.assets.data import me
from flask import Flask, render_template

me = me()


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

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

    @app.route("/")
    def home():
        # return render_template('index.html')
        return render_template('index.html', me=me)

    @app.route("/interest/<path:interest>")
    def interests(interest):
        def getInterest(var):
            notFound = {
                'Name': '404',
                'Description': '404 Not Found! You might want to go home and try again!',
                'Link': 'https://www.youtube.com/watch?v=o-YBDTqX_ZU'
                }
            for i in me[3]:
                for v in i['List']:
                    if v['Name'] == var:
                        return v
            else:
                return notFound
        return render_template('interest.html', interest=getInterest(interest), me=me)
    return app
