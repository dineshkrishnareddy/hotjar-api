from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config.from_object('config.Config')
db = SQLAlchemy(app)

from views.search import LogSimpleSearch, LogAdvancedSearch

api.add_resource(LogSimpleSearch, '/search/<string:browser>/<string:country>')
api.add_resource(LogAdvancedSearch, '/advanced-search/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
