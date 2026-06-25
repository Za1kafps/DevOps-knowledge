import io
import unittest
import urllib.error
from unittest.mock import patch

import check_http


class FakeResponse:
    status = 204

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, traceback):
        return False


class CheckHTTPTests(unittest.TestCase):
    @patch("check_http.urllib.request.urlopen", return_value=FakeResponse())
    def test_check_returns_healthy_for_2xx(self, urlopen):
        result = check_http.check("https://example.com/health", timeout=3)

        self.assertTrue(result["healthy"])
        self.assertEqual(result["status"], 204)
        self.assertEqual(urlopen.call_args.kwargs["timeout"], 3)

    @patch("check_http.urllib.request.urlopen")
    def test_check_propagates_transport_error(self, urlopen):
        urlopen.side_effect = urllib.error.URLError("dns failed")

        with self.assertRaises(urllib.error.URLError):
            check_http.check("https://bad.invalid", timeout=1)

    @patch("check_http.check", side_effect=TimeoutError)
    @patch("check_http.parse_args")
    def test_main_returns_transport_error(self, parse_args, _check):
        parse_args.return_value = type(
            "Args",
            (),
            {"url": "https://bad.invalid", "timeout": 1},
        )()

        with patch("sys.stderr", new=io.StringIO()):
            self.assertEqual(check_http.main(), 2)


if __name__ == "__main__":
    unittest.main()
