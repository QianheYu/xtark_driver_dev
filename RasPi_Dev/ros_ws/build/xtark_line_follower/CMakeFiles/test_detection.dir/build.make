# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.13

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/xtark/ros_ws/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/xtark/ros_ws/build

# Include any dependencies generated for this target.
include xtark_line_follower/CMakeFiles/test_detection.dir/depend.make

# Include the progress variables for this target.
include xtark_line_follower/CMakeFiles/test_detection.dir/progress.make

# Include the compile flags for this target's objects.
include xtark_line_follower/CMakeFiles/test_detection.dir/flags.make

xtark_line_follower/CMakeFiles/test_detection.dir/test/test_detect.cpp.o: xtark_line_follower/CMakeFiles/test_detection.dir/flags.make
xtark_line_follower/CMakeFiles/test_detection.dir/test/test_detect.cpp.o: /home/xtark/ros_ws/src/xtark_line_follower/test/test_detect.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/xtark/ros_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object xtark_line_follower/CMakeFiles/test_detection.dir/test/test_detect.cpp.o"
	cd /home/xtark/ros_ws/build/xtark_line_follower && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/test_detection.dir/test/test_detect.cpp.o -c /home/xtark/ros_ws/src/xtark_line_follower/test/test_detect.cpp

xtark_line_follower/CMakeFiles/test_detection.dir/test/test_detect.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/test_detection.dir/test/test_detect.cpp.i"
	cd /home/xtark/ros_ws/build/xtark_line_follower && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/xtark/ros_ws/src/xtark_line_follower/test/test_detect.cpp > CMakeFiles/test_detection.dir/test/test_detect.cpp.i

xtark_line_follower/CMakeFiles/test_detection.dir/test/test_detect.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/test_detection.dir/test/test_detect.cpp.s"
	cd /home/xtark/ros_ws/build/xtark_line_follower && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/xtark/ros_ws/src/xtark_line_follower/test/test_detect.cpp -o CMakeFiles/test_detection.dir/test/test_detect.cpp.s

xtark_line_follower/CMakeFiles/test_detection.dir/src/linedetect.cpp.o: xtark_line_follower/CMakeFiles/test_detection.dir/flags.make
xtark_line_follower/CMakeFiles/test_detection.dir/src/linedetect.cpp.o: /home/xtark/ros_ws/src/xtark_line_follower/src/linedetect.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/xtark/ros_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object xtark_line_follower/CMakeFiles/test_detection.dir/src/linedetect.cpp.o"
	cd /home/xtark/ros_ws/build/xtark_line_follower && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/test_detection.dir/src/linedetect.cpp.o -c /home/xtark/ros_ws/src/xtark_line_follower/src/linedetect.cpp

xtark_line_follower/CMakeFiles/test_detection.dir/src/linedetect.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/test_detection.dir/src/linedetect.cpp.i"
	cd /home/xtark/ros_ws/build/xtark_line_follower && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/xtark/ros_ws/src/xtark_line_follower/src/linedetect.cpp > CMakeFiles/test_detection.dir/src/linedetect.cpp.i

xtark_line_follower/CMakeFiles/test_detection.dir/src/linedetect.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/test_detection.dir/src/linedetect.cpp.s"
	cd /home/xtark/ros_ws/build/xtark_line_follower && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/xtark/ros_ws/src/xtark_line_follower/src/linedetect.cpp -o CMakeFiles/test_detection.dir/src/linedetect.cpp.s

# Object files for target test_detection
test_detection_OBJECTS = \
"CMakeFiles/test_detection.dir/test/test_detect.cpp.o" \
"CMakeFiles/test_detection.dir/src/linedetect.cpp.o"

# External object files for target test_detection
test_detection_EXTERNAL_OBJECTS =

/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: xtark_line_follower/CMakeFiles/test_detection.dir/test/test_detect.cpp.o
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: xtark_line_follower/CMakeFiles/test_detection.dir/src/linedetect.cpp.o
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: xtark_line_follower/CMakeFiles/test_detection.dir/build.make
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /usr/lib/arm-linux-gnueabihf/libgtest.a
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /opt/ros/kinetic/lib/libcv_bridge.so
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /opt/ros/kinetic/lib/libopencv_core3.so.3.3.1
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /opt/ros/kinetic/lib/libopencv_imgproc3.so.3.3.1
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /opt/ros/kinetic/lib/libopencv_imgcodecs3.so.3.3.1
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /opt/ros/kinetic/lib/libroscpp.so
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /usr/lib/arm-linux-gnueabihf/libpthread.so
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /usr/lib/arm-linux-gnueabihf/libboost_filesystem.so
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /usr/lib/arm-linux-gnueabihf/libboost_signals.so
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /opt/ros/kinetic/lib/librosconsole.so
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /opt/ros/kinetic/lib/librosconsole_log4cxx.so
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /opt/ros/kinetic/lib/librosconsole_backend_interface.so
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /usr/lib/arm-linux-gnueabihf/liblog4cxx.so
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /usr/lib/arm-linux-gnueabihf/libboost_regex.so
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /opt/ros/kinetic/lib/libxmlrpcpp.so
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /opt/ros/kinetic/lib/libroscpp_serialization.so
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /opt/ros/kinetic/lib/librostime.so
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /opt/ros/kinetic/lib/libcpp_common.so
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /usr/lib/arm-linux-gnueabihf/libboost_system.so
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /usr/lib/arm-linux-gnueabihf/libboost_thread.so
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /usr/lib/arm-linux-gnueabihf/libboost_chrono.so
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /usr/lib/arm-linux-gnueabihf/libboost_date_time.so
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /usr/lib/arm-linux-gnueabihf/libboost_atomic.so
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /usr/lib/arm-linux-gnueabihf/libconsole_bridge.so.0.4
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /opt/ros/kinetic/lib/libopencv_stitching3.so.3.3.1
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /opt/ros/kinetic/lib/libopencv_superres3.so.3.3.1
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /opt/ros/kinetic/lib/libopencv_videostab3.so.3.3.1
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /opt/ros/kinetic/lib/libopencv_aruco3.so.3.3.1
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /opt/ros/kinetic/lib/libopencv_bgsegm3.so.3.3.1
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /opt/ros/kinetic/lib/libopencv_bioinspired3.so.3.3.1
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /opt/ros/kinetic/lib/libopencv_ccalib3.so.3.3.1
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /opt/ros/kinetic/lib/libopencv_cvv3.so.3.3.1
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /opt/ros/kinetic/lib/libopencv_dpm3.so.3.3.1
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /opt/ros/kinetic/lib/libopencv_face3.so.3.3.1
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /opt/ros/kinetic/lib/libopencv_fuzzy3.so.3.3.1
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /opt/ros/kinetic/lib/libopencv_hdf3.so.3.3.1
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /opt/ros/kinetic/lib/libopencv_img_hash3.so.3.3.1
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /opt/ros/kinetic/lib/libopencv_line_descriptor3.so.3.3.1
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /opt/ros/kinetic/lib/libopencv_optflow3.so.3.3.1
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /opt/ros/kinetic/lib/libopencv_reg3.so.3.3.1
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /opt/ros/kinetic/lib/libopencv_rgbd3.so.3.3.1
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /opt/ros/kinetic/lib/libopencv_saliency3.so.3.3.1
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /opt/ros/kinetic/lib/libopencv_stereo3.so.3.3.1
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /opt/ros/kinetic/lib/libopencv_structured_light3.so.3.3.1
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /opt/ros/kinetic/lib/libopencv_surface_matching3.so.3.3.1
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /opt/ros/kinetic/lib/libopencv_tracking3.so.3.3.1
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /opt/ros/kinetic/lib/libopencv_xfeatures2d3.so.3.3.1
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /opt/ros/kinetic/lib/libopencv_ximgproc3.so.3.3.1
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /opt/ros/kinetic/lib/libopencv_xobjdetect3.so.3.3.1
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /opt/ros/kinetic/lib/libopencv_xphoto3.so.3.3.1
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /opt/ros/kinetic/lib/libopencv_shape3.so.3.3.1
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /opt/ros/kinetic/lib/libopencv_photo3.so.3.3.1
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /opt/ros/kinetic/lib/libopencv_datasets3.so.3.3.1
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /opt/ros/kinetic/lib/libopencv_plot3.so.3.3.1
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /opt/ros/kinetic/lib/libopencv_text3.so.3.3.1
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /opt/ros/kinetic/lib/libopencv_dnn3.so.3.3.1
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /opt/ros/kinetic/lib/libopencv_ml3.so.3.3.1
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /opt/ros/kinetic/lib/libopencv_video3.so.3.3.1
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /opt/ros/kinetic/lib/libopencv_calib3d3.so.3.3.1
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /opt/ros/kinetic/lib/libopencv_features2d3.so.3.3.1
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /opt/ros/kinetic/lib/libopencv_highgui3.so.3.3.1
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /opt/ros/kinetic/lib/libopencv_videoio3.so.3.3.1
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /opt/ros/kinetic/lib/libopencv_viz3.so.3.3.1
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /opt/ros/kinetic/lib/libopencv_phase_unwrapping3.so.3.3.1
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /opt/ros/kinetic/lib/libopencv_flann3.so.3.3.1
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /opt/ros/kinetic/lib/libopencv_imgcodecs3.so.3.3.1
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /opt/ros/kinetic/lib/libopencv_objdetect3.so.3.3.1
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /opt/ros/kinetic/lib/libopencv_imgproc3.so.3.3.1
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: /opt/ros/kinetic/lib/libopencv_core3.so.3.3.1
/home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection: xtark_line_follower/CMakeFiles/test_detection.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/xtark/ros_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable /home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection"
	cd /home/xtark/ros_ws/build/xtark_line_follower && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/test_detection.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
xtark_line_follower/CMakeFiles/test_detection.dir/build: /home/xtark/ros_ws/devel/lib/xtark_line_follower/test_detection

.PHONY : xtark_line_follower/CMakeFiles/test_detection.dir/build

xtark_line_follower/CMakeFiles/test_detection.dir/clean:
	cd /home/xtark/ros_ws/build/xtark_line_follower && $(CMAKE_COMMAND) -P CMakeFiles/test_detection.dir/cmake_clean.cmake
.PHONY : xtark_line_follower/CMakeFiles/test_detection.dir/clean

xtark_line_follower/CMakeFiles/test_detection.dir/depend:
	cd /home/xtark/ros_ws/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/xtark/ros_ws/src /home/xtark/ros_ws/src/xtark_line_follower /home/xtark/ros_ws/build /home/xtark/ros_ws/build/xtark_line_follower /home/xtark/ros_ws/build/xtark_line_follower/CMakeFiles/test_detection.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : xtark_line_follower/CMakeFiles/test_detection.dir/depend

