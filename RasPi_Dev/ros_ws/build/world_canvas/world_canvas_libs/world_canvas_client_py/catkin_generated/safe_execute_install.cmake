execute_process(COMMAND "/home/xtark/ros_ws/build/world_canvas/world_canvas_libs/world_canvas_client_py/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/xtark/ros_ws/build/world_canvas/world_canvas_libs/world_canvas_client_py/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
