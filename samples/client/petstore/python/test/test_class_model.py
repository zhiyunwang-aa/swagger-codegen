# coding: utf-8

"""
    Swagger Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\

    OpenAPI spec version: 1.0.0
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import petstore_api
from petstore_api.rest import ApiException
from petstore_api.models.class_model import ClassModel


class TestClassModel(unittest.TestCase):
    """ ClassModel unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testClassModel(self):
        """
        Test ClassModel
        """
        model = petstore_api.models.class_model.ClassModel()


if __name__ == '__main__':
    unittest.main()