from data_parser import PostgresqlParser
from exceptions import SearchError
from sqlalchemy.exc import SQLAlchemyError


class LogRepository:
    """ A call to manage all the DB transactions """
    def execute(self, statement):
        from app import db
        records = []
        for r in db.engine.execute(statement):
            records.append(dict(r))
        return records

    def advanced_search(self, validated_input):
        where_stmt = PostgresqlParser().parse_data(validated_input)
        statement = """select * from log where %s""" % where_stmt

        try:
            return self.execute(statement)
        except SQLAlchemyError as e:
            raise SearchError(str(e.__dict__['orig']))

    def simple_search(self, browser, country):
        statement = """select * from log where browser ilike '%s' or country ilike '%s'""" % (browser, country)

        try:
            return self.execute(statement)
        except SQLAlchemyError as e:
            raise SearchError(str(e.__dict__['orig']))
