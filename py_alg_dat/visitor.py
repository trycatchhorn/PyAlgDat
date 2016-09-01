#!/usr/bin/env python

# The MIT License (MIT)
#
# Copyright (c) 2015 by Brian Horn, trycatchhorn@gmail.com.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

"""
Provides a data structure used to model a visitor.
"""

__author__ = "Brian Horn"
__copyright__ = "Copyright (c) 2015 Brian Horn"
__credits__ = "Brian Horn"
__license__ = "MIT"
__version__ = "1.0.2"
__maintainer__ = "Brian Horn"
__email__ = "trycatchhorn@gmail.com"
__status__ = "Prototype"

from abc import abstractmethod

class Visitor(object):

    """
    The interface of a general vistor.
    """

    def __init__(self):
        """
        Constructs a vistor.
        """
        super(Visitor, self).__init__()

    @abstractmethod
    def visit(self, obj):
        """
        The default visit method does nothing.

        @param obj: The object to be visited.
        @type: C{object}
        """
        pass

    @staticmethod
    def is_done():
        """
        The default behaviour of this visitor
        is to always return False, when asked
        if the visitor is done operating.

        @return: False, since the visitor is not done.
        @rtype: C{bool}
        """
        return False

