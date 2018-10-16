from unittest import skip

from django.test import TestCase


class FailTestCase(TestCase):

    @skip
    def test_always_fail(self):
        self.fail('This test always fails. For CI/CD testing.')
