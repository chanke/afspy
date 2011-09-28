from datetime import datetime
from afs.factory.VolTypeFactory import VolType
from afs.factory.VolStatusFactory import VolStatus 
from afs.model.BaseModel import BaseModel


class Volume(BaseModel) :
    """
    Provides information about AFS-Volumes and methods to change them
    """
    
    def __init__(self) :
        """
        initializes to an empty Volume, if ID=-1 is given.
        To get a volume by Name, ID=0 must be given.
        Optional arg. Server is used when getting a RO-Volume. 
        Otherwise the resulting Object can be on any server
        """
        #afs.rxosd.OSDVolume.__init__(self)
        ##Name of the Volume in the VLDB
        
        self.name     = ''
        ##numerical ID of the Volume
        self.vid      = -1
        ## Servername, where this volume is stored
        self.serv     = ""
        ## Partitionname, where this volume is stored.
        self.part     =""
        self.parentID = 0
        self.backupID = 0
        self.cloneID  = 0
        self.inUse         = ""
        self.needsSalvaged = "N"
        self.destroyMe     = "N"
        self.type          = "RW"
        self.creationDate  = 0 
        self.updateDate    = 0
        self.backupDate    = 0 
        self.copyDate = 0
        self.flags    = 0
        self.diskused = 0
        self.maxquota = 0 
        self.minquota = 0
        self.status = VolStatus.OK
        self.filecount = 0
        self.dayUse  = 0
        self.weekUse = 0
        self.spare2  = 0 
        self.spare3  = 0
        self.cdate   = datetime.now()
        self.udate   = datetime.now()
        self.sync    = 0
        













    def __repr__(self):
        return "<Volume('%s',%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s','%s', '%s', '%s', '%s','%s', '%s', '%s', '%s','%s', '%s', '%s', '%s','%s', '%s')>" % (   self.id, self.name, self.vid, self.serv,  self.part, self.parentID, self.backupID, self.cloneID, self.inUse, self.needsSalvaged, self.destroyMe, self.type,  self.creationDate, self.updateDate, self.backupDate, self.copyDate, self.flags, self.diskused,  self.maxquota,   self.minquota, self.status,  self.filecount, self.dayUse, self.weekUse, self.spare2, self.spare3 ) 

   