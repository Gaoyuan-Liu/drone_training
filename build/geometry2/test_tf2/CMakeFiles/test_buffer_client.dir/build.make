# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.10

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
CMAKE_SOURCE_DIR = /home/liu/drone_training/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/liu/drone_training/build

# Include any dependencies generated for this target.
include geometry2/test_tf2/CMakeFiles/test_buffer_client.dir/depend.make

# Include the progress variables for this target.
include geometry2/test_tf2/CMakeFiles/test_buffer_client.dir/progress.make

# Include the compile flags for this target's objects.
include geometry2/test_tf2/CMakeFiles/test_buffer_client.dir/flags.make

geometry2/test_tf2/CMakeFiles/test_buffer_client.dir/test/test_buffer_client.cpp.o: geometry2/test_tf2/CMakeFiles/test_buffer_client.dir/flags.make
geometry2/test_tf2/CMakeFiles/test_buffer_client.dir/test/test_buffer_client.cpp.o: /home/liu/drone_training/src/geometry2/test_tf2/test/test_buffer_client.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/liu/drone_training/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object geometry2/test_tf2/CMakeFiles/test_buffer_client.dir/test/test_buffer_client.cpp.o"
	cd /home/liu/drone_training/build/geometry2/test_tf2 && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/test_buffer_client.dir/test/test_buffer_client.cpp.o -c /home/liu/drone_training/src/geometry2/test_tf2/test/test_buffer_client.cpp

geometry2/test_tf2/CMakeFiles/test_buffer_client.dir/test/test_buffer_client.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/test_buffer_client.dir/test/test_buffer_client.cpp.i"
	cd /home/liu/drone_training/build/geometry2/test_tf2 && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/liu/drone_training/src/geometry2/test_tf2/test/test_buffer_client.cpp > CMakeFiles/test_buffer_client.dir/test/test_buffer_client.cpp.i

geometry2/test_tf2/CMakeFiles/test_buffer_client.dir/test/test_buffer_client.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/test_buffer_client.dir/test/test_buffer_client.cpp.s"
	cd /home/liu/drone_training/build/geometry2/test_tf2 && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/liu/drone_training/src/geometry2/test_tf2/test/test_buffer_client.cpp -o CMakeFiles/test_buffer_client.dir/test/test_buffer_client.cpp.s

geometry2/test_tf2/CMakeFiles/test_buffer_client.dir/test/test_buffer_client.cpp.o.requires:

.PHONY : geometry2/test_tf2/CMakeFiles/test_buffer_client.dir/test/test_buffer_client.cpp.o.requires

geometry2/test_tf2/CMakeFiles/test_buffer_client.dir/test/test_buffer_client.cpp.o.provides: geometry2/test_tf2/CMakeFiles/test_buffer_client.dir/test/test_buffer_client.cpp.o.requires
	$(MAKE) -f geometry2/test_tf2/CMakeFiles/test_buffer_client.dir/build.make geometry2/test_tf2/CMakeFiles/test_buffer_client.dir/test/test_buffer_client.cpp.o.provides.build
.PHONY : geometry2/test_tf2/CMakeFiles/test_buffer_client.dir/test/test_buffer_client.cpp.o.provides

geometry2/test_tf2/CMakeFiles/test_buffer_client.dir/test/test_buffer_client.cpp.o.provides.build: geometry2/test_tf2/CMakeFiles/test_buffer_client.dir/test/test_buffer_client.cpp.o


# Object files for target test_buffer_client
test_buffer_client_OBJECTS = \
"CMakeFiles/test_buffer_client.dir/test/test_buffer_client.cpp.o"

# External object files for target test_buffer_client
test_buffer_client_EXTERNAL_OBJECTS =

/home/liu/drone_training/devel/lib/test_tf2/test_buffer_client: geometry2/test_tf2/CMakeFiles/test_buffer_client.dir/test/test_buffer_client.cpp.o
/home/liu/drone_training/devel/lib/test_tf2/test_buffer_client: geometry2/test_tf2/CMakeFiles/test_buffer_client.dir/build.make
/home/liu/drone_training/devel/lib/test_tf2/test_buffer_client: /usr/lib/x86_64-linux-gnu/libboost_thread.so
/home/liu/drone_training/devel/lib/test_tf2/test_buffer_client: /usr/lib/x86_64-linux-gnu/libboost_chrono.so
/home/liu/drone_training/devel/lib/test_tf2/test_buffer_client: /usr/lib/x86_64-linux-gnu/libboost_system.so
/home/liu/drone_training/devel/lib/test_tf2/test_buffer_client: /usr/lib/x86_64-linux-gnu/libboost_date_time.so
/home/liu/drone_training/devel/lib/test_tf2/test_buffer_client: /usr/lib/x86_64-linux-gnu/libboost_atomic.so
/home/liu/drone_training/devel/lib/test_tf2/test_buffer_client: /usr/lib/x86_64-linux-gnu/libpthread.so
/home/liu/drone_training/devel/lib/test_tf2/test_buffer_client: /opt/ros/melodic/lib/libtf.so
/home/liu/drone_training/devel/lib/test_tf2/test_buffer_client: /opt/ros/melodic/lib/liborocos-kdl.so
/home/liu/drone_training/devel/lib/test_tf2/test_buffer_client: /home/liu/drone_training/devel/lib/libtf2_ros.so
/home/liu/drone_training/devel/lib/test_tf2/test_buffer_client: /opt/ros/melodic/lib/libactionlib.so
/home/liu/drone_training/devel/lib/test_tf2/test_buffer_client: /opt/ros/melodic/lib/libmessage_filters.so
/home/liu/drone_training/devel/lib/test_tf2/test_buffer_client: /opt/ros/melodic/lib/libroscpp.so
/home/liu/drone_training/devel/lib/test_tf2/test_buffer_client: /usr/lib/x86_64-linux-gnu/libboost_filesystem.so
/home/liu/drone_training/devel/lib/test_tf2/test_buffer_client: /opt/ros/melodic/lib/librosconsole.so
/home/liu/drone_training/devel/lib/test_tf2/test_buffer_client: /opt/ros/melodic/lib/librosconsole_log4cxx.so
/home/liu/drone_training/devel/lib/test_tf2/test_buffer_client: /opt/ros/melodic/lib/librosconsole_backend_interface.so
/home/liu/drone_training/devel/lib/test_tf2/test_buffer_client: /usr/lib/x86_64-linux-gnu/liblog4cxx.so
/home/liu/drone_training/devel/lib/test_tf2/test_buffer_client: /usr/lib/x86_64-linux-gnu/libboost_regex.so
/home/liu/drone_training/devel/lib/test_tf2/test_buffer_client: /opt/ros/melodic/lib/libxmlrpcpp.so
/home/liu/drone_training/devel/lib/test_tf2/test_buffer_client: /home/liu/drone_training/devel/lib/libtf2.so
/home/liu/drone_training/devel/lib/test_tf2/test_buffer_client: /opt/ros/melodic/lib/liborocos-kdl.so.1.4.0
/home/liu/drone_training/devel/lib/test_tf2/test_buffer_client: /opt/ros/melodic/lib/libroscpp_serialization.so
/home/liu/drone_training/devel/lib/test_tf2/test_buffer_client: /opt/ros/melodic/lib/librostime.so
/home/liu/drone_training/devel/lib/test_tf2/test_buffer_client: /opt/ros/melodic/lib/libcpp_common.so
/home/liu/drone_training/devel/lib/test_tf2/test_buffer_client: /usr/lib/x86_64-linux-gnu/libboost_system.so
/home/liu/drone_training/devel/lib/test_tf2/test_buffer_client: /usr/lib/x86_64-linux-gnu/libboost_thread.so
/home/liu/drone_training/devel/lib/test_tf2/test_buffer_client: /usr/lib/x86_64-linux-gnu/libboost_chrono.so
/home/liu/drone_training/devel/lib/test_tf2/test_buffer_client: /usr/lib/x86_64-linux-gnu/libboost_date_time.so
/home/liu/drone_training/devel/lib/test_tf2/test_buffer_client: /usr/lib/x86_64-linux-gnu/libboost_atomic.so
/home/liu/drone_training/devel/lib/test_tf2/test_buffer_client: /usr/lib/x86_64-linux-gnu/libpthread.so
/home/liu/drone_training/devel/lib/test_tf2/test_buffer_client: /usr/lib/x86_64-linux-gnu/libconsole_bridge.so.0.4
/home/liu/drone_training/devel/lib/test_tf2/test_buffer_client: gtest/googlemock/gtest/libgtest.so
/home/liu/drone_training/devel/lib/test_tf2/test_buffer_client: /opt/ros/melodic/lib/liborocos-kdl.so.1.4.0
/home/liu/drone_training/devel/lib/test_tf2/test_buffer_client: /usr/lib/x86_64-linux-gnu/libboost_signals.so
/home/liu/drone_training/devel/lib/test_tf2/test_buffer_client: /usr/lib/x86_64-linux-gnu/libconsole_bridge.so.0.4
/home/liu/drone_training/devel/lib/test_tf2/test_buffer_client: /opt/ros/melodic/lib/libroscpp_serialization.so
/home/liu/drone_training/devel/lib/test_tf2/test_buffer_client: /opt/ros/melodic/lib/librostime.so
/home/liu/drone_training/devel/lib/test_tf2/test_buffer_client: /opt/ros/melodic/lib/libcpp_common.so
/home/liu/drone_training/devel/lib/test_tf2/test_buffer_client: /usr/lib/x86_64-linux-gnu/libboost_system.so
/home/liu/drone_training/devel/lib/test_tf2/test_buffer_client: /usr/lib/x86_64-linux-gnu/libboost_thread.so
/home/liu/drone_training/devel/lib/test_tf2/test_buffer_client: /usr/lib/x86_64-linux-gnu/libboost_chrono.so
/home/liu/drone_training/devel/lib/test_tf2/test_buffer_client: /usr/lib/x86_64-linux-gnu/libboost_date_time.so
/home/liu/drone_training/devel/lib/test_tf2/test_buffer_client: /usr/lib/x86_64-linux-gnu/libboost_atomic.so
/home/liu/drone_training/devel/lib/test_tf2/test_buffer_client: /usr/lib/x86_64-linux-gnu/libpthread.so
/home/liu/drone_training/devel/lib/test_tf2/test_buffer_client: /usr/lib/x86_64-linux-gnu/libconsole_bridge.so.0.4
/home/liu/drone_training/devel/lib/test_tf2/test_buffer_client: geometry2/test_tf2/CMakeFiles/test_buffer_client.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/liu/drone_training/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable /home/liu/drone_training/devel/lib/test_tf2/test_buffer_client"
	cd /home/liu/drone_training/build/geometry2/test_tf2 && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/test_buffer_client.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
geometry2/test_tf2/CMakeFiles/test_buffer_client.dir/build: /home/liu/drone_training/devel/lib/test_tf2/test_buffer_client

.PHONY : geometry2/test_tf2/CMakeFiles/test_buffer_client.dir/build

geometry2/test_tf2/CMakeFiles/test_buffer_client.dir/requires: geometry2/test_tf2/CMakeFiles/test_buffer_client.dir/test/test_buffer_client.cpp.o.requires

.PHONY : geometry2/test_tf2/CMakeFiles/test_buffer_client.dir/requires

geometry2/test_tf2/CMakeFiles/test_buffer_client.dir/clean:
	cd /home/liu/drone_training/build/geometry2/test_tf2 && $(CMAKE_COMMAND) -P CMakeFiles/test_buffer_client.dir/cmake_clean.cmake
.PHONY : geometry2/test_tf2/CMakeFiles/test_buffer_client.dir/clean

geometry2/test_tf2/CMakeFiles/test_buffer_client.dir/depend:
	cd /home/liu/drone_training/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/liu/drone_training/src /home/liu/drone_training/src/geometry2/test_tf2 /home/liu/drone_training/build /home/liu/drone_training/build/geometry2/test_tf2 /home/liu/drone_training/build/geometry2/test_tf2/CMakeFiles/test_buffer_client.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : geometry2/test_tf2/CMakeFiles/test_buffer_client.dir/depend

