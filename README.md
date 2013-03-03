For more information, visit http://www.systemical.com/doc/opensource/pysubpub



Small Example
=============

    from subpub import sub, pub
    
    @sub
    def on_topic1(param1):
        print "topic1: ", param1
        
    pub("topic", "value1")




History
=======

0.1.0: Initial release