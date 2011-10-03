#!/usr/bin/env python

# Copyright (c) 2011 Google Inc. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""
Tests that a loadable_module target is built correctly.
"""

import TestGyp

import os
import sys

if sys.platform == 'darwin':
  test = TestGyp.TestGyp(formats=['make', 'xcode'])

  test.run_gyp('test.gyp', chdir='loadable-module')
  test.build('test.gyp', test.ALL, chdir='loadable-module')

  # Binary.
  test.built_file_must_exist(
      'test_loadable_module.plugin/Contents/MacOS/test_loadable_module',
      chdir='loadable-module')

  # Info.plist.
  info_plist = test.built_file_path(
      'test_loadable_module.plugin/Contents/Info.plist',
      chdir='loadable-module')
  test.must_exist(info_plist)
  test.must_contain(info_plist, """
	<key>CFBundleExecutable</key>
	<string>test_loadable_module</string>
""")

  test.pass_test()
