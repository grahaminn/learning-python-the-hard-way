class Parent(object):

    def override(self):
        print "Parent override()"

    def implicit(self):
        print "PARENT implicit()"

    def altered(self):
        print "PARENT altered()"


class Child(Parent):

    def override(self):
        print "CHILD override()"
 
    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()


class Other(object):
    
    def override(self):
        print "OTHER override()"

    def implicit(self):
        print "OTHER implicit()"
    
    def altered(self):
        print "OTHER altered()"


class Fortytwo(object):
    # Let's make it right from the beginning      
    def __init__(self, other):
        self.other = other
    
    def implicit(self):
        self.other.implicit()

    def override(self):
        print "42 override()"

    def altered(self):
        print "42, BEFORE OTHER altered()"
        self.other.altered()
        print "42, AFTER OTHER altered()"

other = Other()
fortytwo = Fortytwo(other)

fortytwo.implicit()
fortytwo.override()
fortytwo.altered()
    
    
