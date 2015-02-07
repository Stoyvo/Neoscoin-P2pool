from p2pool.bitcoin import networks
from p2pool.util import math

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

nets = dict(
    clustercoin=math.Object(
        PARENT=networks.nets['clustercoin'],
        SHARE_PERIOD=10, # seconds
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=120, # shares
        SPREAD=60, # blocks
        IDENTIFIER='a284bd84f219c53d'.decode('hex'),
        PREFIX='dac528561fd321ec'.decode('hex'),
        P2P_PORT=9111,
        MIN_TARGET=5,
        MAX_TARGET=2**256//2**32 - 1,
        PERSIST=False,
        WORKER_PORT=9222,
        BOOTSTRAP_ADDRS=''.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-CLSTR',
        VERSION_CHECK=lambda v: True,
        VERSION_WARNING=lambda v: 'Upgrade Clustercoin to >=0.8.5!' if v < 80500 else None,
    ),
        payprocoin=math.Object(
        PARENT=networks.nets['payprocoin'],
        SHARE_PERIOD=30, # seconds
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares
        SPREAD=6, # blocks
        IDENTIFIER='231eb1186726ac03'.decode('hex'),
        PREFIX='3d7ad0d83243ccb3'.decode('hex'),
        P2P_PORT=28766,
        MIN_TARGET=5,
        MAX_TARGET=2**256//2**32 - 1,
        PERSIST=False,
        WORKER_PORT=28777,
        BOOTSTRAP_ADDRS=''.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-BTI',
        VERSION_CHECK=lambda v: True,
        VERSION_WARNING=lambda v: 'Upgrade payprocoin to >=0.8.5!' if v < 80500 else None,
    ),
        bigbullion=math.Object(
        PARENT=networks.nets['bigbullion'],
        SHARE_PERIOD=40, # seconds
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=60, # shares
        SPREAD=3, # blocks
        IDENTIFIER='2e653ccbd6bda3e6'.decode('hex'),
        PREFIX='9286761ef873d6c9'.decode('hex'),
        P2P_PORT=9334,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**32 - 1,
        PERSIST=False,
        WORKER_PORT=9444,
        BOOTSTRAP_ADDRS=''.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-BIG',
        VERSION_CHECK=lambda v: 50700 <= v < 60000 or 60010 <= v < 60100 or 60400 <= v,
        VERSION_WARNING=lambda v: 'Upgrade BigBullion to >=0.8.5!' if v < 80500 else None,
    ),
        unattainium=math.Object(
        PARENT=networks.nets['unattainium'],
        SHARE_PERIOD=10, # seconds
        CHAIN_LENGTH=24*60*60//15, # shares
        REAL_CHAIN_LENGTH=24*60*60//15, # shares
        TARGET_LOOKBEHIND=200, # shares
        SPREAD=20, # blocks
        IDENTIFIER='46f1a4d388240563'.decode('hex'),
        PREFIX='575610df0a0493f8'.decode('hex'),
        P2P_PORT=9999,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**32 - 1,
        PERSIST=False,
        WORKER_PORT=9888,
        BOOTSTRAP_ADDRS=''.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-UNAT',
        VERSION_CHECK=lambda v: True,
        VERSION_WARNING=lambda v: 'Upgrade unattainium to >=0.8.5.1!' if v < 80501 else None,
    ),
            neoscoin=math.Object(
        PARENT=networks.nets['neoscoin'],
        SHARE_PERIOD=30, # seconds
        CHAIN_LENGTH=24*60*60//15, # shares
        REAL_CHAIN_LENGTH=24*60*60//15, # shares
        TARGET_LOOKBEHIND=200, # shares
        SPREAD=6, # blocks
        IDENTIFIER='47f1a4d388240564'.decode('hex'),
        PREFIX='13185489E8BED418'.decode('hex'),
        P2P_PORT=3333,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**32 - 1,
        PERSIST=False,
        WORKER_PORT=1111,
        BOOTSTRAP_ADDRS='stratum.infernopool.com stoyvo.knowsitall.info'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-neos',
        VERSION_CHECK=lambda v: True,
        VERSION_WARNING=lambda v: 'Upgrade neoscoin to >=0.8.5.1!' if v < 80501 else None,
    ),
)
for net_name, net in nets.iteritems():
    net.NAME = net_name
