import sys
from kazoo.client import KazooClient, KazooState, KeeperState
import logging
from beat.celery_s import app
from const import ZK_ENSEMBLE 
logging.basicConfig(level=logging.DEBUG)
ROOT_PATH='/schedulers'
my_id=None

def getZK(hosts):
    return KazooClient(ZK_ENSEMBLE, read_only=False)

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

def my_watch_chilren(children):
    logging.info('children: %s' %children)
    if min([int(id) for id in children]) == my_id:
       logging.info('====== ITs MY TERM GOGOGO!!!!!')
       app.start()
    else:
       logging.info('------ NOT MY BUSINESS -------')
def init_root_path(zk):
    print '>>>>',ROOT_PATH, zk.exists(ROOT_PATH)
    if not zk.exists(ROOT_PATH):
       
       zk.create(ROOT_PATH)
def get_my_id(id):
    return int(str(id).split('/')[2])

if __name__ == "__main__":
   print sys.argv
   if len(sys.argv) <= 1:
      logging.error( "please input hosts" )
      exit()
   zk = getZK(sys.argv[1])
   zk.add_listener( my_listener )
#   zk.add_listener( my_rw )
   zk.start()

   init_root_path(zk)


   my_id=get_my_id(zk.create(ROOT_PATH+'/',sequence=True, ephemeral=True))
   zk.ChildrenWatch(ROOT_PATH)(my_watch_chilren)

   logging.info('>>>>> i am :%s' %my_id)
   while True:
       pass
