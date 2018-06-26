#--coding:utf-8--
#把100赋值给cars
cars = 100
#把4.0赋值给space_in_a_car
space_in_a_car = 4.0
#把30赋值给drivers
drivers = 30 
#把90赋值给passengers
passengers = 90
#把cars - drivers 的值赋值给car_not_driver
cars_not_driver = cars - drivers 
#把drivers 的值赋值给cars_driven
cars_driven = drivers
#把car_driven * space_in_a_car的值赋值给carpool_capacity
carpool_capacity = cars_driven * space_in_a_car
#把passengers / cars_driven的赋值给average_passengers_per_car
average_passengers_per_car = passengers / cars_driven

#打印输出内容
print "There are",cars, "cars available."
print "There are only" ,drivers,"drivers available."
print "There will be" , cars_not_driver, "empty cars today."
print "We can transport ",carpool_capacity ,"people today."
print "We have" , passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car"


#expent test 
#运行报错是因为在程序的11行定义的car_not_driver ，而我们在打印中拼写成了car_not_driven,所以报错没有定义

#apace_in_a_car=4.0,如果赋值4,cars_driver * apace_in_a_car 就会是一个整数，赋值4.0,结果是一浮点数
#浮点数：一种对于实数的近似值数值表现法，由一个有效数字（即尾数）加上幂数来表示，通常是乘以某个基数的整数次指数得到

#test4
#= equal       _ underscore

#test6

x = 100
y = 2
j = 50

print x / y / j * y
