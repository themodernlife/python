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
from kubernetes.client.models.v1_horizontal_pod_autoscaler_status import V1HorizontalPodAutoscalerStatus


class TestV1HorizontalPodAutoscalerStatus(unittest.TestCase):
    """ V1HorizontalPodAutoscalerStatus unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1HorizontalPodAutoscalerStatus(self):
        """
        Test V1HorizontalPodAutoscalerStatus
        """
        model = kubernetes.client.models.v1_horizontal_pod_autoscaler_status.V1HorizontalPodAutoscalerStatus()


if __name__ == '__main__':
    unittest.main()
