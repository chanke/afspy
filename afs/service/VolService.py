import afs.util.options

from afs.dao.VolumeDAO import VolumeDAO
from afs.dao.FileServerDAO import FileServerDAO
from afs.model.Volume import Volume
from afs.model.AfsConfig import AfsConfig
from afs.model.VolumeError import VolumeError

class VolService (object):
    """
    Provides Service about a Volume management.
    The cellname is set in the methods so that we 
    can use this for more than one cell.
    """
    
    def __init__(self,token,conf=None):
        self._TOKEN  = token
        self._volDAO = VolumeDAO()
        self._srvDAO = FileServerDAO()
        
        # LOAD Configuration from file if exist
        # FIXME Move in decorator
        if conf:
            self._CFG = conf
        else:
            self._CFG = AfsConfig(True)
        
        # DB INIT    
        if self._CFG.DB_CACHE :
            import sqlalchemy.orm
            self.DbSession = sqlalchemy.orm.sessionmaker(bind=self._CFG.DB_ENGINE)

    ###############################################
    # Volume Section
    ###############################################    
    """
    Retrieve Volume Group
    """
    def getVolGroup(self, id,  **kwargs):
        cellname = self._TOKEN._CELL_NAME
        
        if kwargs.get("cellname"):
            cellname = kwargs.get("cellname")

        rc , err, list = self._volDAO.getVolGroup(id, cellname, self._TOKEN );
        if rc != 0:
            raise VolumeError('Not Found:'+ err)
        
        return list 
       
    
        #ALWAYS REAL DATA on single volume    
        vol=self._volDAO.getVolume(id,cellname, self._TOKEN)
        
        #STORE info into  CACHE
        if self._CFG.DB_CACHE:
            import sqlalchemy.orm
            session=self.DbSession()
            # update by simple delete and re-add
            session.query(Volume.vid, Volume.serv, Volume.part).filter(Volume.vid == vol.vid).filter(Volume.serv == vol.serv).filter(Volume.part == vol.part).delete()
            session.add(vol)
            session.commit()
            session.refresh(vol)
            session.close()
            # detach vol-object from the session
            sqlalchemy.orm.session.make_transient(vol)
        return vol
    
    
    """
    Retrieve Volume Information by Name or ID
    """
    def getVolume(self, name, serv, part, **kwargs):
        cellname = self._TOKEN._CELL_NAME
        
        if kwargs.get("cellname"):
            cellname = kwargs.get("cellname")
    
        #ALWAYS REAL DATA on single volume  

        rc, vol_or_err = self._volDAO.getVolume(name, serv, part, cellname, self._TOKEN)
        
        if  rc != 0:
            raise VolumeError('Not Found:'+vol_or_err)
        
        self._setIntoCache(vol_or_err)
       
        return  vol_or_err
    
    """
    Retrieve Volume extended information
    """
    def getVolExtended(self,id):
        pass
    
    
    ################################################
    #  Cache Management 
    ################################################

    def _getFromCache(self,id, serv, part):
        #STORE info into  CACHE
        if not self._CFG.DB_CACHE:
            return 1, None
        session = self.DbSession()
        # Do update
        vol = session.query(Volume).filter(Volume.vid == id).filter(Volume.serv == serv).filter(Volume.part == part).first
        
        session.commit()
        session.close()
        return 0,vol
        
    def _setIntoCache(self,vol):
         #STORE info into  CACHE
        if not self._CFG.DB_CACHE:
            return 1, None
        
        session = self.DbSession()
        session.add(vol)  
        print "add"
        
        session.commit()  
        session.close()
        
        return 0,vol
    
    def _delCache(self,vol):
         #STORE info into  CACHE
        if not self._CFG.DB_CACHE:
            return 1, None
        session = self.DbSession()
        # Do update
        session.delete(vol)
            
        session.commit()
        session.close()
    
    #MERGE ?    
    def _updateCache(self,vol):
         #STORE info into  CACHE
        if not self._CFG.DB_CACHE:
            return 1
        
        session = self.DbSession()
            
        session.commit()
        session.close()
            
    

    
    
    
 
    
