#include <iostream>
#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>

class Histogram1D {

private:
        int histSize[1]; // 直方图中箱子的数量
        float hranges[2]; // 值范围
        const float* ranges[1]; // 值范围的指针
        int channels[1]; // 要检查的通道数量
        static cv::Mat getImageOfHistogram (const cv::Mat &hist, int zoom);
public:
        Histogram1D() {
                // 准备一维直方图的默认参数
                histSize[0] = 256; // 256 个箱子
                hranges[0] = 0.0; // 从 0 开始（含）
                hranges[1] = 256.0; // 到 256（不含）
                ranges[0] = hranges;
                channels[0] = 0; // 先关注通道 0
        }
        cv::Mat getHistogram(const cv::Mat &image);
        cv::Mat getHistogramImage(const cv::Mat &image, int zoom=1);
};


cv::Mat Histogram1D::getHistogram(const cv::Mat &image) {
        cv::Mat hist;
        // 用 calcHist 函数计算一维直方图
        cv::calcHist(&image, 1, // 仅为一幅图像的直方图
            channels, // 使用的通道
            cv::Mat(), // 不使用掩码
            hist, // 作为结果的直方图
            1, // 这是一维的直方图
            histSize, // 箱子数量
            ranges // 像素值的范围
        );
        return hist;
}

// 计算一维直方图，并返回它的图像
cv::Mat Histogram1D::getHistogramImage(const cv::Mat &image, int zoom) {
        // 先计算直方图
        cv::Mat hist= getHistogram(image);
        // 创建图像
        return getImageOfHistogram(hist, zoom);
}

// 创建一个表示直方图的图像（静态方法）
cv::Mat Histogram1D::getImageOfHistogram (const cv::Mat &hist, int zoom) {
        // 取得箱子值的最大值和最小值
        double maxVal = 0;
        double minVal = 0;
        cv::minMaxLoc(hist, &minVal, &maxVal, 0, 0);
        // 取得直方图的大小
        int histSize = hist.rows;
        // 用于显示直方图的方形图像
        cv::Mat histImg(histSize*zoom, histSize*zoom,
                CV_8U, cv::Scalar(255));
        // 设置最高点为 90%（即图像高度）的箱子个数
        int hpt = static_cast<int>(0.9*histSize);
        // 为每个箱子画垂直线
        for (int h = 0; h < histSize; h++) {
                float binVal = hist.at<float>(h);
                if (binVal>0) {
                        int intensity = static_cast<int>(binVal*hpt / maxVal);
                        cv::line(histImg,
                                cv::Point(h*zoom, histSize*zoom),
                                cv::Point(h*zoom, (histSize - intensity)*zoom),
                                cv::Scalar(0), zoom
                        );
                }
        }
        return histImg;
}

int main() {
        cv::Mat image = cv::imread("/home/ian/Pictures/截图/截图 2022-09-08 18-02-29.png", 0);
        Histogram1D h;
        cv::Mat histo = h.getHistogram(image);
        // histo 2D-1(2维单元素)-float
        std::cout << histo << std::endl;
        for (int i = 0; i <256; i++) {
                std::cout << "Value " << i << " = "
                               <<histo.at<float>(i) << std::endl;
        }
        cv::namedWindow("Histogram1");
        cv::imshow("Histogram1", h.getHistogramImage(image, 2));
        cv::waitKey(0);
        cv::imshow("Histogram1img", image);
        cv::waitKey(0);

//        // 二级化
//        cv::Mat thresholded;
//        cv::threshold(image, thresholded, 70,
//                      255, cv::THRESH_BINARY);
//        cv::imshow("thresholded", thresholded);
//        cv::waitKey(0);

        // 均衡化
        cv::equalizeHist(image, image);
        cv::imshow("Histogram2", h.getHistogramImage(image, 2));
        cv::waitKey(0);
        cv::imshow("Histogram2img", image);
        cv::waitKey(0);
}
