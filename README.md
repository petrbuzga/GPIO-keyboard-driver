# Matrix keyboard driver using GPIO on RaspberryPi

A userspace driver that starts at system boot as a systemd service. Using root user permissions, this service runs a Python program that scans at regular intervals individual columns of the keyboard connected via GPIO pins. The main loop utilizes an infinite while loop. In the case of detection key press is called the corresponding function to process the event.

Work is part of the Bachelor's thesis (https://www.vut.cz/studenti/zav-prace/detail/149472)



