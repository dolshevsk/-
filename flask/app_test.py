import app
import unittest


class BasicTestCase(unittest.TestCase):

    # Exercise 6
    def setup(self):
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()

    def test_ping(self):
        client = app.app.test_client(self)
        response = client.get('/ping')
        self.assertEqual(response.status_code, 200)
        assert b"Cats Service" in response.data
        for _ in range(600):
            response = client.get('/ping')
        self.assertEqual(response.status_code, 429)

    def test_cats(self):
        client = app.app.test_client(self)
        response = client.get('/cats')
        self.assertEqual(response.status_code, 200)
        response = client.get('/cats?attribute=name&order=asc')
        self.assertEqual(response.status_code, 200)
        response = client.get('/cats?offset=10&limit=10')
        self.assertEqual(response.status_code, 200)
        response = client.get('/cats?offset=-10')
        self.assertEqual(response.status_code, 400)

    def test_add_cat(self):
        client = app.app.test_client(self)
        rv = client.post('/cat', data="Try to post invalid data")
        assert b'json format' in rv.data

        rv = client.post('/cat', data="{\"name\": \"Tihon\", \"color\": \"red & white\", "
                                      "\"tail_length\": 15, \"whiskers_length\": 12}")
        assert b'name already exists' in rv.data

        rv = client.post('/cat', data="{\"name\": 2213, \"color\": \"red & white\", "
                                      "\"tail_length\": 15, \"whiskers_length\": 12}")
        assert b'invalid name' in rv.data

        rv = client.post('/cat', data="{\"name\": \"Tomas\", \"color\": \"2134\", "
                                      "\"tail_length\": 15, \"whiskers_length\": 12}")
        assert b'this color is not allowed' in rv.data

        rv = client.post('/cat', data="{\"name\": \"Tomas\", \"color\": \"red & white\", "
                                      "\"tail_length\": -15, \"whiskers_length\": -12}")
        assert b'integers should be positive' in rv.data


if __name__ == '__main__':
    unittest.main()