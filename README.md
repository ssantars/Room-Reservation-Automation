# Room-Reservation-Automation
Automated Library Room Application for Gateway at University of California, Irvine using Python import Selenium

In DEMO phase 11/20/2018

Currently allows user to designate a 2 hour time gap (EX: 9:00 AM - 11:00PM) and either use the current date or a desired date inputted (EX: 2018-12-1). These imports create a string which that matches the "Title" of each tile on the UCI reservation website. Using xml path and this title it searches all the available rooms at gate way within the selected time slots and checks if it they are open. The first room it finds with appropriate reservations is choosen and proceeds to login the user and complete the check out. 

Phase 2
- Want to make this a program that runs on the command line to allow for easy use. 
-Incorporate options to allow for multiple users logins to locate a room together. Allowing a signle individual to use friend's logins to grab additional 2 hour time gap of the same room. 
