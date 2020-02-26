# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.14.11
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.apis.networking_v1_api import NetworkingV1Api


class TestNetworkingV1Api(unittest.TestCase):
    """ NetworkingV1Api unit test stubs """

    def setUp(self):
        self.api = kubernetes.client.apis.networking_v1_api.NetworkingV1Api()

    def tearDown(self):
        pass

    def test_create_namespaced_network_policy(self):
        """
        Test case for create_namespaced_network_policy

        
        """
        pass

    def test_delete_collection_namespaced_network_policy(self):
        """
        Test case for delete_collection_namespaced_network_policy

        
        """
        pass

    def test_delete_namespaced_network_policy(self):
        """
        Test case for delete_namespaced_network_policy

        
        """
        pass

    def test_get_api_resources(self):
        """
        Test case for get_api_resources

        
        """
        pass

    def test_list_namespaced_network_policy(self):
        """
        Test case for list_namespaced_network_policy

        
        """
        pass

    def test_list_network_policy_for_all_namespaces(self):
        """
        Test case for list_network_policy_for_all_namespaces

        
        """
        pass

    def test_patch_namespaced_network_policy(self):
        """
        Test case for patch_namespaced_network_policy

        
        """
        pass

    def test_read_namespaced_network_policy(self):
        """
        Test case for read_namespaced_network_policy

        
        """
        pass

    def test_replace_namespaced_network_policy(self):
        """
        Test case for replace_namespaced_network_policy

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
