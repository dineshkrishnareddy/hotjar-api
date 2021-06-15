from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from views.documentation import blueprint

app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy(app)
app.config['RESTPLUS_MASK_SWAGGER'] = False

app.register_blueprint(blueprint)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
