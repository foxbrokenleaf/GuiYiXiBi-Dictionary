# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.html
from GetContent import SWC

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,480 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        gbSizer1 = wx.GridBagSizer( 0, 0 )
        gbSizer1.SetFlexibleDirection( wx.BOTH )
        gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, u"佐藤", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_textCtrl1.SetMinSize( wx.Size( 360,-1 ) )
        
        gbSizer1.Add( self.m_textCtrl1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_button1 = wx.Button( self, wx.ID_ANY, u"搜索", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1.Add( self.m_button1, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        
        bSizer1.Add( gbSizer1, 1, wx.EXPAND, 5 )
        
        self.m_htmlWin1 = wx.html.HtmlWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.html.HW_SCROLLBAR_AUTO )
        self.m_htmlWin1.SetMinSize( wx.Size( -1,400 ) )
        
        bSizer1.Add( self.m_htmlWin1, 0, wx.ALL|wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.m_button1.Bind( wx.EVT_BUTTON, self.EVENT_CLICKSEARCH )
        self.Bind(wx.EVT_CLOSE,self.CloseWindo)
        self.Bind(wx.EVT_UPDATE_UI,self.ChangeSize)
        
        self.Show()
    def __del__( self ):
        
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def ChangeSize( self ,event ):
        sizeInputBox = wx.Size(self.GetSize()[0]-150,self.m_textCtrl1.GetMinHeight())
        self.m_textCtrl1.SetMinSize(sizeInputBox)
        event.Skip()
    
    def CloseWindo( self,event ):
        self.Destroy()
        
    def EVENT_CLICKSEARCH( self, event ):
        """wbs = SWC()
        wbs.SetSearchObject(self.m_textCtrl1.GetValue())
        wbs.GetData()
        wbs.Paren()
        wbs.SaveLocal()"""
        with open("1.html",'r') as f:
            string = f.read()
            self.m_htmlWin1.SetPage(string)
    
app = wx.App()
frame = MyFrame1(None)
app.MainLoop()