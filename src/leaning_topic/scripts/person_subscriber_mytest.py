#!/usr/bin/env python
# -*- coding: utf-8 -*-

########################################################################
####          Copyright 2020 GuYueHome (www.guyuehome.com).          ###
########################################################################

# 该例程将订阅/person_info话题，自定义消息类型learning_topic::Person

import rospy
from leaning_topic.msg import Person

def personInfoCallback(msg):
    rospy.loginfo("Subcribe Person Info: name:%s  age:%d  sex:%d", 
			 msg.name, msg.age, msg.sex)
    print("h")
    print("he")
    print("hel")
    print("hell")
    print("hello")
    rospy.sleep( 5)
    print("w")
    print("wo")
    print("wor")
    print("worl")
    print("world")
    

def person_subscriber():
	# ROS节点初始化
    rospy.init_node('person_subscriber', anonymous=True)

	# 创建一个Subscriber，订阅名为/person_info的topic，注册回调函数personInfoCallback
    #"<class 'rospy.topics.Subscriber'>"
    timee = 0
    while 1:
        timee+=1
        rospy.sleep(1)
        print("wait ",timee," sec")
        rospy.Subscriber("/person_info", Person, personInfoCallback)
        
	# 循环等待回调函数
    # rospy.spin()

if __name__ == '__main__':
    person_subscriber()
