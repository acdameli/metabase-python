from unittest import TestCase

from metabase import Metabase


class MetabaseTests(TestCase):
    def test_singleton(self):
        """Ensure Metabase acts as a singleton; the same instance is always returned when instantiated."""
        metabase = Metabase(host="", user="", password="")
        metabase1 = Metabase()

        self.assertEqual(metabase, metabase1)
        self.assertEqual(metabase.host, metabase1.host)
        self.assertEqual(Metabase(), Metabase())

    def test_host(self):
        """Ensure Metabase.host adds https:// and trims trailing /."""
        metabase = Metabase(host="example.com/", user="", password="")
        self.assertEqual(metabase.host, "https://example.com")

        del metabase

        metabase = Metabase(host="http://example.com/", user="", password="")
        self.assertEqual(metabase.host, "http://example.com")

    def test_token(self):
        """Ensure Metabase.token returns Metabase._token if not None, else gets a new token."""
        metabase = Metabase(host="example.co.", user="", password="", token="123")
        self.assertEqual(metabase.token, "123")

        # TODO: add test case when token is None

    def test_headers(self):
        """Ensure Metabase.headers returns a dictionary with the token."""
        metabase = Metabase(host="example.com", user="", password="", token="123")
        self.assertDictEqual(metabase.headers, {"X-Metabase-Session": "123"})

    def test_get(self):
        # TODO
        pass

    def test_post(self):
        # TODO
        pass

    def test_put(self):
        # TODO
        pass

    def test_delete(self):
        # TODO
        pass