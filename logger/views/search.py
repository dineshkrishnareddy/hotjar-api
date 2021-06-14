from sqlalchemy.exc import SQLAlchemyError
from flask import request
from flask_restful import Resource

from exceptions import AdvancedSearchError
from repository import LogRepository


class LogSimpleSearch(Resource):

    def get(self, browser, country):
        """ Simple search endpoint that returns log records. """
        try:
            result = LogRepository().simple_search(browser, country)
        except AdvancedSearchError as error:
            return str(error), 400
        else:
            for row in result:
                row['created'] = str(row['created'])

        return result


class LogAdvancedSearch(Resource):

    def post(self):
        """ Advanced search endpoint that return log records. """
        data = request.json
        input_filter = data['filter']

        try:
            result = LogRepository().advanced_search(input_filter)
        except AdvancedSearchError as error:
            return str(error), 400
        else:
            for row in result:
                row['created'] = str(row['created'])

        return result
