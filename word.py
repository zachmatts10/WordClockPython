# Import functions
import Matrix
import clock
import datetime

clockList = [clock.one, clock.two, clock.three, clock.four, clock.five, clock.six, clock.seven, clock.eight, clock.nine, clock.ten, clock.eleven, clock.twelve, clock.thirteen, clock.fourteen, clock.quarter, clock.sixteen, clock.seventeen, clock.eighteen, clock.nineteen, clock.twenty, clock.twentyone, clock.twentytwo, clock.twentythree, clock.twenty.four, clock.twentyfive, clock.twentysix, clock.twentyseven, clock.twentyeight, clock.twentynine, clock.half, clock.Hone, clock.Htwo, clock.Hthree, clock.Hfour, clock.Hfive, clock.Hsix, clock.Hseven, clock.Height, clock.Hnine, clock.Hten, clock.Heleven, clock.Htwelve, clock.the, clock.time, clock.iss, clock.minute, clock.minutes, clock.past, clock.to, clock.oclock, clock.inn, clock.at, clock.night, clock.the, clock.morning, clock.evening, clock.afternoon]
clockListMinute = [clock.one, clock.two, clock.three, clock.four, clock.five, clock.six, clock.seven, clock.eight, clock.nine, clock.ten, clock.eleven, clock.twelve, clock.thirteen, clock.fourteen, clock.quarter, clock.sixteen, clock.seventeen, clock.eighteen, clock.nineteen, clock.twenty, clock.twentyone, clock.twentytwo, clock.twentythree, clock.twentyfour, clock.twentyfive, clock.twentysix, clock.twentyseven, clock.twentyeight, clock.twentynine, clock.half] #0-29
clockListHour = [clock.Hone, clock.Htwo, clock.Hthree, clock.Hfour, clock.Hfive, clock.Hsix, clock.Hseven, clock.Height, clock.Hnine, clock.Hten, clock.Heleven, clock.Htwelve] #0-11
clockListAdd = [clock.the, clock.time, clock.iss, clock.minute, clock.minutes, clock.past, clock.to, clock.oclock, clock.inn, clock.at, clock.night, clock.the, clock.morning, clock.evening, clock.afternoon, clock.noon] #0-15
# A nice start animation
for m in clockList:
        table = [[0 for g in range (32)] for h in range (32)]
        m (table)
        x = 0
        while x <= 5:
                Matrix.panel (table)
                x = x + 1

### it really starts from here
# simple endless loop East German system
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
        # Create an empty table
        table = [[0 for g in range (32)] for h in range (32)]
        # It is always lit.
        clockListAdd [0] (table)
        clockListAdd [1] (table)
        clockListAdd [2] (table)
        
        if (minute <= 30):
                if (minute==0):
                        clockListAdd [7] (table)
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
                        elif (hour>=20):
                                clockListHour [hour-12] (table)
                                clockListAdd [9] (table)
                                clockListAdd [10] (table)
                elif (minute==1):
                        clockListMinute [minute-1] (table)
                        clockListAdd [3] (table)
                        clockListAdd [5] (table)
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
                        elif (hour>=20):
                                clockListHour [hour-12] (table)
                                clockListAdd [9] (table)
                                clockListAdd [10] (table)
                else:
                        clockListMinute [minute-1] (table)
                        clockListAdd [4] (table)
                        clockListAdd [5] (table)
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
                        elif (hour>=20):
                                clockListHour [hour-12] (table)
                                clockListAdd [9] (table)
                                clockListAdd [10] (table)
        elif (minute > 30):
                clockListMinute [59-minute] (table)
                if (minute==59):
                        clockListAdd [3] (table)
                        clockListAdd [6] (table)
                        if (hour<4):
                                clockListHour [hour+1] (table)
                                clockListAdd [9] (table)
                                clockListAdd [10] (table)
                        elif (hour<12):
                                clockListHour [hour+1] (table)
                                clockListAdd [8] (table)
                                clockListAdd [11] (table)
                                clockListAdd [12] (table)
                        elif (hour==12):
                                clockListHour [hour+1] (table)
                                clockListAdd [15] (table)
                        elif (hour<17):
                                clockListHour [hour+1] (table)
                                clockListAdd [8] (table)
                                clockListAdd [11] (table)
                                clockListAdd [14] (table)
                        elif (hour<20):
                                clockListHour [hour+1] (table)
                                clockListAdd [8] (table)
                                clockListAdd [11] (table)
                                clockListAdd [13] (table)
                        elif (hour<23):
                                clockListHour [hour+1] (table)
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
                                clockListHour [hour+1] (table)
                                clockListAdd [9] (table)
                                clockListAdd [10] (table)
                        elif (hour<12):
                                clockListHour [hour+1] (table)
                                clockListAdd [8] (table)
                                clockListAdd [11] (table)
                                clockListAdd [12] (table)
                        elif (hour==12):
                                clockListHour [hour+1] (table)
                                clockListAdd [15] (table)
                        elif (hour<17):
                                clockListHour [hour-11] (table)
                                clockListAdd [8] (table)
                                clockListAdd [11] (table)
                                clockListAdd [14] (table)
                        elif (hour<20):
                                clockListHour [hour-11] (table)
                                clockListAdd [8] (table)
                                clockListAdd [11] (table)
                                clockListAdd [13] (table)
                        elif (hour<23):
                                clockListHour [hour-11] (table)
                                clockListAdd [9] (table)
                                clockListAdd [10] (table)
                        elif (hour==23):
                                clockListHour [0] (table)
                                clockListAdd [9] (table)
                                clockListAdd [10] (table)           

#        for n in range (30-second, 30):
#               table [n-2] [2] = 1
#        if (30 <= second <= 60):
#                for n in range (second-30):
#                        table [n] [29] = 1


        Matrix.panel (table)

