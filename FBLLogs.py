import time
class FBLlogs:
    __stringWhoLogs = ''
    __date = {"YY":'',"MM":'',"DD":'','H':'','M':'','S':''}
    __stringFilePointName = ''
    __stringLogInfo = ''
    __boolShowLogs = False
    
    def __init__(self,WhoLogs ) -> None:
        self.__stringFilePointName = "[{}]".format(WhoLogs) + ' ' + self.GetTime()
        self.__stringWhoLogs = WhoLogs
    
    def GetShowLogsStatus( self ):
        print(self.__boolShowLogs)
    
    def GetWhoLogs( self ):
        print(self.__stringWhoLogs)
    
    def SetShowLogsStatus( self,status ):
        self.__boolShowLogs = status
        
    def Log( self,string ):
        self.__stringLogInfo = string
        self.WriteLogFile()
        
    def GetTime( self ):
        self.__date["YY"] = year = "{:04}".format(time.localtime().tm_year)
        self.__date["MM"] = month = "{:02}".format(time.localtime().tm_mon)
        self.__date["DD"] = day = "{:02}".format(time.localtime().tm_mday)
        self.__date['H'] = hour = "{:02}".format(time.localtime().tm_hour)
        self.__date['M'] = min = "{:02}".format(time.localtime().tm_min)
        self.__date['S'] = sec = "{:02}".format(time.localtime().tm_sec)
        return str(year + month + day + hour + min + sec)
    
    def BuildLog( self ):
        stringCompleteLog = '[{}{}{}{}{}{}]'.format(self.__date["YY"],self.__date["MM"],self.__date["DD"],self.__date['H'],self.__date['M'],self.__date['S']) + self.__stringLogInfo
        if self.__boolShowLogs == True:
            print(stringCompleteLog)
        return stringCompleteLog
    
    def WriteLogFile( self ):
        with open(self.__stringFilePointName,"+a") as f:
            f.writelines(self.BuildLog() + '\n')