// DisplayVideo.cpp


#include <stdio.h>
#include <opencv2/opencv.hpp>

int readMp4()
{
    cv::Mat frame;  // variable frame of datatype Matrix
    cv::VideoCapture capture;
    capture.open("/Users/ianvzs/Desktop/audio_tagging_demo.mp4");

    for(;;){
        capture>>frame;
        if(frame.empty())
            break;
        cv::imshow("Window", frame);

        if(cv::waitKey(30)>=0)
                break;
    }
    return 0;
}

int readCapture()
{
    cv::VideoCapture capture(0);
    while(true)
    {
        cv::Mat frame;
        capture >> frame;
        // std::cout << frame << std::endl;
        cv::imshow("视频", frame);
        if(cv::waitKey(30)>=0)
            break;
    }
    return 0;
}

int main(int argc, char** argv )
{
    readMp4();
    return readCapture();
}