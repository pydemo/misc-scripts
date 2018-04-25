import wx
from wx.lib.scrolledpanel import ScrolledPanel

import wx.lib.scrolledpanel as scrolled

text = "one two buckle my shoe three four shut the door five six pick up sticks seven eight lay them straight nine ten big fat hen"




########################################################################
class MyPanel(ScrolledPanel):
	""""""

	#----------------------------------------------------------------------
	def __init__(self, parent, size, pos,style):
		"""Constructor"""
		ScrolledPanel.__init__(self, parent, size=size, pos=pos,style=style )

		self.mainsizer = wx.BoxSizer(wx.VERTICAL)

		add_btn = wx.Button(self, label="Add")
		add_btn.Bind(wx.EVT_BUTTON, self.onAdd)
		self.mainsizer.Add(add_btn, 0, wx.ALL, 5)
		self.SetSizer( self.mainsizer )
		#self.mainsizer.Fit(panel)
		self.mainsizer.Fit(self)
		self.mainsizer.Layout()
		self.SetAutoLayout(1)
		self.SetupScrolling()


	#----------------------------------------------------------------------
	def onAdd(self, event):
		""""""
		gen_sizer = wx.BoxSizer(wx.HORIZONTAL)

		txt = wx.TextCtrl(self, size=(600, -1))
		gen_sizer.Add(txt, 0, wx.ALL, 5)

		browse_btn = wx.Button(self, label='Browse')
		browse_evt = lambda evt, ctrl=txt: self.onBrowse(evt, ctrl)
		browse_btn.Bind(wx.EVT_BUTTON, browse_evt)
		gen_sizer.Add(browse_btn, 0, wx.ALL, 5)
		self.mainsizer.Prepend(gen_sizer, 0, wx.ALL, 5)
		self.mainsizer.Layout()


	#----------------------------------------------------------------------
	def onBrowse(self, event, ctrl):
		""""""
		wildcard = "Python source (*.py)|*.py|" \
			"All files (*.*)|*.*"
		dlg = wx.FileDialog(self, message="Choose a file",
							defaultFile="", wildcard=wildcard,
							style=wx.OPEN | wx.CHANGE_DIR)
		if dlg.ShowModal() == wx.ID_OK:
			path = dlg.GetPath()
			ctrl.SetValue(path)
		dlg.Destroy()


class TestPanel(scrolled.ScrolledPanel):
	def __init__(self, parent, log=None):
		self.log = log
		scrolled.ScrolledPanel.__init__(self, parent, -1)

		vbox = wx.BoxSizer(wx.VERTICAL)
		desc = wx.StaticText(self, -1,
							"ScrolledPanel extends wx.ScrolledWindow, adding all "
							"the necessary bits to set up scroll handling for you.\n\n"
							"Here are three fixed size examples of its use. The "
							"demo panel for this sample is also using it -- the \nwxStaticLine "
							"below is intentionally made too long so a scrollbar will be "
							"activated."
							)
		desc.SetForegroundColour("Blue")
		vbox.Add(desc, 0, wx.ALIGN_LEFT|wx.ALL, 5)
		vbox.Add(wx.StaticLine(self, -1, size=(1024,-1)), 0, wx.ALL, 5)
		vbox.Add((20,20))

		words = text.split()

		self.panel1=panel1 = scrolled.ScrolledPanel(self, -1, size=(140, 300),
								 style = wx.TAB_TRAVERSAL|wx.SUNKEN_BORDER, name="panel1" )
		self.fgs1=fgs1 = wx.FlexGridSizer(cols=2, vgap=4, hgap=4)

		for word in words:
			label = wx.StaticText(panel1, -1, word+":")

			# A test for scrolling with a too big control
			#if word == "three":
			#    tc = wx.TextCtrl(panel1, -1, word, size=(150,-1))
			#else:
			#    tc = wx.TextCtrl(panel1, -1, word, size=(50,-1))

			tc = wx.TextCtrl(panel1, -1, word, size=(50,-1))

			fgs1.Add(label, flag=wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL | wx.LEFT, border=10)
			fgs1.Add(tc, flag=wx.RIGHT, border=10)

		panel1.SetSizer( fgs1 )
		panel1.SetAutoLayout(1)
		panel1.SetupScrolling()



		hbox = wx.BoxSizer(wx.HORIZONTAL)
		hbox.Add((20,20))
		hbox.Add(panel1, 0, wx.FIXED_MINSIZE)
		hbox.Add((40, 10))
		add_btn = wx.Button(self, label="Add")
		add_btn.Bind(wx.EVT_BUTTON, self.onAdd)
		hbox.Add(add_btn, 0, wx.ALL, 5)
		



		vbox.Add(hbox, 0)
		self.SetSizer(vbox)
		self.SetAutoLayout(1)
		self.SetupScrolling()

	#----------------------------------------------------------------------
	def onAdd(self, event):	
		""""""
		word='test'
		label = wx.StaticText(self.panel1, -1, word+":")
		tc = wx.TextCtrl(self.panel1, -1, word, size=(50,-1))
		self.fgs1.Add(label, flag=wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL | wx.LEFT, border=10)
		self.fgs1.Add(tc, flag=wx.RIGHT, border=10)
		#self.fgs1.Fit(self.panel1)
		#self.panel1.Layout()
		#self.panel1.SetAutoLayout(1)
		#self.panel1.SetupScrolling()
		self.panel1.FitInside()
		self.panel1.Scroll(-1,self.GetClientSize()[1])		
		if 0:
			gen_sizer = wx.BoxSizer(wx.HORIZONTAL)

			txt = wx.TextCtrl(self, size=(600, -1))
			gen_sizer.Add(txt, 0, wx.ALL, 5)

			browse_btn = wx.Button(self, label='Browse')
			browse_evt = lambda evt, ctrl=txt: self.onBrowse(evt, ctrl)
			browse_btn.Bind(wx.EVT_BUTTON, browse_evt)
			gen_sizer.Add(browse_btn, 0, wx.ALL, 5)
			self.mainsizer.Prepend(gen_sizer, 0, wx.ALL, 5)
			self.mainsizer.Layout()
		
		
########################################################################
class MainFrame(wx.Frame):
	""""""

	#----------------------------------------------------------------------
	def __init__(self):
		"""Constructor"""
		wx.Frame.__init__(self, None, title='Dynamic file browser',
						  size=(800,500))
		#panel = MyPanel(self, size=(800,300), pos=(0,28),style=wx.SIMPLE_BORDER)
		panel = TestPanel(self, log=None)
		self.Show()

if __name__ == '__main__':
	app = wx.App(False)
	frame = MainFrame()
	app.MainLoop()
