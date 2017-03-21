#!/usr/bin/python
import logging
from time import sleep
from kazoo.client import KazooClient, ChildrenWatch

# print log to console
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

zk = KazooClient('127.0.0.1:2181')
zk.start()

@zk.ChildrenWatch('/zookeeper')
def children_callback(children):
    print '****' , children

children = zk.get_children('/zookeeper', children_callback)

zk.create('/zookeeper/',sequence=True, ephemeral=True)
#zk.delete('/zookeeper/goodboy')

while True: 
   #children = zk.get_children('/zookeeper', children_callback)

   sleep(1)
