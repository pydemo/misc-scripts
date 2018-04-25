import wx

########################################################################
class TestPopup(wx.PopupWindow):
	""""""

	#----------------------------------------------------------------------
	def __init__(self, parent, style):
		"""Constructor"""
		wx.PopupWindow.__init__(self, parent, style)

		panel = wx.Panel(self)
		self.panel = panel
		panel.SetBackgroundColour("CADET BLUE")

		if 1:
			import keyword
			self.lb = wx.ListBox(panel, -1, choices = keyword.kwlist)
			#sz = self.lb.GetBestSize()
			self.SetSize((150, 75)) #sz)
			self.lb.SetSize(self.GetClientSize())
			self.lb.SetFocus()
			self.Bind(wx.EVT_LISTBOX, self.OnListBox)
			self.Bind(wx.EVT_LISTBOX_DCLICK, self.OnListBoxDClick)
		sizer = wx.BoxSizer(wx.VERTICAL)
		#sizer.Add(st, 0, wx.ALL, 5)
		sizer.Add(self.lb, 0, wx.ALL, 5)
		#sizer.Add(btn, 0, wx.ALL, 5)
		#sizer.Add(spin, 0, wx.ALL, 5)
		panel.SetSizer(sizer)

		sizer.Fit(panel)
		sizer.Fit(self)
		self.Layout()
		wx.CallAfter(self.Refresh)    
	def OnListBox(self, evt):
		obj = evt.GetEventObject()
		self.log.write("OnListBox: %s\n" % obj)
		self.log.write('Selected: %s\n' % obj.GetString(evt.GetInt()))
		evt.Skip()

	def OnListBoxDClick(self, evt):
		self.Hide()
		self.Destroy()	


	def OnMouseLeftDown(self, evt):
		self.Refresh()
		self.ldPos = evt.GetEventObject().ClientToScreen(evt.GetPosition())
		self.wPos = self.ClientToScreen((0,0))
		self.panel.CaptureMouse()

	def OnMouseMotion(self, evt):
		if evt.Dragging() and evt.LeftIsDown():
			dPos = evt.GetEventObject().ClientToScreen(evt.GetPosition())
			nPos = (self.wPos.x + (dPos.x - self.ldPos.x),
					self.wPos.y + (dPos.y - self.ldPos.y))
			self.Move(nPos)

	def OnMouseLeftUp(self, evt):
		if self.panel.HasCapture():
			self.panel.ReleaseMouse()

	def OnRightUp(self, evt):
		self.Show(False)
		self.Destroy()

########################################################################
class TestPanel(wx.Panel):
	""""""

	#----------------------------------------------------------------------
	def __init__(self, parent):
		"""Constructor"""
		wx.Panel.__init__(self, parent)

		btn = wx.Button(self, label="Open Popup")
		btn.Bind(wx.EVT_BUTTON, self.onShowPopup)


	#----------------------------------------------------------------------
	def onShowPopup(self, event):
		""""""
		win = TestPopup(self.GetTopLevelParent(), wx.SIMPLE_BORDER)

		btn = event.GetEventObject()
		pos = btn.ClientToScreen( (0,0) )
		sz =  btn.GetSize()
		win.Position(pos, (0, sz[1]))

		win.Show(True)
		
class TestPopupWithListbox(wx.PopupWindow):
	def __init__(self, parent, style, log):
		wx.PopupWindow.__init__(self, parent, style)
		self.log = log
		import keyword
		self.lb = wx.ListBox(self, -1, choices = keyword.kwlist)
		#sz = self.lb.GetBestSize()
		self.SetSize((150, 75)) #sz)
		self.lb.SetSize(self.GetClientSize())
		self.lb.SetFocus()
		self.Bind(wx.EVT_LISTBOX, self.OnListBox)
		self.Bind(wx.EVT_LISTBOX_DCLICK, self.OnListBoxDClick)

	def OnListBox(self, evt):
		obj = evt.GetEventObject()
		self.log.write("OnListBox: %s\n" % obj)
		self.log.write('Selected: %s\n' % obj.GetString(evt.GetInt()))
		evt.Skip()

	def OnListBoxDClick(self, evt):
		self.Hide()
		self.Destroy()
		

########################################################################
class TestFrame(wx.Frame):
	""""""

	#----------------------------------------------------------------------
	def __init__(self):
		"""Constructor"""
		wx.Frame.__init__(self, None, title="Test Popup")
		panel = TestPanel(self)
		self.Show()

#----------------------------------------------------------------------
if __name__ == "__main__":
	app = wx.App(False)
	frame = TestFrame()
	app.MainLoop()
