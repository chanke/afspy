import sys
from afs.exceptions.ORMError import ORMError
import afs
import logging,datetime

logger=logging.getLogger("afs.DB_CACHE")

def createDbEngine(conf=None):
    """
    using conf, setup the core DB-engine
    and return it.
    The returned engine must be incorporated in the 
    used AfsConfig object
    """
    from sqlalchemy import create_engine
    if conf:
        _CFG = conf
    else:
        _CFG = afs.defaultConfig

    # Option definition
    ###########################################
    driver = ""
    
    # Connection
    ###########################################
    engine = 0
    if conf.DB_TYPE == "mysql":
        driver = 'mysql://%s:%s@%s:%s/%s' % (conf.DB_USER,  conf.DB_PASSWD,conf.DB_HOST, conf.DB_PORT, conf.DB_SID)
        logger.debug("creating engine with driver :'%s'" % driver)
        try: 
            engine = create_engine(driver,pool_size=20, max_overflow=30, pool_recycle=3600, echo=False)         
        except :
            raise ORMError("Cannot create DB Engine for type mysql using driver %s" % driver )
    elif _CFG.DB_TYPE == "sqlite":    
        driver = 'sqlite:///'+_CFG.DB_SID
        logger.debug("creating engine with driver :'%s'" % driver)
        try:
            engine = create_engine(driver, echo=False)
        except :
            raise ORMError("Cannot create DB Engine for type sqlite using driver %s " % driver )
    return engine

def safeMapping( ModelClass, TableDef):
    from afs.model.BaseModel import BaseModel
    from sqlalchemy.orm import mapper
    
    ModelObj=ModelClass()
    ModelAttributes=dir(ModelObj)
    BaseModelAttributes=dir(BaseModel())
    m=mapper(ModelClass, TableDef)
    mappedColumns=m.columns.keys()
    
    for k in ModelAttributes :
        # ignore private sqlalchemy methods
        if k[0] == "_" : continue
        # a python-only attribute to define which other attributes should not put into the DB
        if k == "ignAttrList" : continue
        # ignore stuff defined in BaseModel (includes all general private methods of an obj.)
        if k in BaseModelAttributes : continue
        if not k in mappedColumns :
          if "%s_js" % k in mappedColumns : continue # ignore fields which are json encoded in DB
          raise ORMError("Mapping of model Object '%s' not correct. Attribute '%s' not mapped." % (ModelObj.__class__.__name__,k) )
    
    for c in mappedColumns :
        if not c in ModelAttributes :
            raise ORMError("Mapping of model Object '%s' not correct. Mapped attribute '%s' not in Objectmodel." % (ModelObj.__class__.__name__, c))
    
def setupDbMappers(conf=None):
    from sqlalchemy     import Table, Column, Integer, BigInteger, String, MetaData, DateTime, Boolean, TEXT, Float
    from sqlalchemy     import  ForeignKeyConstraint,ForeignKey
    
    if conf:
        _CFG = conf
    else:
        _CFG = afs.defaultConfig
   
    logger.debug("Entering setupDbMappers")
    metadata = MetaData()
   
    # Scheduler
    ##################################################
    
    #  Servers
    ##################################################
    tbl_fileserver = Table('tbl_fileserver', metadata,
          Column('id'           , Integer, primary_key=True),
          Column('uuid'         , String(255), index=True),
          Column('servernames_js', TEXT),
          Column('ipaddrs_js'    , TEXT),
          Column('version'      , String(32) ),
          Column('builddate'      , String(32) ),
          Column('cdate'        , DateTime),
          Column('udate'        , DateTime),
          )
    #Mapping Table
    from afs.model.FileServer import FileServer
    safeMapping(FileServer,tbl_fileserver)

    tbl_extfileservattr = Table('tbl_extfileservattr', metadata,
          Column('id'           , Integer, primary_key=True),
          Column('server_id'    , Integer),
          Column('location'      , String(32) ),
          Column('owner'      , String(32) ),
          Column('description'  , TEXT ),
          Column('cdate'        , DateTime),
          Column('udate'        , DateTime),
          )

    #Mapping Table
    from afs.model.ExtendedFileServerAttributes import ExtFileServAttr
    safeMapping(ExtFileServAttr,tbl_extfileservattr)

    tbl_dbserver = Table('tbl_dbserver', metadata,
          Column('id'           , Integer, primary_key=True),
          Column('servernames_js', TEXT),
          Column('ipaddr'    , String(32)),
          Column('type'      , String(32) ),
          Column('localDBVersion'      , String(32) ),
          Column('isClone'      , Boolean ),
          Column('version'      , String(32) ),
          Column('builddate'      , String(32) ),
          Column('cdate'        , DateTime),
          Column('udate'        , DateTime),
          )

    #Mapping Table         
    from afs.model.DBServer import DBServer
    safeMapping(DBServer,tbl_dbserver)

    tbl_extdbservattr = Table('tbl_extdbservattr', metadata,
          Column('id'           , Integer, primary_key=True),
          Column('server_id'    , Integer),
          Column('location'      , String(32) ),
          Column('owner'      , String(32) ),
          Column('description'  , TEXT ),
          Column('cdate'        , DateTime),
          Column('udate'        , DateTime),
          )

    #Mapping Table
    from afs.model.ExtendedDBServerAttributes import ExtDBServAttr
    safeMapping(ExtDBServAttr,tbl_extdbservattr)

    tbl_bosserver = Table('tbl_bosserver', metadata,
          Column('id'           , Integer, primary_key=True),
          Column('servernames_js', TEXT),
          Column('ipaddrs_js'    , TEXT),
          Column('binaryRestartTime'      , String(32) ),
          Column('generalRestartTime'       , String(32) ),
          Column('version'      , String(32) ),
          Column('builddate'      , String(32) ),
          Column('cdate'        , DateTime),
          Column('udate'        , DateTime),
          )
        
    #Mapping Table
    from afs.model.BosServer import BosServer
    safeMapping(BosServer,tbl_bosserver)
 
      
    #  Partition
    ##################################################
    tbl_partition = Table('tbl_partition', metadata,
          Column('id'           , Integer, primary_key=True),
          Column('serv_uuid'         , String(255), index=True),
          Column('name'         , String(2),index=True),
          Column('size'         , BigInteger ),
          Column('free'         , BigInteger ),
          Column('used'         , BigInteger ),
          Column('cdate'        , DateTime),
          Column('udate'        , DateTime),
          ) 
    #Mapping Table
    from afs.model.Partition import Partition
    safeMapping(Partition,tbl_partition)

    tbl_extpartattr = Table('tbl_extpartattr', metadata,
          Column('id'           , Integer, primary_key=True),
          Column('serv_uuid',     String(255),ForeignKey("tbl_partition.serv_uuid"),nullable=False), 
          Column('name'         , String(2),ForeignKey("tbl_partition.name"), nullable=False),
          Column('projectIDs_js'      , TEXT),
          Column('allocated'    , BigInteger ),
          Column('allocated_stale', BigInteger ),
          Column('owner'        , String(255)),
          Column('unLimitedVolumes' , Integer ),
          Column('numRW'         ,Integer,  nullable=False, default=0),
          Column('numRO'         ,Integer,  nullable=False, default=0),
          Column('numBK'         ,Integer,  nullable=False, default=0),
          Column('numOffline'         ,Integer,  nullable=False, default=0),
          Column('cdate'        , DateTime),
          Column('udate'        , DateTime),
         )

    #Mapping Table
    from afs.model.ExtendedPartitionAttributes import ExtPartAttr
    safeMapping(ExtPartAttr,tbl_extpartattr)
  
    #  BOS
    ##################################################
    tbl_bos = Table('tbl_bos', metadata,
          Column('id'           , Integer, primary_key=True),
          Column('servername'         , String(255)),
          Column('generalRestartTime' , DateTime),
          Column('binaryRestartTime'  , DateTime),
          Column('cdate'        , DateTime),
          Column('udate'        , DateTime),
          ) 
    #Mapping Table
    from afs.model.Bos import Bos
    safeMapping(Bos,tbl_bos)
  
    #  BNodes (Server Processes)
    ##################################################
    tbl_bnode = Table('tbl_bnode', metadata,
          Column('id'           , Integer, primary_key=True),
          Column('bos_id'       , Integer),
          Column('BNodeType'         , String(2)),
          Column('status'       , String(2)),
          Column('Commands'    , String(255)),
          Column('startdate'    , String(255)),
          Column('startcount'   , String(255)),
          Column('exitdate'     , String(255)),
          Column('notifier'     , String(255)),
          Column('state'        , String(255)),
          Column('errorstop'    , String(255) ),
          Column('core'         , String(255)),
          Column('errorexitdate', String(255) ),
          Column('errorexitdue' , String(255) ),
          Column('errorexitsignal' , String(255) ),
          Column('errorexitcode' , String(255) ),
          Column('cdate'        , DateTime),
          Column('udate'        , DateTime),
          ) 
    #Mapping Table
    from afs.model.BNode import BNode
    safeMapping(BNode,tbl_bnode) 

    #  Volume
    ##################################################
    tbl_volume = Table('tbl_volume', metadata,
          Column('id'           , Integer, primary_key=True),
          Column('name'         , String(255)),
          Column('vid'          , Integer,     index=True ),
          Column('serv_uuid'    , String(255), index=True),
          Column('part'         , String(2),   index=True),
          Column('servername'   , String(255 )), 
          Column('parentID'     , Integer ),
          Column('backupID'     , Integer ),
          Column('cloneID'      , Integer ),
          Column('inUse'        , String(1)),
          Column('needsSalvaged', String(1)),
          Column('destroyMe'    , String(1)),
          Column('type'         , String(2)),
          Column('creationDate' , DateTime),
          Column('accessDate'   , DateTime),
          Column('updateDate'   , DateTime),
          Column('backupDate'   , DateTime),
          Column('copyDate'     , DateTime),
          Column('flags'        , Integer ),
          Column('diskused'     , Integer ),
          Column('maxquota'     , Integer ),
          Column('minquota'     , Integer ),
          Column('status'       , String(2)),
          Column('filecount'    , Integer ),
          Column('dayUse'       , Integer ),
          Column('weekUse'      , Integer ),
          Column('spare2'       , Integer ),
          Column('spare3'       , Integer ),
          Column('cdate'        , DateTime),
          Column('udate'        , DateTime),
          )
             
    #Mapping Table
    from afs.model.Volume import Volume
    safeMapping(Volume,tbl_volume)
    
    #  Volume Ext Param
    ##################################################
    tbl_extvolattr= Table('tbl_extvolattr', metadata,
          Column('vid', Integer, primary_key=True ), 
          Column('mincopy'      , Integer),
          Column('owner'        , String(255)),
          Column('projectIDs_js'      , TEXT),
          Column('pinnedOnServer'       , Integer),
          Column('cdate'        , DateTime),
          Column('udate'        , DateTime),
          ForeignKeyConstraint(['vid'], ['tbl_volume.vid'])
          ) 
    #Mapping Table
    from afs.model.ExtendedVolumeAttributes import ExtVolAttr
    safeMapping(ExtVolAttr,tbl_extvolattr)
  
 
    #  Project Table
    ##################################################
    tbl_project =  Table('tbl_project',metadata,
          Column('id'           , Integer, primary_key=True),
          Column('name'        , String(255)),
          Column('contact'        , String(255)),
          Column('owner'        , String(255)),
          Column('NestingLevel'        , Integer),
          Column('description'      , String(1023)),
          Column('rw_locations_js',  TEXT), 
          Column('ro_locations_js',  TEXT), 
          Column('rw_serverparts_js',  TEXT), 
          Column('ro_serverparts_js',  TEXT), 
          Column('volnameRegEx_js',  TEXT),
          Column('additionalVolnames_js',  TEXT), 
          Column('excludedVolnames_js',  TEXT), 
          Column('minSize_kB'         , Integer ), 
          Column('maxSize_kB'         , Integer ), 
          Column('minnum_ro'      , Integer),
          Column('cdate'        , DateTime),
          Column('udate'        , DateTime),
          )

    #Map Table to object
    from afs.model.Project import Project
    safeMapping(Project,tbl_project)

    #  Cell Table
    ##################################################
    tbl_cell =  Table('tbl_cell',metadata,
        Column('id'           , Integer, primary_key=True),
        Column('Name'        , String(255), index=True ),
        Column('VLDBSyncSite'        , String(50), nullable=False, default=""),
        Column('PTDBSyncSite'        , String(50), nullable=False, default=""),
        Column('VLDBVersion'        , String(20), nullable=False, default=""),
        Column('PTDBVersion'        , String(20), nullable=False, default=""),
        Column('VLDBState'        , String(20), nullable=False, default=""),
        Column('PTDBState'        , String(20), nullable=False, default=""),
        Column('FileServers_js'         , TEXT),
        Column('DBServers_js'         , TEXT),
        Column('Projects_js'         , TEXT),
        Column('size'     , BigInteger,  nullable=False, default=0),
        Column('used'     , BigInteger,  nullable=False, default=0),
        Column('free'     , BigInteger,  nullable=False, default=0),
        Column('allocated'     , BigInteger,  nullable=False, default=0),
        Column('allocated_stale'     , BigInteger,  nullable=False, default=0),
        Column('numRW'         ,Integer,  nullable=False, default=0),
        Column('numRO'         ,Integer,  nullable=False, default=0),
        Column('numBK'         ,Integer,  nullable=False, default=0),
        Column('numOffline'         ,Integer,  nullable=False, default=0),
        Column('numUsers'         ,Integer,  nullable=False, default=0),
        Column('numGroups'         ,Integer,  nullable=False, default=0),
        Column('cdate'        , DateTime),
        Column('udate', DateTime, onupdate=datetime.datetime.now)
        )
        
    #Map Table to object
    from afs.model.Cell import Cell
    safeMapping(Cell,tbl_cell)

    # Cell OSD
    ##################################################
    tbl_cell_osd =  Table('tbl_cell_osd',metadata,
        Column('id'           , Integer, primary_key=True),
        Column('Name'        , String(255), index=True ),
        Column('OSDDBSyncSite'        , String(50)),
        Column('OSDDBVersion'        , String(20)),
        Column('RXOSDServers_js'         , TEXT),
        Column('StorageUsage_js'         , TEXT),
        Column('numRW'         ,Integer),
        Column('numRO'         ,Integer),
        Column('numBK'         ,Integer),
        Column('numRW_OSD'         ,Integer),
        Column('numRO_OSD'         ,Integer),
        Column('numBK_OSD'         ,Integer),
        Column('size'     , BigInteger),
        Column('allocated'     , BigInteger),
        Column('allocated_stale'     , BigInteger),
        Column('size_OSD'     , BigInteger),
        Column('allocated_OSD'     , BigInteger),
        Column('allocated_stale_OSD'     , BigInteger),
        Column('blocks_fs'     , BigInteger),
        Column('blocks_osd_on' , BigInteger),
        Column('blocks_osd_off', BigInteger),
        Column('cdate'        , DateTime),
        Column('udate'        , DateTime),
        )
        
    #Map Table to object
    from afs.model.Cell_OSD import Cell_OSD
    safeMapping(Cell_OSD,tbl_cell_osd)

    #  Volume OSD Param
    ##################################################
    tbl_extvolattr_osd= Table('tbl_extvolattr_osd', metadata,
          Column('vid'          , Integer, primary_key=True),
          Column('filequota'    , Integer),
          Column('files_fs'    , Integer),
          Column('files_osd'    , Integer),
          Column('blocks_fs'     , BigInteger),
          Column('blocks_osd_on' , BigInteger),
          Column('blocks_osd_off', BigInteger),
          Column('osdPolicy'    , Integer),
          Column('cdate'        , DateTime),
          Column('udate'        , DateTime),
          ForeignKeyConstraint(['vid'], ['tbl_volume.vid'])
          )   
    #Mapping Table
    from afs.model.ExtendedVolumeAttributes_OSD import ExtVolAttr_OSD
    safeMapping(ExtVolAttr_OSD,tbl_extvolattr_osd) 

    metadata.create_all(conf.DB_ENGINE) 
    try  :
        metadata.create_all(conf.DB_ENGINE) 
    except :
        sys.stderr.write("Cannot connect to %s-Database.\n" % _CFG.DB_TYPE)
        if _CFG.DB_TYPE == "mysql":
            sys.stderr.write("Are the MySQL parameters correct and the DB-Server up and running ?\n")
        elif _CFG.DB_TYPE == "sqlite":
            sys.stderr.write("Is the path \"%s\" to the sqlite-DB accessible ?\n" % _CFG.DB_SID)
        sys.exit(1)
    return
    
