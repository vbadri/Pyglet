#!/usr/bin/env python

'''Testing hex map debug rendering.

Press "s" to switch between lines and checkered display.

Press escape or close the window to finish the test.
'''

__docformat__ = 'restructuredtext'
__version__ = '$Id$'

import unittest
from render_base import RenderBase, DummyImage
import pyglet.scene2d

class HexFlatDebugTest(RenderBase):
    def test_main(self):
        m = pyglet.scene2d.HexMap(32, images=[[DummyImage()]*10]*10)
        self.run_test(m)

if __name__ == '__main__':
    unittest.main()