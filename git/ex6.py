#--coding:utf-8--
#%d处取的值是%10中的10
x = "There are %d types of people." %10
#赋值
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary , do_not)
#打印变量
print x 
print y 
#打印字符串
print "I said:%r"  %x
print "I said:'%s'" % y 
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious 
#拼接字符串
w = "This is the left side of ...."
e = "a string with a right side."
print w + e 
