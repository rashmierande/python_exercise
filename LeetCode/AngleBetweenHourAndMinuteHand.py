'''
 * Find small angle between hour and minute hand in analog clock
'''

import math

def findangle(hour, min):

    hourAngle = (hour%12)*360/12 + (min/60)*(360/12)
    minAngle = min*360/60
    angleDiff = abs(hourAngle - minAngle)
    if angleDiff < 360-angleDiff:
        return angleDiff
    else:
        return 360 - angleDiff

print(findangle(10, 15))
print(findangle(9, 45))


