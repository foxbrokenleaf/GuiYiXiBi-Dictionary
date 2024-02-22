import requests
class GetWebPage:
    
    url = ''
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}
    content = ''
    logs = None
    
    def __init__(self) -> None:
        pass
    
    def SetUrl( self,url ):
        self.url = url
        
    def GetWeb( self ):
        res = requests.get(self.url,self.headers)
        print(res.status_code)
        return res
        
    def SaveFile( self ):
        res = self.GetWeb()
        with open("WebPage.html",'wb') as f:
            for temp in res.iter_content(chunk_size=1024):
                f.write(temp)