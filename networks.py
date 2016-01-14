    securecoin=math.Object(
        PARENT=networks.nets['securecoin'],
        SHARE_PERIOD=15, # seconds
        NEW_SHARE_PERIOD=15, # seconds
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=50, # shares //with that the pools share diff is adjusting faster, important if huge hashing power comes to the pool
        SPREAD=30, # blocks
        NEW_SPREAD=30, # blocks
        IDENTIFIER='f699135c7a81bc6f'.decode('hex'),
        PREFIX='d399ef181efcd37b'.decode('hex'),
        P2P_PORT=P2P_PORT,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=WORKER_PORT,
        BOOTSTRAP_ADDRS='p2pool.e-pool.net:29968'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool',
        VERSION_CHECK=lambda v: True,
    ),

    securecoin=math.Object(
        P2P_PREFIX='fcb4d9ab'.decode('hex'),
        P2P_PORT=P2P_PORT,
        ADDRESS_VERSION=125,
        RPC_PORT=RPC_PORT,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'securecoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 5*100000000 >> (height + 1)//2100000,
        BLOCKHASH_FUNC=lambda data: pack.IntType(256).unpack(__import__('quark_hash').getPoWHash(data)),
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('quark_hash').getPoWHash(data)),
        BLOCK_PERIOD=30, # s
        SYMBOL='SRC',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'securecoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/securecoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.securecoin'), 'securecoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='https://securechain.info/en/block/',
        ADDRESS_EXPLORER_URL_PREFIX='https://securechain.info/en/address/',
        TX_EXPLORER_URL_PREFIX='https://securechain.info/en/tx/',
        SANE_TARGET_RANGE=(2**256//2**32//1000 - 1, 2**256//2**20 - 1),
        DUMB_SCRYPT_DIFF=1,
        DUST_THRESHOLD=0.001e8,
    ),



