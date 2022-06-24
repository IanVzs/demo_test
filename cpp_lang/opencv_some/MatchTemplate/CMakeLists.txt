#set (CMAKE_CXX_STANDARD 20)
# 以上得放在首行, 否则无效
cmake_minimum_required(VERSION 2.8)
project( MatchTemplateCpp )
find_package( OpenCV REQUIRED )
include_directories( ${OpenCV_INCLUDE_DIRS} )
add_executable( MatchTemplate.out MatchTemplate.cpp )
target_link_libraries( MatchTemplate.out ${OpenCV_LIBS} )
