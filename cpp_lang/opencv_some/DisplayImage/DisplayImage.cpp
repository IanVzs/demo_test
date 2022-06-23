//  DisplayImage.cpp

// Display the image

#include <stdio.h>
#include <opencv2/opencv.hpp>

int main(int argc, char** argv )
{

    cv::Mat image;  // variable image of datatype Matrix
    image = cv::imread("../../../opencv_some/flower.png");

    cv::imshow("Display Image", image);
    cv::waitKey(0);
    return 0;
}