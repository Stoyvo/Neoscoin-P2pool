import os
import platform

from twisted.internet import defer

from . import data
from p2pool.util import math, pack, jsonrpc

@defer.inlineCallbacks
def check_genesis_block(bitcoind, genesis_block_hash):
    try:
        yield bitcoind.rpc_getblock(genesis_block_hash)
    except jsonrpc.Error_for_code(-5):
        defer.returnValue(False)
    else:
        defer.returnValue(True)

nets = dict(
       clustercoin=math.Object(
        P2P_PREFIX='bbf9a4a6'.decode('hex'),
        P2P_PORT=9123,
        ADDRESS_VERSION=28,
        RPC_PORT=9234,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'clustercoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 0.1*100000000,
        POW_FUNC=data.hash256,
        BLOCK_PERIOD=60, # s
        SYMBOL='CLSTR',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'clustercoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/clustercoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.clustercoin'), 'clustercoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='',
        ADDRESS_EXPLORER_URL_PREFIX='',
        TX_EXPLORER_URL_PREFIX='',
        SANE_TARGET_RANGE=(2**256//2**32//1000 - 1, 2**256//2**32 - 1),
        DUMB_SCRYPT_DIFF=1,
        DUST_THRESHOLD=0.001e8,
    ),
    payprocoin=math.Object(
        P2P_PREFIX='7070726f'.decode('hex'),
        P2P_PORT=28765,
        ADDRESS_VERSION=56,
        RPC_PORT=28764,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'payprocoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 1000*100000000,
        POW_FUNC=data.hash256,
        BLOCK_PERIOD=300, # s
        SYMBOL='PRO',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'payprocoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/payprocoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.payprocoin'), 'payprocoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='',
        ADDRESS_EXPLORER_URL_PREFIX='',
        TX_EXPLORER_URL_PREFIX='',
        SANE_TARGET_RANGE=(2**256//2**32//1000 - 1, 2**256//2**32 - 1),
        DUMB_SCRYPT_DIFF=1,
        DUST_THRESHOLD=0.03e8,
    ),
        bigbullion=math.Object(
        P2P_PREFIX='f9beb4d9'.decode('hex'),
        P2P_PORT=11055,
        ADDRESS_VERSION=0,
        RPC_PORT=21055,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'bigbullionaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 36*100000000 >> (height + 1)//147000,
        POW_FUNC=data.hash256,
        BLOCK_PERIOD=600, # s
        SYMBOL='BIG',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'BigBullioncoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/BigBullioncoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.bigbullioncoin'), 'coin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://188.226.197.228/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://188.226.197.228/address/',
        TX_EXPLORER_URL_PREFIX='http://188.226.197.228/tx/',
        SANE_TARGET_RANGE=(2**256//2**32//1000 - 1, 2**256//2**32 - 1),
        DUMB_SCRYPT_DIFF=1,
        DUST_THRESHOLD=0.001e8,
    ),
        unattainium=math.Object(
        P2P_PREFIX='f9beb4d9'.decode('hex'),
        P2P_PORT=9777,
        ADDRESS_VERSION=0,
        RPC_PORT=9444,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'unattainiumaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 0.16*100000000,
        POW_FUNC=data.hash256,
        BLOCK_PERIOD=8, # s
        SYMBOL='UNAT',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'unattainium') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/unattainium/') if platform.system() == 'Darwin' else os.path.expanduser('~/.unattainium'), 'unattainium.conf'),
        BLOCK_EXPLORER_URL_PREFIX='',
        ADDRESS_EXPLORER_URL_PREFIX='',
        TX_EXPLORER_URL_PREFIX='',
        SANE_TARGET_RANGE=(2**256//2**32//1000 - 1, 2**256//2**32 - 1),
        DUMB_SCRYPT_DIFF=1,
        DUST_THRESHOLD=0.03e8,
    ),
               neoscoin=math.Object(
        P2P_PREFIX='09080706'.decode('hex'),
        P2P_PORT=15005,
        ADDRESS_VERSION=53,
        RPC_PORT=15004,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'neoscoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 50*100000000  >> (height + 1)//105000,
        POW_FUNC=data.hash256,
        BLOCK_PERIOD=300, # s
        SYMBOL='NEOS',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join("C:/", "Program Files (x86)", "Neos-v2.0.2", "neos-data") if platform.system() == 'Windows' else os.path.expanduser('~/usr/local/neos') if platform.system() == 'Darwin' else os.path.expanduser('~/usr/local/neos'), 'neoscoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://stratum.infernopool.com:8880/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://stratum.infernopool.com:8880/address/',
        TX_EXPLORER_URL_PREFIX='http://stratum.infernopool.com:8880/tx/',
        SANE_TARGET_RANGE=(2**256//2**32//1000 - 1, 2**256//2**32 - 1),
        DUMB_SCRYPT_DIFF=1,
        DUST_THRESHOLD=0.03e8,
    ),
)
for net_name, net in nets.iteritems():
    net.NAME = net_name
