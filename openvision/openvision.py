#!/usr/bin/env python
from __future__ import division

import os
import sys
import inspect
import cv2
from PIL import Image
from numpy import matrix
from common.lanedetection import *
import common.track as track
import common.detect as detect


class vision(object):
    """docstring for vision."""
    def __init__(self, image):
        super(vision, self).__init__()
        self.image = image
        self.find_lanes()

    def find_lanes(self):
        lanes = lanedetect(self.image)
        lanes.show_image()


def main(video_path):
    cap = cv2.VideoCapture(video_path)

    ticks = 0

    lt = track.LaneTracker(2, 0.1, 500)
    ld = detect.LaneDetector(180)
    while cap.isOpened():
        precTick = ticks
        ticks = cv2.getTickCount()
        dt = (ticks - precTick) / cv2.getTickFrequency()

        ret, frame = cap.read()

        predicted = lt.predict(dt)

        lanes = ld.detect(frame)

        if predicted is not None:
            cv2.line(frame, (predicted[0][0], predicted[0][1]), (predicted[0][2], predicted[0][3]), (0, 0, 255), 5)
            cv2.line(frame, (predicted[1][0], predicted[1][1]), (predicted[1][2], predicted[1][3]), (0, 0, 255), 5)

        lt.update(lanes)

        cv2.imshow('', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


def main_old():
    prototyping_image = os.path.join(os.getcwd(), 'resources', 'frontfacing01.jpeg')
    auto_view = vision(prototyping_image)


if __name__ == "__main__":
    try:
        os.system('cls')
        main()
    except KeyboardInterrupt:
        "KeyboardInterrupt: exiting..."
else:
    "openvision.py must be run as the main script"
