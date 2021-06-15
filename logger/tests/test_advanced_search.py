from app import app
import json


def test_advanced_search():
    """ Test 200 response on API endpoint """
    # Given
    app.testing = True
    client = app.test_client()
    data = json.dumps({'filter': {"NOT": {"OR": [{"AND": [{"IS": {"browser": "safari"}},{"IS": {"country": "Germany"}}]},
                                                 {"CONTAINS": {"message": "stacktrace"}}]}}})

    # When
    res = client.post(
        '/advanced-search/',
        data=data,
        content_type='application/json',
    )

    # Then
    assert len(res.json) == 100


def test_advanced_search_failure_4xx():
    """ Test 400 response on API endpoint given wrong JSON data """
    # Given
    app.testing = True
    client = app.test_client()
    data = json.dumps({'filter': {"NOT": {"OR": [{"AND": [{"IS": {"browser": "safari"}},{"IS": {"country": "Germany"}}]},
                                                 {"CONTAINS": {"message": "stacktrace"}}]}}})

    res = client.post(
        '/advanced-search/',
        data=data[:-1],
        content_type='application/json',
    )

    assert res.status_code == 400


def test_advanced_search_failure_5xx():
    """ Test 500 response on API endpoint given wrong column name """
    # Given
    app.testing = True
    client = app.test_client()

    # When
    res = client.post(
        '/advanced-search/',
        data=json.dumps({'filter': {"CONTAINS": {"dummy": "error"}}}),
        content_type='application/json',
    )

    # Then
    assert res.status_code == 400
    assert 'column "dummy" does not exist' in str(res.json)
