For more information, visit http://www.systemical.com/doc/opensource/pysubpub

Overview
========

This package offers a "publish-subscribe" framework.

The framework can be used to implement basic "actors" where each "actor" is contained in a python module.
The function "upub" can be used to queue a message in front instead of the normal tail. 

Small Example
=============

    ## Actor 1 in module1.py
    ##
    from subpub import sub, pub
    
    @sub
    def on_topic1(param1):
        print "module1/topic1: ", param1

    @sub
    def on_topic2(param1):
        print "module1/topic2: ", param1
        

    ## Actor 2 in module2.py
    ##
    from subpub import sub, pub
    
    @sub
    def on_topic1(param1):
        print "module2/topic1: ", param1
        
    pub("topic1", "value1")
    pub("topic2", "value2")
    

The example above would yield:

    "module1/topic1: value1"
    "module2/topic1: value1"
    "module1/topic2: value2"
    

History
=======

0.1.0: Initial release