#!/usr/bin/env python
from samplebase import SampleBase
import clock
import datetime
#import word

clockListMinute = [clock.one, clock.two, clock.three, clock.four, clock.five, clock.six, clock.seven, clock.eight, clock.nine, clock.ten, clock.eleven, clock.twelve, clock.thirteen, clock.fourteen, clock.quarter, clock.sixteen, clock.seventeen, clock.eighteen, clock.nineteen, clock.twenty, clock.twentyone, clock.twentytwo, clock.twentythree, clock.twentyfour, clock.twentyfive, clock.twentysix, clock.twentyseven, clock.twentyeight, clock.twentynine, clock.half] #0-29
clockListHour = [clock.Hone, clock.Htwo, clock.Hthree, clock.Hfour, clock.Hfive, clock.Hsix, clock.Hseven, clock.Height, clock.Hnine, clock.Hten, clock.Heleven, clock.Htwelve] #0-11
clockListAdd = [clock.the, clock.time, clock.iss, clock.minute, clock.minutes, clock.past, clock.to, clock.oclock, clock.inn, clock.at, clock.night, clock.the2, clock.morning, clock.evening, clock.afternoon, clock.noon] #0-15

class FinalClock(SampleBase):
    def __init__(self, *args, **kwargs):
        super(SimpleSquare, self).__init__(*args, **kwargs)

    def run(self):
        offset_canvas = self.matrix.CreateFrameCanvas()
        while True:
            # Record local time in the RPi
            time = datetime.datetime.now ()
            # Set variables for hours, minutes, seconds
            hour = time.strftime ("%H")
            minute = time.strftime ("%M")
            second = time.strftime ("%S")
            # Make the whole thing available as an integer
            hour = int (hour)
            minute = int (minute)
            second = int (second)
            print (hour, minute, second)
            # Create an empty table
            table = [[0 for g in range (33)] for h in range (33)]
            # It is always lit.
            clockListAdd [0] (table)
            clockListAdd [1] (table)
            clockListAdd [2] (table)

            if (minute <= 30):
                    if (minute==0):
                            clockListAdd [7] (table)
                            if (hour<4):
                                    clockListHour [hour-1] (table)
                                    clockListAdd [9] (table)
                                    clockListAdd [10] (table)
                            elif (hour<12):
                                    clockListHour [hour-1] (table)
                                    clockListAdd [8] (table)
                                    clockListAdd [11] (table)
                                    clockListAdd [12] (table)
                            elif (hour==12):
                                    clockListHour [hour-1] (table)
                                    clockListAdd [15] (table)
                            elif (hour<17):
                                    clockListHour [hour-13] (table)
                                    clockListAdd [8] (table)
                                    clockListAdd [11] (table)
                                    clockListAdd [14] (table)
                            elif (hour<20):
                                    clockListHour [hour-13] (table)
                                    clockListAdd [8] (table)
                                    clockListAdd [11] (table)
                                    clockListAdd [13] (table)
                            elif (hour>=20):
                                    clockListHour [hour-13] (table)
                                    clockListAdd [9] (table)
                                    clockListAdd [10] (table)
                    elif (minute==1):
                            clockListMinute [minute-1] (table)
                            clockListAdd [3] (table)
                            clockListAdd [5] (table)
                            if (hour<4):
                                    clockListHour [hour-1] (table)
                                    clockListAdd [9] (table)
                                    clockListAdd [10] (table)
                            elif (hour<12):
                                    clockListHour [hour-1] (table)
                                    clockListAdd [8] (table)
                                    clockListAdd [11] (table)
                                    clockListAdd [12] (table)
                            elif (hour==12):
                                    clockListHour [hour-1] (table)
                                    clockListAdd [15] (table)
                            elif (hour<17):
                                    clockListHour [hour-13] (table)
                                    clockListAdd [8] (table)
                                    clockListAdd [11] (table)
                                    clockListAdd [14] (table)
                            elif (hour<20):
                                    clockListHour [hour-13] (table)
                                    clockListAdd [8] (table)
                                    clockListAdd [11] (table)
                                    clockListAdd [13] (table)
                            elif (hour>=20):
                                    clockListHour [hour-13] (table)
                                    clockListAdd [9] (table)
                                    clockListAdd [10] (table)
                    else:
                            clockListMinute [minute-1] (table)
                            clockListAdd [4] (table)
                            clockListAdd [5] (table)
                            if (hour<4):
                                    clockListHour [hour-1] (table)
                                    clockListAdd [9] (table)
                                    clockListAdd [10] (table)
                            elif (hour<12):
                                    clockListHour [hour-1] (table)
                                    clockListAdd [8] (table)
                                    clockListAdd [11] (table)
                                    clockListAdd [12] (table)
                            elif (hour==12):
                                    clockListHour [hour-1] (table)
                                    clockListAdd [15] (table)
                            elif (hour<17):
                                    clockListHour [hour-13] (table)
                                    clockListAdd [8] (table)
                                    clockListAdd [11] (table)
                                    clockListAdd [14] (table)
                            elif (hour<20):
                                    clockListHour [hour-13] (table)
                                    clockListAdd [8] (table)
                                    clockListAdd [11] (table)
                                    clockListAdd [13] (table)
                            elif (hour>=20):
                                    clockListHour [hour-13] (table)
                                    clockListAdd [9] (table)
                                    clockListAdd [10] (table)
            elif (minute > 30):
                    clockListMinute [59-minute] (table)
                    if (minute==59):
                            clockListAdd [3] (table)
                            clockListAdd [6] (table)
                            if (hour<4):
                                    clockListHour [hour] (table)
                                    clockListAdd [9] (table)
                                    clockListAdd [10] (table)
                            elif (hour<12):
                                    clockListHour [hour] (table)
                                    clockListAdd [8] (table)
                                    clockListAdd [11] (table)
                                    clockListAdd [12] (table)
                            elif (hour==12):
                                    clockListHour [hour] (table)
                                    clockListAdd [15] (table)
                            elif (hour<17):
                                    clockListHour [hour-12] (table)
                                    clockListAdd [8] (table)
                                    clockListAdd [11] (table)
                                    clockListAdd [14] (table)
                            elif (hour<20):
                                    clockListHour [hour-12] (table)
                                    clockListAdd [8] (table)
                                    clockListAdd [11] (table)
                                    clockListAdd [13] (table)
                            elif (hour<23):
                                    clockListHour [hour-12] (table)
                                    clockListAdd [9] (table)
                                    clockListAdd [10] (table)
                            elif (hour==23):
                                    clockListHour [0] (table)
                                    clockListAdd [9] (table)
                                    clockListAdd [10] (table)        
                    else:
                            clockListAdd [4] (table)
                            clockListAdd [6] (table) 
                            if (hour<4):
                                    clockListHour [hour] (table)
                                    clockListAdd [9] (table)
                                    clockListAdd [10] (table)
                            elif (hour<12):
                                    clockListHour [hour] (table)
                                    clockListAdd [8] (table)
                                    clockListAdd [11] (table)
                                    clockListAdd [12] (table)
                            elif (hour==12):
                                    clockListHour [hour] (table)
                                    clockListAdd [15] (table)
                            elif (hour<17):
                                    clockListHour [hour-12] (table)
                                    clockListAdd [8] (table)
                                    clockListAdd [11] (table)
                                    clockListAdd [14] (table)
                            elif (hour<20):
                                    clockListHour [hour-12] (table)
                                    clockListAdd [8] (table)
                                    clockListAdd [11] (table)
                                    clockListAdd [13] (table)
                            elif (hour<23):
                                    clockListHour [hour-12] (table)
                                    clockListAdd [9] (table)
                                    clockListAdd [10] (table)
                            elif (hour==23):
                                    clockListHour [0] (table)
                                    clockListAdd [9] (table)
                                    clockListAdd [10] (table) 
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
