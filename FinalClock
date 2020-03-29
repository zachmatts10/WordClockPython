#!/usr/bin/env python
from samplebase import SampleBase
import clock
import datetime
import word


class FinalClock(SampleBase,clock,datetime):
    def __init__(self, *args, **kwargs):
        super(FinalClock, self).__init__(*args, **kwargs)

    def run(self):
        offset_canvas = self.matrix.CreateFrameCanvas()
        while True:
            for j in range (0, self.matrix.width):
                    for x in range(0, self.matrix.width):
                        if table [j] [i] == 1:
                            offset_canvas.SetPixel(j, i, 255, 255, 255)
            offset_canvas = self.matrix.SwapOnVSync(offset_canvas)


# Main function
if __name__ == "__main__":
    finalclock = FinalClock()
    if (not finalclock.process()):
        finalclock.print_help()
