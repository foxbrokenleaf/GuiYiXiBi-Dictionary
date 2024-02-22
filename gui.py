# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

from FBLLogs import FBLlogs

###########################################################################
## Class frameMainFrame
###########################################################################

class frameMainFrame ( wx.Frame ):
    
    __Logs = None
    
    def __init__( self, parent ):
        self.__Logs = FBLlogs("GUI")
        
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"日本姓氏語源辞典", pos = wx.DefaultPosition, size = wx.Size( 529,397 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        Right = wx.BoxSizer( wx.VERTICAL )
        
        gbSizer3 = wx.GridBagSizer( 0, 0 )
        gbSizer3.SetFlexibleDirection( wx.BOTH )
        gbSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.inputboxSerachBox = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 410,-1 ), 0 )
        gbSizer3.Add( self.inputboxSerachBox, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.buttonSerachButton = wx.Button( self, wx.ID_ANY, u"搜索", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer3.Add( self.buttonSerachButton, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        
        Right.Add( gbSizer3, 1, wx.EXPAND, 5 )
        
        self.statictextOutput_1 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.Size( -1,100 ), 0 )
        self.statictextOutput_1.Wrap( -1 )
        self.statictextOutput_1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        
        Right.Add( self.statictextOutput_1, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.statictextOutput_2 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.Size( -1,100 ), 0 )
        self.statictextOutput_2.Wrap( -1 )
        self.statictextOutput_2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        
        Right.Add( self.statictextOutput_2, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.statictextOutput_3 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.Size( -1,100 ), 0 )
        self.statictextOutput_3.Wrap( -1 )
        self.statictextOutput_3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        
        Right.Add( self.statictextOutput_3, 0, wx.ALL|wx.EXPAND, 5 )
        
        
        self.SetSizer( Right )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.buttonSerachButton.Bind( wx.EVT_BUTTON, self.EVENT_CLICKSERACH )
        self.Bind(wx.EVT_CLOSE,self.ReleaseFrame)
    
    def __del__( self ):
        pass
    
    def Logs( self,string ):
        self.__Logs.Log(string)
    
    def ReleaseFrame( self,event ):
        pass
    
    # Virtual event handlers, overide them in your derived class
    def EVENT_CLICKSERACH( self, event ):
        event.Skip()
    
app = wx.App()
myframe = frameMainFrame(None)
app.MainLoop()