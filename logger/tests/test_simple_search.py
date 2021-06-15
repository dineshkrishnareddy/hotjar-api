from app import app


def test_simple_search():
    app.testing = True
    client = app.test_client()

    res = client.get('/search/browser/philippines/')

    assert len(res.json) == 8

    res = client.get('/search/IE/philippines/')

    assert len(res.json) == 31
