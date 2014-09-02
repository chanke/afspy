
# autogenerated by setup.py
# DO NOT EDIT!
#
import datetime
from afs.orm.DBMapper import safe_mapping, LOGGER
def setup_db_mappings(conf = None) :
    """
    function to setup the objects-database mappings
    """
    from sqlalchemy import Table, Column, Integer, BigInteger, String, \
        MetaData, DateTime, Boolean, TEXT
    from sqlalchemy import ForeignKeyConstraint, ForeignKey, UniqueConstraint

    if conf:
        _cfg = conf
    else:
        _cfg = afs.CONFIG

    LOGGER.debug("Entering setupDbMappers")
    metadata = MetaData()

    #  Servers
    ##################################################
    tbl_hist_fileserver = Table('tbl_hist_fileserver', metadata,
        Column('db_id', Integer, primary_key = True),
        Column('real_db_id', Integer),
        Column('uuid', String(255), index = True),
        Column('servernames_js', TEXT),
        Column('ipaddrs_js', TEXT),
        Column('version', String(32) ),
        Column('build_date', String(32) ),
        Column('db_creation_date', DateTime),
        Column('db_update_date', DateTime),
        )
    # create mapping table
    from afs.model.Historic import historic_FileServer
    safe_mapping(historic_FileServer, tbl_hist_fileserver)

    tbl_hist_extfileservattr = Table('tbl_hist_extfileservattr', metadata,
        Column('db_id', Integer, primary_key = True),
        Column('real_db_id', Integer),
        Column('server_db_id', Integer),
        Column('location', String(32) ),
        Column('owner', String(32) ),
        Column('description', TEXT ),
        Column('db_creation_date', DateTime),
        Column('db_update_date', DateTime),
        )

    # create mapping table
    from afs.model.Historic import historic_ExtFileServAttr
    safe_mapping(historic_ExtFileServAttr, tbl_hist_extfileservattr)

    tbl_hist_dbserver = Table('tbl_hist_dbserver', metadata,
        Column('db_id', Integer, primary_key = True),
        Column('real_db_id', Integer),
        Column('servernames_js', TEXT),
        Column('ipaddr', String(32)),
        Column('afsdb_type', String(32) ),
        Column('local_afsdb_version', String(32) ),
        Column('is_clone', Boolean ),
        Column('version', String(32) ),
        Column('build_date', String(32) ),
        Column('db_creation_date', DateTime),
        Column('db_update_date', DateTime),
        )

    #Mapping Table
    from afs.model.Historic import historic_DBServer
    safe_mapping(historic_DBServer, tbl_hist_dbserver)

    tbl_hist_extdbservattr = Table('tbl_hist_extdbservattr', metadata,
        Column('db_id', Integer, primary_key = True),
        Column('real_db_id', Integer),
        Column('server_db_id', Integer),
        Column('location', String(32) ),
        Column('owner', String(32) ),
        Column('description', TEXT ),
        Column('db_creation_date', DateTime),
        Column('db_update_date', DateTime),
        )

    #Mapping Table
    from afs.model.Historic import historic_ExtDBServAttr
    safe_mapping(historic_ExtDBServAttr, tbl_hist_extdbservattr)

    #
    # BosServer
    #

    tbl_hist_bosserver = Table('tbl_hist_bosserver', metadata,
        Column('db_id', Integer, primary_key = True),
        Column('real_db_id', Integer),
        Column('servernames_js', TEXT),
        Column('ipaddrs_js', TEXT),
        Column('superusers_js', TEXT),
        Column('db_servers_js', TEXT),
        Column('newbinary_restart_time', String(32) ),
        Column('general_restart_time', String(32) ),
        Column('version', String(32) ),
        Column('build_date', String(32) ),
        Column('db_creation_date', DateTime),
        Column('db_update_date', DateTime),
        )

    #Mapping Table
    from afs.model.Historic import historic_BosServer
    safe_mapping(historic_BosServer, tbl_hist_bosserver)


    #
    #  BNodes (Server Processes)
    #

    tbl_hist_bnode = Table('tbl_hist_bnode', metadata,
        Column('db_id', Integer, primary_key = True),
        Column('real_db_id', Integer),
        Column('bos_db_id', Integer),
        Column('bnode_type', String(6)),
        Column('instance_name', String(255)),
        Column('status', String(10)),
        Column('commands_js', TEXT),
        Column('start_date', DateTime),
        Column('start_count', String(255)),
        Column('last_exit_date', DateTime),
        Column('notifier', String(255)),
        Column('error_stop', String(255) ),
        Column('core', String(255)),
        Column('error_exit_date', DateTime ),
        Column('error_exit_due', String(255) ),
        Column('error_exit_signal', String(255) ),
        Column('error_exit_code', String(255) ),
        Column('db_creation_date', DateTime),
        Column('db_update_date', DateTime),
        )

    #Mapping Table
    from afs.model.Historic import historic_BNode
    safe_mapping(historic_BNode, tbl_hist_bnode)

    #  Partition
    ##################################################
    tbl_hist_partition = Table('tbl_hist_partition', metadata,
        Column('db_id', Integer, primary_key = True),
        Column('real_db_id', Integer),
        Column('fileserver_uuid', String(255), index = True),
        Column('name', String(2),index=True),
        Column('size_kb', BigInteger ),
        Column('free_kb', BigInteger ),
        Column('used_kb', BigInteger ),
        Column('db_creation_date', DateTime),
        Column('db_update_date', DateTime),
        )
    #Mapping Table
    from afs.model.Historic import historic_Partition
    safe_mapping(historic_Partition, tbl_hist_partition)

    tbl_hist_extpartattr = Table('tbl_hist_extpartattr', metadata,
        Column('db_id', Integer, primary_key = True),
        Column('real_db_id', Integer),
        Column('fileserver_uuid', String(255), ForeignKey("tbl_hist_partition.fileserver_uuid"),\
            nullable = False),
        Column('name', String(2), ForeignKey("tbl_hist_partition.name"),\
            nullable = False),
        Column('project_ids_js', TEXT),
        Column('allocated', BigInteger ),
        Column('allocated_stale', BigInteger ),
        Column('owner', String(255)),
        Column('unlimited_volumes', Integer ),
        Column('num_vol_rw', Integer, nullable = False, default = 0),
        Column('num_vol_ro', Integer, nullable = False, default = 0),
        Column('num_vol_bk', Integer, nullable = False, default = 0),
        Column('num_vol_offline', Integer, nullable = False, default = 0),
        Column('db_creation_date', DateTime),
        Column('db_update_date', DateTime),
        )

    #Mapping Table
    from afs.model.Historic import historic_ExtPartAttr
    safe_mapping(historic_ExtPartAttr, tbl_hist_extpartattr)

    #  Volume
    ##################################################
    tbl_hist_volume = Table('tbl_hist_volume', metadata,
        Column('db_id', Integer, primary_key = True),
        Column('real_db_id', Integer),
        Column('name', String(255)),
        Column('vid', Integer, index = True ),
        Column('fileserver_uuid', String(255), index = True),
        Column('partition', String(2), index = True),
        Column('servername', String(255)),
        Column('parent_id', Integer ),
        Column('readonly_id', Integer ),
        Column('backup_id', Integer ),
        Column('clone_id', Integer ),
        Column('in_use', String(1)),
        Column('needs_salvage', String(1)),
        Column('destroy_me', String(1)),
        Column('type', String(2)),
        Column('creation_date', DateTime),
        Column('access_date', DateTime),
        Column('backup_date', DateTime),
        Column('copy_date', DateTime),
        Column('flags', Integer ),
        Column('diskused', Integer ),
        Column('maxquota', Integer ),
        Column('minquota', Integer ),
        Column('status', String(2)),
        Column('filecount', Integer ),
        Column('day_use', Integer ),
        Column('week_use', Integer ),
        Column('spare2', Integer ),
        Column('spare3', Integer ),
        Column('db_creation_date', DateTime),
        Column('db_update_date', DateTime),
        )

    #Mapping Table
    from afs.model.Historic import historic_Volume
    safe_mapping(historic_Volume, tbl_hist_volume)

    #  Volume Ext Param
    ##################################################
    tbl_hist_extvolattr = Table('tbl_hist_extvolattr', metadata,
        Column('vid', Integer, primary_key = True),
        Column('real_db_id', Integer),
        Column('num_min_copy', Integer),
        Column('owner', String(255)),
        Column('project_ids_js', TEXT),
        Column('pinned_on_server', Integer),
        Column('db_creation_date', DateTime),
        Column('db_update_date', DateTime),
        ForeignKeyConstraint(['vid'], ['tbl_hist_volume.vid'])
        )
    #Mapping Table
    from afs.model.Historic import historic_ExtVolAttr
    safe_mapping(historic_ExtVolAttr, tbl_hist_extvolattr)


    #  Project Table
    ##################################################
    tbl_hist_project =  Table('tbl_hist_project', metadata,
        Column('db_id', Integer, primary_key = True),
        Column('real_db_id', Integer),
        Column('name', String(255)),
        Column('contact', String(255)),
        Column('owner', String(255)),
        Column('specificity', Integer),
        Column('description', String(1023)),
        Column('rw_locations_js', TEXT),
        Column('ro_locations_js', TEXT),
        Column('rw_serverparts_js', TEXT),
        Column('ro_serverparts_js', TEXT),
        Column('volname_regex_js', TEXT),
        Column('additional_volnames_js', TEXT),
        Column('excluded_volnames_js', TEXT),
        Column('min_size_kb', Integer ),
        Column('max_size_kb', Integer ),
        Column('num_min_ro', Integer),
        Column('db_creation_date', DateTime),
        Column('db_update_date', DateTime),
        )

    #Map Table to object
    from afs.model.Historic import historic_Project
    safe_mapping(historic_Project, tbl_hist_project)

    #  Project Spread
    ##################################################
    tbl_hist_project_spread = Table('tbl_hist_project_spread', metadata,
        Column('db_id', Integer, primary_key = True),
        Column('real_db_id', Integer),
        Column('project_id', Integer),
        Column('fileserver_uuid',  String(255)),
        Column('part', String(2)),
        Column('blocks_fs', BigInteger),
        Column('blocks_osd_on' , BigInteger),
        Column('blocks_osd_off', BigInteger),
        Column('vol_type', String(2)),
        Column('used_kb', BigInteger),
        Column('num_vol', Integer ),
        Column('db_creation_date', DateTime),
        Column('db_update_date', DateTime),
            UniqueConstraint('project_id', 'fileserver_uuid', 'part', 'vol_type',\
            name='uix_1')
        )

    #Map Table to object
    from afs.model.Historic import historic_ProjectSpread
    safe_mapping(historic_ProjectSpread, tbl_hist_project_spread)

    #  Cell Table
    ##################################################
    tbl_hist_cell =  Table('tbl_hist_cell', metadata,
        Column('db_id', Integer, primary_key = True),
        Column('real_db_id', Integer),
        Column('name', String(255), index = True ),
        Column('vldb_sync_site', String(50), nullable = False, default = ""),
        Column('ptdb_sync_site', String(50), nullable = False, default = ""),
        Column('vldb_version', String(20), nullable = False, default = ""),
        Column('ptdb_version', String(20), nullable = False, default = ""),
        Column('vldb_state', String(20), nullable = False, default = ""),
        Column('ptdb_state', String(20), nullable = False, default = ""),
        Column('file_servers_js', TEXT),
        Column('db_servers_js', TEXT),
        Column('projects_js', TEXT),
        Column('size_kb', BigInteger,  nullable = False, default = 0),
        Column('used_kb', BigInteger,  nullable = False, default = 0),
        Column('free_kb', BigInteger,  nullable = False, default = 0),
        Column('allocated_kb', BigInteger, nullable = False, default = 0),
        Column('allocated_stale_kb', BigInteger, nullable = False, default = 0),
        Column('num_vol_rw', Integer, nullable = False, default = 0),
        Column('num_vol_ro', Integer, nullable = False, default = 0),
        Column('num_vol_bk', Integer, nullable = False, default = 0),
        Column('num_vol_offline', Integer, nullable = False, default = 0),
        Column('num_users', Integer, nullable = False, default = 0),
        Column('num_groups', Integer, nullable = False, default = 0),
        Column('db_creation_date', DateTime),
        Column('db_update_date', DateTime, onupdate = datetime.datetime.now)
        )

    #Map Table to object
    from afs.model.Historic import historic_Cell
    safe_mapping(historic_Cell, tbl_hist_cell)

    metadata.create_all(conf.DB_ENGINE)
    try  :
        metadata.create_all(conf.DB_ENGINE)
    except :
        sys.stderr.write("Cannot connect to %s-Database.\n" % _cfg.DB_TYPE)
        if _cfg.DB_TYPE == "mysql":
            sys.stderr.write("Are the MySQL parameters correct and the " +\
            "DB-Server up and running ?\n")
        elif _cfg.DB_TYPE == "sqlite":
            sys.stderr.write("Is the path \"%s\" to the sqlite-DB " + \
            "accessible ?\n" % _cfg.DB_SID)
        sys.exit(1)
    return

# list of all historic tables
historic_tables = ["tbl_hist_fileserver", "tbl_hist_extfileservattr", "tbl_hist_dbserver", "tbl_hist_extdbservattr", "tbl_hist_bosserver", "tbl_hist_bnode", "tbl_hist_partition", "tbl_hist_extpartattr", "tbl_hist_volume", "tbl_hist_extvolattr", "tbl_hist_project", "tbl_hist_project_spread", "tbl_hist_cell", ]
