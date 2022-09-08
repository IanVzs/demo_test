#include <random>
#include <iostream>
#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>

cv::Mat createFunction() {
        // create image
        cv::Mat img(500, 500, CV_8U, 50);
        cv::putText(img, "gray_from_function",
                    cv::Point(10, 100),
                    cv::FONT_HERSHEY_SIMPLEX,
                    1,
                    255);
        return img;
}

void show(cv::Mat & img, cv::String name) {
        cv::imshow(name, img);
        cv::waitKey(0);
}

void salt_img(cv::Mat img, int n) {
        // 给图像加入椒盐噪声
        std::default_random_engine generator;
        std::uniform_int_distribution<int>randomRow(0, img.rows - 1);
        std::uniform_int_distribution<int>randomCol(0, img.cols - 1);

        int i, j;
        for (int k=0; k<n; k++) {
                j = randomCol(generator);
                i = randomRow(generator);
                if (img.type() == CV_8UC1) {
                        img.at<uchar>(i, j) = 255;
                } else if (img.type() == CV_8UC3) {
                        img.at<cv::Vec3b>(i, j) = cv::Vec3b(255, 255, 255);
                }
        }
}
int main() {
        // 240 rows * 320 cols
        cv::Mat image1(240, 320, CV_8U, 100);
        show(image1, "image1");

        // reload
        image1.create(200, 200, CV_8U);
        image1 = 200;
        show(image1, "iamge1");

        // red img
        // bgr
        cv::Mat image2(240, 320, CV_8UC3, cv::Scalar(0, 0, 255));
        cv::Mat image2_cp = image2;
        // or image2 = cv::Scalar(0, 0, 255);
        show(image2, "image2");

        // from function
        cv::Mat gray_img = createFunction();
        image1 = image2;
        // 这一步image2获得了新生，但它的追随者继续负重前行
        cv::flip(gray_img, image2, 1);
        show(gray_img, "gray_img");
        show(image2, "image2");
        cv::putText(image1, "image1",
                    cv::Point(10, 150),
                    cv::FONT_HERSHEY_SIMPLEX,
                    1,
                    255);
        show(image2_cp, "image2_cp");
        show(image1, "image1");
        salt_img(image1, 1000);
        // 提取roi的方法，可以直接赋值也可以搞个变量，共享数据可以直接作用到原图
        image1(cv::Range(image1.rows-50, image1.rows),
               cv::Range(image1.cols-50, image1.cols)) = 0;
        show(image1, "image1_salt");
}
