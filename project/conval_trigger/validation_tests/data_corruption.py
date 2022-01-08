# -*- coding: utf-8 -*-
# Copyright 2021 Intel Corporation All Rights Reserved.
# Author: ravitejax.pamujula@intel.com

import common_utility


class Video_Stream_720p():

	def setUp(self):
		print("calling setUp ")
		return True

	def run(self):
		print("Creating run")
		return True


	def tearDown(self):
		print("Creating tearDown")
		return True


if __name__ == '__main__':
	obj=Video_Stream_720p()
	common_utility.run_tests(obj)