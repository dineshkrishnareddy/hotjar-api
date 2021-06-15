from flask import Blueprint
from flask_restplus import Api

from views.simple_search import search_api as simple_search
from views.advanced_search import search_api as advanced_search

blueprint = Blueprint('doc', __name__)

api_extension = Api(
    blueprint,
    title='Hotjar Task',
    version='1.0',
    description='API documentation for endpoints',
    doc='/doc'
)

api_extension.add_namespace(simple_search)
api_extension.add_namespace(advanced_search)
