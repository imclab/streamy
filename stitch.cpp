#include "opencv2/highgui/highgui.hpp"
#include "opencv2/stitching/stitcher.hpp"
#include <iostream>

using namespace std;
using namespace cv;

bool try_use_gpu = true;
string result_name = "result.jpg";

int main(int argc, char* argv[])
{
    vector<Mat> imgs;
    // add images...
    for (int i=1; i<30; ++i) {
      string c = "frame" + to_string(i) + ".jpeg";
      cout << "filename: " << c << endl;
      imgs.push_back( imread(c));
    }

    Mat pano;
    Stitcher stitcher = Stitcher::createDefault(try_use_gpu);
    stitcher.stitch(imgs, pano);
    imwrite(result_name, pano);
}
