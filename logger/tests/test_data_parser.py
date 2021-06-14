import pytest
from logger.data_parser import PostgresqlParser


@pytest.mark.parametrize("input,expected_output", [
    ({"CONTAINS": {"message": "error"}}, "message LIKE '%%error%%'"),
    ({"IS": {"browser": "chrome"}}, "browser = 'chrome'"),
    ({"NOT": {"IS": {"country": "Italy"}}}, "country != 'Italy'"),
    ({"NOT": {"OR": [{"AND": [{"IS": {"browser": "safari"}},{"IS": {"country": "Germany"}}]},
                     {"CONTAINS": {"message": "stacktrace"}}]}},
     "browser != 'safari' AND country != 'Germany' OR message NOT LIKE '%%stacktrace%%'"),
])
def test_simple_search(input, expected_output):
    """ Test parser """
    # Given/when
    parser = PostgresqlParser()
    actual_output = parser.parse_data(input)

    # Then
    assert actual_output == expected_output
