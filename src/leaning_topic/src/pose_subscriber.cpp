/*
该例子将订阅turtle1/pose话题，消息类型turtlesim::Pose
*/

#include <ros/ros.h>
#include "turtlesim/Pose.h"

//接收到订阅的消息后，会进入信息回调函数  msg是长指针  回调函数不会被打断，如果回调函数整体过长，收到消息又很频繁，那么有些消息就会丢失，所以回调函数尽量执行时间短
void poseCallback(const turtlesim::Pose::ConstPtr& msg) 
{
	//将接受到的消息打印出来
	ROS_INFO("Turtle pose: x:%0.6f, y:%0.6f", msg->x, msg->y);
}


int main(int argc,char **argv)
{
	//初始化ros节点
	ros::init(argc,argv,"pose_subscriber");
	
	//创建句柄
	ros::NodeHandle n;

	//创建订阅者  订阅名为/turtle1/Pose的topic，注册回调函数poseCallback subscriber也有个缓冲区，可以放10个消息
	ros::Subscriber pose_sub = n.subscribe("/turtle1/pose",10,poseCallback);	

	//循环等待回调函数
	ros::spin();

	return 0;
}
