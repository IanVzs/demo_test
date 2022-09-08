set(SCRIPT
#    mat.cpp
    hist.cpp
)
cmake_minimum_required(VERSION 3.14)
project(BASE VERSION 0.1 LANGUAGES CXX)

set(CMAKE_INCLUDE_CURRENT_DIR ON)

set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package( OpenCV REQUIRED )
message(STATUS "OpenCV ${OpenCV_DIR}")
message(STATUS "OpenCV_LIBS ${OpenCV_LIBS}")

add_executable(BASE
    ${SCRIPT}
)

target_link_libraries(BASE
  PRIVATE ${OpenCV_LIBS}
)
