'''
Create a program that once executed the programs
prints Hello  instantly first, then it prints it after 1 second,
then after 2, 3, and then the program prints out the message "End of the Loop" and stops.
'''
import time

cnt = 0

while True:
    if cnt<4:
        print("Hello")
        time.sleep(cnt)
        cnt += 1
    else:
        print("End of Loop")
        break
