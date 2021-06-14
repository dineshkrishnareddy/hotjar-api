class BaseParser:
    """ Abstract Parser class """
    def __init__(self):
        self.mapper = {
            'AND': self.add_operation,
            'OR': self.or_operation,
            'NOT': self.not_operation,
            'IS': self.is_operation,
            'CONTAINS': self.contains_operation,
        }

    def parse_data(self, data):
        raise NotImplementedError

    def add_operation(self, data, negation=False):
        raise NotImplementedError

    def or_operation(self, data, negation=False):
        raise NotImplementedError

    def not_operation(self, data, negation=False):
        raise NotImplementedError

    def is_operation(self, data, negation=False):
        raise NotImplementedError

    def contains_operation(self, data, negation=False):
        raise NotImplementedError


class PostgresqlParser(BaseParser):
    """ Parser for Postgresql that converts a JSON to a where clause statement """
    def parse_data(self, data):
        [(key, value)] = data.items()
        return self.mapper[key](data=value)

    def add_operation(self, data, negation=False):
        """ A grouping operation that adds 'AND' between different conditions """
        result = []
        for dt in data:
            [(key, value)] = dt.items()
            result.append(self.mapper[key](data=value, negation=negation))
        return ' AND '.join(result)

    def or_operation(self, data, negation=False):
        """ A grouping operation that adds 'OR' between different conditions """
        result = []
        for dt in data:
            [(key, value)] = dt.items()
            result.append(self.mapper[key](data=value, negation=negation))
        return ' OR '.join(result)

    def not_operation(self, data, negation=False):
        """ A negation operation that adds negates the condition """
        [(key, value)] = data.items()
        return self.mapper[key](value, not negation)

    def is_operation(self, data, negation=False):
        """ An operation that checks the exact match of the value given """
        [(key, value)] = data.items()
        if not negation:
            return f"{key} = '{value}'"
        return f"{key} != '{value}'"

    def contains_operation(self, data, negation=False):
        """ An operation that checks the partial match of the value given """
        [(key, value)] = data.items()
        if not negation:
            return f"{key} LIKE '%%{value}%%'"
        return f"{key} NOT LIKE '%%{value}%%'"
