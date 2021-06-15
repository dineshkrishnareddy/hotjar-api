from flask import abort
from flask_restplus import Namespace, Resource, fields

from exceptions import SearchError
from repository import LogRepository


search_api = Namespace('search', 'Simple Search')

search_api_model = search_api.model('Simple Search', {
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


@search_api.route('/<browser>/<country>/')
@search_api.param('browser', 'Specify browser')
@search_api.param('country', 'Specify country')
class LogSimpleSearch(Resource):
    @search_api.marshal_list_with(search_api_model)
    @search_api.response(400, 'DB error')
    @search_api.response(500, 'Internal Server error')
    def get(self, browser, country):
        """ Simple search endpoint that returns log records. """
        try:
            result = LogRepository().simple_search(browser, country)
        except SearchError as error:
            abort(400, str(error))
        else:
            for row in result:
                row['created'] = str(row['created'])

        return result
