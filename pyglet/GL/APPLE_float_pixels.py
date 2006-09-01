
"""APPLE_float_pixels
http://developer.apple.com/opengl/extensions/apple_float_pixels.html
"""

import ctypes as _ctypes
from pyglet.GL import get_function as _get_function
from pyglet.GL import c_ptrdiff_t as _c_ptrdiff_t
GL_HALF_APPLE = 0x140B
GL_COLOR_FLOAT_APPLE = 0x8A0F
GL_RGBA_FLOAT32_APPLE = 0x8814
GL_RGB_FLOAT32_APPLE = 0x8815
GL_ALPHA_FLOAT32_APPLE = 0x8816
GL_INTENSITY_FLOAT32_APPLE = 0x8817
GL_LUMINANCE_FLOAT32_APPLE = 0x8818
GL_LUMINANCE_ALPHA_FLOAT32_APPLE = 0x8819
GL_RGBA_FLOAT16_APPLE = 0x881A
GL_RGB_FLOAT16_APPLE = 0x881B
GL_ALPHA_FLOAT16_APPLE = 0x881C
GL_INTENSITY_FLOAT16_APPLE = 0x881D
GL_LUMINANCE_FLOAT16_APPLE = 0x881E
GL_LUMINANCE_ALPHA_FLOAT16_APPLE = 0x881F
