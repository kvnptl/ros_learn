#!/usr/bin/env python3

import rospy

from my_module.sample_api import say_hello_to_python_developer

if __name__ == '__main__':
    rospy.init_node('main_program')
    say_hello_to_python_developer('Kevin')