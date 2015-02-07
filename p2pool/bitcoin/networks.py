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
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join("C:/", "Program Files (x86)", "Neos-v2.0.2", "neos-data") if platform.system() == 'Windows' else os.path.expanduser('~/.neoscoin') if platform.system() == 'Darwin' else os.path.expanduser('~/.neoscoin'), 'neoscoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://stratum.infernopool.com:8880/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://stratum.infernopool.com:8880/address/',
        TX_EXPLORER_URL_PREFIX='http://stratum.infernopool.com:8880/tx/',
        SANE_TARGET_RANGE=(2**256//2**32//1000 - 1, 2**256//2**32 - 1),
        DUMB_SCRYPT_DIFF=1,
        DUST_THRESHOLD=0.03e8,
    )
)
for net_name, net in nets.iteritems():
    net.NAME = net_name
