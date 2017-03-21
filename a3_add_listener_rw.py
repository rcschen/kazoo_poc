import sys
from kazoo.client import KazooClient, KazooState, KeeperState
import logging
logging.basicConfig(level=logging.DEBUG)

def getZK(hosts):
    return KazooClient(hosts, read_only=True)

def my_listener(state):
    if state == KazooState.LOST:
        logging.error('KazooState.LOST')
        # Register somewhere that the session was lost
    elif state == KazooState.SUSPENDED:
        logging.error('KazooState.SUSPENDED')
        # Handle being disconnected from Zookeeper
    else:
        logging.error('KazooState.connected/reconned: %s' %state)
        # Handle being connected/reconnected to Zookeeper
def my_rw(state):
    if state == KeeperState.CONNECTED_RO:
       logging.info("Read only mode!")
    else:
       logging.info("Read/Write mode!")

if __name__ == "__main__":
   print sys.argv
   if len(sys.argv) <= 1:
      logging.error( "please input hosts" )
      exit()
   zk = getZK(sys.argv[1])
   zk.add_listener( my_listener )
   zk.add_listener( my_rw )
   zk.start()
   while True:
       pass
