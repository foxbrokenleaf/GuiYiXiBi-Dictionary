import requests
import bs4
import FBLLogs

class SWC:
    #"https://name-power.net/fn/見崎.html"
    stringUrl = None
    htmlHeader = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    }
    __res = None
    __Logs = None
    
    def __init__(self) -> None:
        self.__Logs = FBLLogs.FBLlogs("SWC")
    
    def Logs( self,string ):
        self.__Logs.Log(string)
    
    def SetSearchObject( self ,string ):
        self.stringUrl = "https://name-power.net/fn/{}}.html".format(string)
        
    def SaveLocal( self ):
        with open("Temp",'w',encoding="utf-8") as f:
            f.write(self.__res.content.decode())
    
    def GetData( self ):
        self.__res = requests.get(url=self.stringUrl,headers=self.htmlHeader)
    
    def GetStatuCode( self ):
        print(self.__res.status_code)
    
    def Paren( self ):
        with open("page.html",'r',encoding="utf-8") as f:
            tempFileContent = f.read()
            soup = bs4.BeautifulSoup(tempFileContent,features="lxml")
            tempFind = soup.find_all('div',class_="entry")
            for temp in tempFind:
                print("".center(100,'-'))
                print(temp)
                print("".center(100,'-'))

a = SWC()
a.Paren()