# 
# autogenerated by setup.py
# DO NOT EDIT!
#
from datetime import datetime
from afs.model.BaseModel import BaseModel
from afs.magix import *


#
# ExtDBServAttr
#

class historic_ExtDBServAttr(BaseModel):
    """
    Model object of extra Attributes to a server.
    IN DB_CACHE, this is stored in an own table
    """

    ## id of server in DB Table tbl_dbserver
    server_db_id = None
    ## physical Location of the server (string)
    location = ""
    ## Owner of the server (string)
    owner = ""
    ## custom description about HW etc.
    description = ""

    ## pointer to current table entry
    real_db_id = -1

    def __init__(self):
        """
        initialize an empty object
        """
        BaseModel.__init__(self)

#
# ExtFileServAttr
#

class historic_ExtFileServAttr(BaseModel):
    """
    Model object of extra Attributes of a fileserver.
    IN DB_CACHE, this is stored in an own table
    """
    ## id of server in DB Table tbl_servers
    server_db_id = None
    ## physical Location of the server (string)
    location = ""
    ## Owner of the server (string)
    owner = ""
    ## custom description about HW etc.
    description = ""

    ## pointer to current table entry
    real_db_id = -1

    def __init__(self):
        """
        initialize an empty object
        """
        BaseModel.__init__(self)

#
# ExtVolAttr
#

class historic_ExtVolAttr(BaseModel):
    """
    Model object of extra Attributes to a volume.
    IN DB_CACHE, this is stored in an own table
    """

    ## ID of Volume, foreign key to volume-table
    ## SHOULD point to RWID
    vid = -1
    ## number of RO required for this volume, overrrides project
    num_min_copy = -1
    ## Owner of the volume (string)
    owner = ""
    ## json-encodedlist of projectIDs this Volume belongs to
    project_ids_js = '[]'
    project_ids = []
    ## if volume should stay on the present server.
    pinned_on_server = 0

    ## pointer to current table entry
    real_db_id = -1

    def __init__(self):
        """
        initialize an empty object
        """
        BaseModel.__init__(self)

#
# BosServer
#

class historic_BosServer(BaseModel):
    """
    Model object of a bosserver running on a host
    """

    ## list of DNS-hostnames
    servernames = None
    servernames_js = ""
    ## list of ipaddrs
    ipaddrs = None
    ipaddrs_js = ""
    ## list of superusers
    superusers = None
    superusers_js = ""
    ## list of cell hosts (dbservers)
    db_servers = None
    db_servers_js = ""
    ## rxdebug version string and builddate
    version = ""
    build_date = ""
    ## Date of general restart Time
    general_restart_time = ""
    ## Date of newbinary restart Time
    newbinary_restart_time = ""
    ## list of attributes not to put into the DB
    ## these contain (lists of) independent objects
    ## or convenience attributes
    ## bnodes: list of BNode objects
    ## servername short for servernames[0]
    unmapped_attributes_list = ['bnodes', 'servernames']

    ## pointer to current table entry
    real_db_id = -1

    def __init__(self):
        """
        initialize an empty object.
        """
        BaseModel.__init__(self)

#
# PTDB
#

class historic_PTDB(BaseModel) :
    """
    Model for Protection Database.
    This defines a logical view on the DB.
    The single copies of it are defined in the
    DBServer model.
    """

    ## list of servers providing this DB
    dbservers_ipaddrs__js = "[]"
    dbservers_ipaddrs = []
    ## syncsite, master-server
    sync_server_ipaddrs = ""
    ## FIXME: add more attributes like e.g. num_groups
    ## DB-version
    ptdb_version = -1

    ## pointer to current table entry
    real_db_id = -1

    def __init__(self):
        """
        Initializes empty model object
        """
        BaseModel.__init__(self)

#
# ExtPartAttr
#

class historic_ExtPartAttr(BaseModel):
    """
    model object of extra attributes for a partition.
    IN DB_CACHE, this is stored in an own table
    """

    ##  (fileserver_uuid,name) is foreign key to partition-table
    name = ""
    fileserver_uuid = ""
    ## Owner of the Partition (string)
    owner = ""
    ## json-encoded dict { "projectID" : "numVolumes" }
    ## showing ProjectIDs having numVolumes  volumes on that partition
    project_ids_js = '{}'
    project_ids = {}
    ## allocated (by quota) size in Kbytes
    allocated = -1
    ## stale_allocated, same as allocated,
    ## but for volumes which had not been accessed in $StaleTime days
    allocated_stale = -1
    ## number of volumes with unlimited quota
    unlimited_volumes = -1
    ## Total number of volumes
    num_vol_rw = -1
    num_vol_ro = -1
    num_vol_bk = -1
    num_vol_offline = -1

    ## pointer to current table entry
    real_db_id = -1

    def __init__(self) :
        """
        initialize an empty object
        """
        BaseModel.__init__(self)

#
# CacheManager
#

class historic_CacheManager(object) :
    """
    empty Model for a CacheManager
    """
    ## pointer to current table entry
    real_db_id = -1

    def __init__(self):
        """
        Initializes empty shell
        """
        
        ## Cellname
        self.ws_cell = ""
        ## Aliases
        self.cell_aliases={}

#
# Partition
#

class historic_Partition(BaseModel):
    """
    Model object of the live-data of a partition
    """

    ## UUID of fileserver
    fileserver_uuid = ""
    ## canonicalized partition name e.g "ad" for "/vicepad"
    name = ""
    ## free size in Kbytes
    free_kb = -1
    ## total size in Kbytes
    size_kb = -1
    ## used size in Kbytes
    used_kb = -1
    ## list of attributes not to put into the DB
    unmapped_attributes_list = [ "ExtAttr" ]

    ## pointer to current table entry
    real_db_id = -1

    def __init__(self):
        """
        initialize an empty object
        """
        BaseModel.__init__(self)

#
# Volume
#

class historic_Volume(BaseModel) :
    """
    Provides information about AFS-Volumes 
    """

    ## name of the volume in the VLDB
    name = ''
    ## numerical ID of the volume, can be RW, RO or BK
    vid = -1
    ## ServerUUID where this volume is stored
    fileserver_uuid = ""
    ## Partitionname, where this volume is stored.
    partition = ""
    ## hostname, not to be used for queries
    servername = ""
    ## numerical ID of RW Volume
    parent_id = 0
    ## numerical ID of RO Volume
    readonly_id = 0
    ## numerical ID of Backup Volume
    backup_id = 0
    clone_id  = 0
    in_use = ""
    needs_salvage = ""
    destroy_me = ""
    type = ""
    creation_date = datetime.fromtimestamp(0)
    access_date = datetime.fromtimestamp(0)
    backup_date = datetime.fromtimestamp(0)
    copy_date = datetime.fromtimestamp(0)
    flags = 0
    diskused = -1
    maxquota = -1
    minquota = -1
    status = VolStatus.OK
    filecount = 0
    day_use  = 0
    week_use = 0
    spare2  = 0
    spare3  = 0
    ## list of attributes not to put into the DB
    unmapped_attributes_list =  ['ExtAttr']

    ## pointer to current table entry
    real_db_id = -1

    def __init__(self) :
        """
        initializes to an empty Volume
        """
        BaseModel.__init__(self)

#
# Project
#

class historic_Project(BaseModel):
    """
    Model object of  a Project :
    A project is a group of Volumes defined by the Volume names
    and size.
    A project then defines other attributes such as  (geographical) location,
    contact person, owner(organisation), on which server partition-pairs
    the volumes should reside.
    """

    ## name
    name = ""
    ## list of regexes, json encoded
    volname_regex_js = "[]"
    volname_regex = []
    ## list of additional Volumenames, json encoded
    additional_volnames_js = "[]"
    additional_volnames = []
    ## list of excluded Volumenames , json encoded
    excluded_volnames_js = "[]"
    excluded_volnames = []
    ## minimum Size for a Volume
    min_size_kb = -1
    ## maximum Size for a volume
    max_size_kb = -1
    ## specificity can be used for project hierachies
    specificity = 0
    ## contact
    contact = ""
    ## owner
    owner = ""
    ## list of locationIDs for RW-Volumes, json encoded
    rw_locations_js = "[]"
    rw_locations = []
    ## list of locationIDs for RO-Volumes, json encoded
    ro_locations_js = "[]"
    ro_locations = []
    ## list of "server-uuid,partition" pairs for RW-Volumes, json encoded
    rw_serverparts_js = "[]"
    rw_serverparts = []
    ## list of "server-uuid,partition" pairs for RO-Volumes, json encoded
    ro_serverparts_js = ""
    ro_serverparts = []
    ## free form description
    description = ""
    ## minimum number of RO-replicas
    num_min_ro = 1

    ## pointer to current table entry
    real_db_id = -1

    def __init__(self) :
        """
        initialize an empty object
        """
        BaseModel.__init__(self)

#
# BNode
#

class historic_BNode(BaseModel):
    """
    Model object of a bosserver child process (bnode)
    """

    ## DB-ID of owning bosserver
    bos_db_id = -1
    instance_name = ""
    bnode_type = ""
    # FIXME : what to do with procs of type cron ?
    ## list of commands run for this bnode
    commands = ''
    commands_js = ''
    status = ''
    start_date = datetime.fromtimestamp(0)
    start_count = ''
    last_exit_date = datetime.fromtimestamp(0)
    notifier = ''
    error_stop  = ''
    core = ''
    error_exit_date = datetime.fromtimestamp(0)
    error_exit_due = ''
    error_exit_signal = ''
    error_exit_code = ''

    ## pointer to current table entry
    real_db_id = -1

    def __init__(self, instance_name = "N/A", bnode_type = "N/A", bos_db_id = -1):
        """
        initialize an empty object
        """
        BaseModel.__init__(self)
        ## DB-ID of owning bosserver
        bos_db_id = bos_db_id
        instance_name = instance_name
        bnode_type = bnode_type
    

#
# DBServer
#

class historic_DBServer(BaseModel):
    """
    Model object of a database-server
    """

    ## for db index
    db_id = None
    ## list of DNS-hostnames
    servernames = None
    servernames_js = ""
    ## list of ipaddrs
    ipaddr = ""
    ## Flag if it is a clone or real db-server
    is_clone = True
    ## type of db : vldb or ptdb
    afsdb_type = ""
    ## local version of the DB
    local_afsdb_version = ""
    ## rxdebug version string 
    version = ""
    build_date = ""
    ## list of attributes not to put into the DB
    unmapped_attributes_list= ['BNode', 'ExtServAttr' ]

    ## pointer to current table entry
    real_db_id = -1

    def __init__(self):
        """
        initialize an empty object.
        """
        BaseModel.__init__(self)

#
# FileServer
#

class historic_FileServer(BaseModel):
    """
    Model object of a fileserver 
    initialize an empty object.
    Partitions are not in the same Table in DB_CACHE as
    Server, so the attribute 'partitions' will be inserted by the FsService
    """

    ## AFS Server UUID
    uuid = ""
    ## list of DNS-hostnames
    servernames_js = '[]'
    servernames = []
    ## list of ipaddrs
    ipaddrs_js = '[]'
    ipaddrs = []
    ## rxdebug version string 
    version = ""
    ## build-date of binary according to rxdebug
    build_date = ""
    ## list of attributes not to put into the DB
    unmapped_attributes_list = [ 'parts', 'ExtServAttr' ]

    ## pointer to current table entry
    real_db_id = -1

    def __init__(self):
        """
        base initialiser   
        """
        BaseModel.__init__(self)
        return

#
# Cell
#

class historic_Cell(BaseModel) :
    """
    empty Model for a Cell
    """
        
    ## Database definitions
    ## Cellname
    name = ""
    ## VLDb-Version
    vldb_version = -1
    ## VLDb-syncsite, hostname
    vldb_sync_site = ""
    ## VLDB-State (aka "Recovery state")
    vldb_state = ""
    ## PTDB-Version
    ptdb_version = -1
    ## PTDB-syncsite, hostname
    ptdb_sync_site = ""
    ## PTDB-State (aka "Recovery state")
    ptdb_state = ""
    ## Number of users in PTDB
    num_users = -1
    ## Number of groups in PTDB
    num_groups = -1
    ## Total number of volumes
    num_vol_rw = -1
    num_vol_ro = -1
    num_vol_bk = -1
    num_vol_offline = -1
    ## List of DBServers (hostnames only)
    db_servers = []
    db_servers_js = ""
    ## List of FileServers (hostnames only)
    file_servers = []
    file_servers_js = ""
    ## List of Projects (names only)
    projects = []
    projects_js = ""
    ## Total Size, etc
    size_kb = -1
    used_kb = -1
    free_kb = -1
    allocated_kb = -1
    allocated_stale_kb = -1

    ## pointer to current table entry
    real_db_id = -1

    def __init__(self):
        """
        Initializes empty shell
        """
        BaseModel.__init__(self)

#
# ProjectSpread
#

class historic_ProjectSpread(BaseModel):
    """
    Model object of the spread of a project :
    This is a helper table to show how many volumes of what size
    are stored on different server partition of a single project
    """

    ## DB ID of Project 
    project_id = -1
    ## UUID of FSServer
    fileserver_uuid = -1
    ## partition
    part = ""
    ## type of volumes
    vol_type = ""
    ## number of volumes of that type
    num_vol = -1
    ## total used kilobytes 
    used_kb = -1
    ## osd - cruft
    blocks_fs = -1
    blocks_osd_on = -1
    blocks_osd_off = -1

    ## pointer to current table entry
    real_db_id = -1

    def __init__(self):
        """
        initialize an empty object
        """
        BaseModel.__init__(self)

#
# VLDB
#

class historic_VLDB(BaseModel) :
    """
    empty model for volume Location Database.
    This defines a logical view on the DB.
    The single copies of it are defined in the
    DBServer model.
    """

    ## list of servers providing this DB
    dbservers_ipaddrs_js = "[]"
    dbservers_ipaddrs = []
    ## syncsite, master-server
    sync_server_ipaddrs = ""
    ## FIXME: add more attributes like registered fileservers etc.
    ## DB-version
    vldb_version = -1

    ## pointer to current table entry
    real_db_id = -1

    def __init__(self):
        """
        Initializes empty shell
        """
        BaseModel.__init__(self)
