"""
PyAV is a Pythonic binding for FFmpeg. 
较深度PY整合, 1.6K 持续更新ing(2022)

github: https://github.com/PyAV-Org/PyAV
website: https://pyav.org/docs/stable/
cookbook_base: https://pyav.org/docs/stable/cookbook/basics.html

依赖(但是这个库居然没声明,需要自行补全安装...):
    PIL (pip install Pillow)

原生支持格式:
    .mov
    .mp4
"""
import av

def all_frame(path_to_video):
    """提取所有帧"""
    container = av.open(path_to_video)
    for frame in container.decode(video=0):
        # print(frame.index)
        frame.to_image().save('frame-%04d.jpg' % frame.index)
        # if frame.index >= 10:
        #     break

def key_frame(path):
    """提取关键帧(画面场景大幅不同)"""
    with av.open(path) as container:
        stream = container.streams.video[0]
        # Signal that we only want to look at keyframes.     stream = container.streams.video[0]
        stream.codec_context.skip_frame = 'NONKEY'

        for frame in container.decode(stream):
            print(frame)
            # We use `frame.pts` as `frame.index` won't make must sense with the `skip_frame`.         
            frame.to_image().save(
                'night-sky.{:04d}.jpg'.format(frame.pts),
                quality=80,
            )

def composite_video(path):
    """
    合成视频
    """
    import numpy as np

    duration = 4
    fps = 24
    total_frames = duration * fps
    container = av.open(path, mode='w')
    stream = container.add_stream('mpeg4', rate=fps)
    stream.width = 480
    stream.height = 320
    stream.pix_fmt = 'yuv420p'

    for frame_i in range(total_frames):
        img = np.empty((480, 320, 3))
        img[:, :, 0] = 0.5 + 0.5 * np.sin(2 * np.pi * (0 / 3 + frame_i / total_frames))
        img[:, :, 1] = 0.5 + 0.5 * np.sin(2 * np.pi * (1 / 3 + frame_i / total_frames))
        img[:, :, 2] = 0.5 + 0.5 * np.sin(2 * np.pi * (2 / 3 + frame_i / total_frames))

        img = np.round(255 * img).astype(np.uint8)
        img = np.clip(img, 0, 255)

        frame = av.VideoFrame.from_ndarray(img, format='rgb24')
        for packet in stream.encode(frame):
            container.mux(packet)
    """
    1. Flush stream
        for packet in stream.encode():
            container.mux(packet)
    2. Close the file:
        container.close()
    """
    container.close()

def extract_audio(video_path, audio_path="extract.mp3"):
    # 报错
    """
Audio frame: pts 0, time 0.000000Encoder did not produce proper pts, making some up.
Audio frame: pts 1024, time 0.023220Traceback (most recent call last):
  File "/Users/ianvzs/demo_test/ffmpeg_some/hello_av.py", line 102, in <module>
    extract_audio(path)
  File "/Users/ianvzs/demo_test/ffmpeg_some/hello_av.py", line 87, in extract_audio
    for packet in out_stream.encode(frame):
  File "av/stream.pyx", line 164, in av.stream.Stream.encode
  File "av/codec/context.pyx", line 482, in av.codec.context.CodecContext.encode
  File "av/audio/codeccontext.pyx", line 42, in av.audio.codeccontext.AudioCodecContext._prepare_frames_for_encode
  File "av/audio/resampler.pyx", line 101, in av.audio.resampler.AudioResampler.resample
  File "av/filter/graph.pyx", line 211, in av.filter.graph.Graph.push
  File "av/filter/context.pyx", line 89, in av.filter.context.FilterContext.push
  File "av/error.pyx", line 336, in av.error.err_check
av.error.ValueError: [Errno 22] Invalid argument
"""
    return
    in_container = av.open(video_path)
    in_stream = in_container.streams.get(audio=0)[0]

    out_container = av.open(audio_path, 'w')
    out_stream = out_container.add_stream('mp3')

    for frame in in_container.decode(in_stream):
        print('\rAudio frame: pts %d, time %f'%(frame.pts, frame.time), end = '')
        frame.pts = None
        for packet in out_stream.encode(frame):
            out_container.mux(packet)
        for packet in out_stream.encode(None):
            out_container.mux(packet)
        out_container.close()

def audio_frame(audio_path):
    import numpy as np

    in_container = av.open(audio_path)
    stream = in_container.streams.get(audio=0)[0]
    for frame in in_container.decode(stream):
        print('\rFrame info: pts %d, time %f'%(frame.pts, frame.time), end = '')
        frame_value = frame.to_ndarray()[0]

def get_net_video(url):
    import cv2

    #video = av.open('rtsp://admin:ts123456@10.21.38.241:554', 'r') video = av.open('url', 'r')
    video = av.open(url, 'r')
    index = 0
    try:
        for frame in video.decode():
            img = frame.to_ndarray(format='bgr24')
            cv2.imshow("Test", img)
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break
    except Exception as e:
        print('fate erro:{}'.format(e))
    cv2.destroyAllWindows()

if __name__ == "__main__":
    import os
    home = os.environ.get("HOME")

    path = os.path.join(home, "Desktop", "audio_tagging_demo.mp4")
    # https://paddlespeech.bj.bcebos.com/PaddleAudio/audio_tagging_demo.mp4
    # all_frame(path)
    # key_frame(path)
    # composite_video("composite.mp4")
    # extract_audio(path)
    get_net_video("https://paddlespeech.bj.bcebos.com/PaddleAudio/audio_tagging_demo.mp4")
