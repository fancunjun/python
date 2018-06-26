#--coding:utf-8 --
my_name = 'Zed A. Shaw'
my_age = 35 # not a lie 
my_height = 74 #inches
my_weight = 180 #lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Lte's talk about %s." % my_name
print "He's %d pounds heavy" % my_weight
print "He's %d inches tall." % my_height
print "Actually that's not too heavy"
print "He's got %s eyes and %s hair." % (my_eyes,my_hair)
print "His teeth are usually %s depending on the coffee." %my_teeth

#this line is tricky,try to get it exactly right 
print "If I add %d ,%d,and %d I get %d." %(my_age,my_height,my_weight,my_age + my_height + my_weight)

print 'this is del "my_" '
name = 'Zed A. Shaw'
age = 35 # not a lie 
height = 74 #inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Lte's talk about %s." % name
print "He's %d pounds heavy" % weight
print "He's %d inches tall." % height
print "Actually that's not too heavy"
print "He's got %s eyes and %s hair." % (eyes,hair)
print "His teeth are usually %s depending on the coffee." % teeth

#this line is tricky,try to get it exactly right 
print "If I add %d ,%d,and %d I get %d." %(age,height,weight,age + height + weight)

# inches change cm and lbs change kilogram

mid  = 2.5
mid1 = 0.45
inches  = 2
lbs = 3

cm = inches * mid
kilogram = lbs * mid1
print kilogram
print cm



