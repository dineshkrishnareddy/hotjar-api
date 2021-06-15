from flask import abort
from flask import request
from flask_restplus import Namespace, Resource, fields, reqparse

from exceptions import SearchError
from repository import LogRepository


search_api = Namespace('advanced-search', 'Advanced Search')

search_api_model = search_api.model('Advanced Search', {
    'created': fields.String(
        readonly=True,
        description='created date'
    ),
    'browser': fields.String(
        readonly=True,
        description='browser info'
    ),
    'country': fields.String(
        readonly=True,
        description='country info'
    ),
    'message': fields.String(
        readonly=True,
        description='message'
    )
})

post_parser = reqparse.RequestParser()
post_parser.add_argument('filter',  type=str, help='filter', location='json')


@search_api.route('/')
class LogAdvancedSearch(Resource):
    @search_api.expect(post_parser)
    @search_api.marshal_list_with(search_api_model)
    @search_api.response(400, 'DB error')
    @search_api.response(500, 'Internal Server error')
    def post(self):
        """ Advanced search endpoint that return log records. """
        data = request.json
        input_filter = data['filter']

        try:
            result = LogRepository().advanced_search(input_filter)
        except SearchError as error:
            abort(400, str(error))
        else:
            for row in result:
                row['created'] = str(row['created'])

        return result
