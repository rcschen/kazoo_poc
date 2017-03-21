import sys
from kazoo.client import KazooClient
import logging
logging.basicConfig(level=logging.DEBUG)

def getZK(hosts):
    return KazooClient(hosts)


if __name__ == "__main__":
   print sys.argv
   if len(sys.argv) <= 1:
      logging.error( "please input hosts" )
      exit()
   zk = getZK(sys.argv[1])
   zk.start()
   while True:
     pass
