#include <string>
#include <iostream>

#include <opencv2/core/core.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/core/utils/filesystem.hpp>

using namespace cv;
using namespace std;
using namespace cv::utils::fs;

Mat g_srcImage, g_templateImage, g_resultImage;
int g_nMatchMethod;
int g_nMaxTrackbarNum = 5;

void on_matching(int, void*)
{
    	Mat srcImage;
    	g_srcImage.copyTo(srcImage);
    	int resultImage_cols = g_srcImage.cols - g_templateImage.cols + 1;
    	int resultImage_rows = g_srcImage.rows - g_templateImage.rows + 1;
    	g_resultImage.create(resultImage_cols, resultImage_rows, CV_32FC1);

	cout << "g_nMatchMethod: " << g_nMatchMethod << endl;
    	matchTemplate(g_srcImage, g_templateImage, g_resultImage, g_nMatchMethod);
    	double minValue, maxValue;
    	Point minLocation, maxLocation, matchLocation;
    	minMaxLoc(g_resultImage, &minValue, &maxValue, &minLocation, &maxLocation);

    	if (g_nMatchMethod == TM_SQDIFF || g_nMatchMethod == TM_SQDIFF_NORMED)
    	{
    	        matchLocation = minLocation;
    	} else {
    	        matchLocation = maxLocation;
    	}
    	rectangle(
    	        srcImage,
    	        matchLocation,
    	        Point(matchLocation.x + g_templateImage.cols, matchLocation.y + g_templateImage.rows),
    	        Scalar(0, 0, 255),
    	        2,
    	        8,
    	        0
    	);
    	rectangle(
    	    g_resultImage,
    	    matchLocation,
    	    Point(matchLocation.x + g_templateImage.cols, matchLocation.y + g_templateImage.rows),
    	    Scalar(0, 0, 255),
    	    2,
    	    8,
    	    0
    	);
	imshow("source_img", srcImage);
	imshow("effect_img", g_resultImage);
}


int matchOne()
{
	g_srcImage = imread("srcImage.jpeg");
	if (!g_srcImage.data)
	{
		cout << "原始图读取失败" << endl;
		return -1;
	}
	g_templateImage = imread("round.png");
	if (!g_templateImage.data)
	{
		cout << "模版读取失败" << endl;
		return -1;
	}

	imshow("g_srcImage", g_srcImage);
	imshow("g_templateImage", g_templateImage);

	namedWindow("source_img", WINDOW_AUTOSIZE);
	namedWindow("effect_img", WINDOW_AUTOSIZE);
	createTrackbar("func", "source_img", &g_nMatchMethod, g_nMaxTrackbarNum, on_matching);

	on_matching(0, NULL);
	
	waitKey(0);
	return 0;
}

int main()
{
	string path = "temp_imgs";
	if(cv::utils::fs::exists(path))
    	{
        	std::cout << "该文件夹存在---" << path << std::endl;
    	}
	return matchOne();
}
