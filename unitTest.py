try:
    from main import app
    import unittest

except Exception as e:
    print("Some modules are missing {}".format(e))


class FlaskTest(unittest.TestCase):
    # check for response 200
    def test_index(self):
        tester = app.test_client(self)
        response_date = tester.get("/order/13-09-2021")
        statuscode_date = response_date.status_code
        self.assertEqual(statuscode_date, 200)

    # chek for response 400 for no valid date
    def test_date_format(self):
        tester = app.test_client(self)
        response_date = tester.get("/order/13-09-20211")
        statuscode_date = response_date.status_code
        self.assertEqual(statuscode_date, 400)

    # check if content return is json
    def test_index_content(self):
        tester = app.test_client(self)
        response = tester.get("/order/13-09-2021")
        self.assertEqual(response.content_type, "application/json")

    # chek for response 404 for no order

    def test_data_exist(self):
        tester = app.test_client(self)
        response_date = tester.get("/order/13-09-2008")
        statuscode_date = response_date.status_code
        self.assertEqual(statuscode_date, 404)

    # check for data exist

    def test_index_data(self):
        tester = app.test_client(self)
        response = tester.get("/order/13-09-2021")
        self.assertTrue(b'13-09-2021' in response.data)


if __name__ == "__main__":
    unittest.main()
