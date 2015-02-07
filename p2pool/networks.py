from p2pool.bitcoin import networks
from p2pool.util import math

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

nets = dict(
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
        PERSIST=True,
        WORKER_PORT=1111,
        BOOTSTRAP_ADDRS='stratum.infernopool.com stoyvo.knowsitall.info'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-neos',
        VERSION_CHECK=lambda v: True,
        VERSION_WARNING=lambda v: 'Upgrade neoscoin to >=0.8.5.1!' if v < 80501 else None,
    )
)
for net_name, net in nets.iteritems():
    net.NAME = net_name
