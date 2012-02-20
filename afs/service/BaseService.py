import afs.util.options
import logging

from afs.util.AfsConfig import AfsConfig
from afs.exceptions.AfsError import AfsError

import afs

class BaseService(object):
    """
    Provides implementation for basic methods for all Service.
    """
    
    def __init__(self,conf=None, DAOList=[], DAOImplementation="childprocs"):
        
        # CONF INIT
        if conf:
            self._CFG = conf
        else:
            self._CFG = afs.defaultConfig
        
        # LOG INIT
        self.Logger=logging.getLogger("afs.%s" % self.__class__.__name__)
        numeric_level = getattr(logging,afs.defaultConfig.LogLevel.upper() , None)
        self.Logger.setLevel(numeric_level)
        self.Logger.debug("initializing %s-Object with conf=%s" % (self.__class__.__name__,conf))
        
        # DB INIT 
        if self._CFG.DB_CACHE :
            import sqlalchemy.orm
            from sqlalchemy import func, or_
            
            self.DbSession = afs.DbSessionFactory()
            self.or_ = or_
        
        # DAO INIT 
        if DAOImplementation == "childprocs" :
            for dao in DAOList :
                if dao == "vl":
                    from afs.dao.VLDbDAO import VLDbDAO
                    self._vlDAO  = VLDbDAO()
                elif dao == "vol" :
                    from afs.dao.VolumeDAO import VolumeDAO 
                    self._volDAO = VolumeDAO()
                elif dao == "bnode" :
                    from afs.dao.BNodeDAO import BNodeDAO
                    self._bnodeDAO = BNodeDAO()
                elif dao == "fs" :
                    from afs.dao.FileServerDAO import FileServerDAO
                    self._fsDAO = FileServerDAO()
                elif dao == "pag" :
                    from afs.dao import PAGDAO
                    self._pagDAO=PAGDAO.PAGDAO()
                elif dao == "krb5" :
                    from afs.dao import krb5DAO
                    self._krb5DAO=krb5DAO.krb5DAO()
                elif dao == "ubik" :
                    from afs.dao import UbikPeerDAO
                    self._ubikDAO=UbikPeerDAO.UbikPeerDAO()
                elif dao == "dns" :
                    from afs.dao import DNSconfDAO
                    self._dnsDAO=DNSconfDAO.DNSconfDAO()
                else :
                    raise AfsError("internal Error. invalid DAO '%s' requested" % dao)
        else :
            raise AfsError("internal Error. DAO-implementation '%s' not available" % DAOImplementation)
    
    def execQuery(self, query):
        conn = self._CFG.DB_ENGINE.connect()
        res = conn.execute(query)
        conn.close()
        return res
    
    def execOrmQuery(self,orm):
        session = self.DbSession()
        
        res = eval(orm)
            
        session.commit()
        session.close()
        
        return res