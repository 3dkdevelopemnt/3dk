__copyright__ = "Copyright (C) 2013 David Braam - Released under terms of the AGPLv3 License"

import wx._core #We only need the core here, which speeds up the import. As we want to show the splashscreen ASAP.
import time

from Cura.util.resources import getPathForImage

class splashScreen(wx.SplashScreen):
	def __init__(self, callback):
		self.callback = callback
		bitmap = wx.Bitmap(getPathForImage('splash.png'))
		super(splashScreen, self).__init__(bitmap, wx.SPLASH_CENTRE_ON_SCREEN, 0, None)
		wx.CallAfter(self.DoCallback)

	def DoCallback(self):
		time.sleep(4)
		self.callback()
		self.Destroy()
