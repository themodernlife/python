# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.5.1-660c2a2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v1_namespace_list import V1NamespaceList


class TestV1NamespaceList(unittest.TestCase):
    """ V1NamespaceList unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1NamespaceList(self):
        """
        Test V1NamespaceList
        """
        model = kubernetes.client.models.v1_namespace_list.V1NamespaceList()


if __name__ == '__main__':
    unittest.main()
