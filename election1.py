#!/usr/bin/python
import logging
from time import sleep
from kazoo.client import KazooClient

# print log to console
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

zk = KazooClient('127.0.0.1:2181')
zk.start()

def children_callback(children):
    print '****' , children
def get_children():
    print '>>>>>>>>'
    #zk.get_children('/electionpath', children_callback)

election = zk.Election("/electionpath", "my-identifierGGG")
while True: 
   election.run(get_children)
   sleep(1)
