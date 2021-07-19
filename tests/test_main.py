# *************************************************************************
#
# Royal Dutch Shell
# __________________
#
# Copyright (c) 2020, Royal Dutch shell. All Rights Reserved.
#
# NOTICE:  All information contained herein is, and remains
# the property of Royal Dutch Shell and its suppliers,
# if any.  The intellectual and technical concepts contained
# herein are proprietary to Royal Dutch Shell
# and its suppliers and may be covered by U.S. and Foreign Patents,
# patents in process, and are protected by trade secret or copyright law.
# Dissemination of this information or reproduction of this material
# is strictly forbidden unless prior written permission is obtained
# from Royal Dutch Shell.
# *************************************************************************

"""
A simple python test for inner source example.
"""

from sample import logic


def test_print():
    """
    Testing the logic actually runs.
    """
    logic.print_statement()
