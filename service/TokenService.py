

import afs.model.Token


class TokenService():
    
    def __init__(self,config=None):
        pass
    
    
    def getToken(self,username,password,cellname):
        token = Token(username,password,cellname)
        return token