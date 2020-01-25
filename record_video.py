import logging 
import picamera
import time 
import subprocess
import os


class record_video:

    def __init__(self):
        self.cam = picamera.PiCamera()
        self.record_dir = 'record_files'
        self.file_h264 = self.record_dir + '/video.h264'
        self.file_mp4 = self.record_dir + '/video.mp4'

    def start_record(self, sleep_time):
        logging.info('Start record')
        self.cam.start_recording(self.file_h264)
        time.sleep(sleep_time)

    def stop_record(self):
        logging.info('Stop record')
        self.cam.stop_recording()

    def video_convert_to_mp4(self):
        logging.info('Converting video')
        if os.path.isfile(self.file_h264):
            cmd = f'ffmpeg -y -framerate 24 -i {self.file_h264} -c copy {self.file_mp4}'
            subprocess.call(cmd, shell=True)
    
    def record_video_time(self, sleep_time):
        logging.info(f'Record a video with {sleep_time} sec')
        self.start_record(sleep_time)
        self.stop_record()
        self.video_convert_to_mp4()

# cam = picamera.PiCamera()

# record_dir = 'record_files'

# file_h264 = record_dir + '/video.h264'

# file_mp4 = record_dir + '/video.mp4'

# cam.start_recording(file_h264)

# time.sleep(10)

# cam.stop_recording()

# if os.path.isfile(file_h264) :
#     cmd = f'ffmpeg -y -framerate 24 -i {file_h264} -c copy {file_mp4}'
#     subprocess.call(cmd, shell=True)


