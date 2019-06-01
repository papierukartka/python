"""
An attempt to understand python mocking mechanism, written with the tutorial
Point of reference: https://www.toptal.com/python/an-introduction-to-mocking-in-python
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from simple_delete_function import RemovalService, UploadService

import mock
import unittest


class RemovalServiceTestCase(unittest.TestCase):

    @mock.patch('simple_delete_function.os.path') # this is an :insider:
    @mock.patch('simple_delete_function.os')
    def test_rm(self, mock_os, mock_path):
        # instantiate our service
        reference = RemovalService()

        # set up the mock
        mock_path.isfile.return_value = False

        reference.rm("anypath")

        # test that remove call was not called
        self.assertFalse(mock_os.remove.called, "Failed not to remove the file if not present.")

        # make the file exist
        mock_path.isfile.return_value = True

        reference.rm('any path')

        # test that rm called os.remove with the right parameters
        mock_os.remove.assert_called_with("any path")


class UploadServiceTestCase(unittest.TestCase):

    def test_upload_complete(self):
        # build our dependencies
        mock_removal_service = mock.create_autospec(RemovalService)
        reference = UploadService(mock_removal_service)

        # call upload_complete, which should in turn call rm
        reference.upload_complete('my uploaded file')

        # check that it called the method of OUR RemovalService
        mock_removal_service.rm.assert_called_with('my uploaded file')
