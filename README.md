For more information, visit http://www.systemical.com/doc/opensource/pysubpub

Overview
========

This package offers a "publish-subscribe" framework.

The framework can be used to implement basic "actors" where each "actor" is contained in a python module.
The function "upub" can be used to queue a message in front instead of the normal tail. 


Features
========

* Extremely lightweight
* Easy to use : 1 decorator 'sub' and 1 function 'pub'
* Simple introspection : use of an 'on_all' @sub function
* No external dependencies   


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
        
    @sub
    def on_all(topic, *p):
        """
        This function will get access to all published messages
        """

        
    pub("topic1", "value1")
    pub("topic2", "value2")
    

The example above would yield:

    "module1/topic1: value1"
    "module2/topic1: value1"
    "module1/topic2: value2"
    
Tests
=====

`nose` can be used to run the package tests.

History
=======

0.2.0 : Added 'on_all' wildcard subscription 
0.1.0 : Initial release