#!/usr/bin/env python3
import unittest
import app

class TestHello(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'\n')

    def test_app_path(self):
        path = 'test'
        rv = self.app.get('/{path}')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'{path}\n')

    def test_app_health(self):
        rv = self.app.get('/health')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'{"status":"OK"}\n')

if __name__ == '__main__':
    import xmlrunner
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
    unittest.main()
