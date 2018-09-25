#!/usr/bin/env python3
# encoding: utf-8
"""
Unit tests for cli
"""
import unittest

from freezegun import freeze_time

from pypistats import cli


class TestCli(unittest.TestCase):
    @freeze_time("2018-09-25")
    def test__last_month(self):
        # Arrange
        # Act
        first, last = cli._last_month()

        # Assert
        self.assertEqual(first, "2018-08-01")
        self.assertEqual(last, "2018-08-31")
