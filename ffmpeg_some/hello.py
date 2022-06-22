"""
第三方库 功能简朴 6k
pip install ffmpeg-python
早已停更(2019), 文档有误
"""
from ffmpeg.stream import Stream

def main(path):
    stream = Stream()
    stream.input(path)
    info = stream.video_info()
    print(info)

if __name__ == "__main__":
    import os
    home = os.environ.get("HOME")

    path = os.path.join(home, "Desktop", "ScreenRecording.mov")
    main(path)