in1 = str
print ("Command testing")
print ("Test the help command")
print ("Type 'help' to try out the command!")
in1 = str(input("FC://"))
if in1 == ("help"):
    print ("Help list")
    print ("DIR = Directory")
    print ("CLS = Clear screen")
    print ("HELP = Help guide")
    print ("RUN = Run a program/file")
    print ("DEL = Delete the selected file")
    print ("COLOR = Change the text color of the terminal")
    print ("EXIT = Shut down the system")
    print ("CD = Choose a directory, type .. or the directory name afterwards, and you will go to the next directory")
    print ("PLAY = Play the currently selected audio or video")
    print ("EJECT = Eject the system, make it ready for ejecting the drive")
    print ("NETW = Change the current network")
    print ("DISCON = Disconnect from the Internet, go offline")
    print ("DRCHECK = Test your drives memory")
    print ("SPCHK = Calculate the amount of space being used")
    print ("VMOUTRUN = Use this command to launch programs OUTSIDE of the hard drive operating system, and onto the targeted receiver device")
    print ("VMORUTOG = Toggle launching programs outside of the hard drive operating systems to the other device on and off")
    print ("COMPBLOG = View the file compatibility of the system")
    print ("PREVTOG = Toggle file previews")
    print ("UPDUSR2 = Check for updates for the network receiver device")
    print ("RENAME = Rename the selected file/directory")
    print ("URENAME = Undo the recent renaming action")
    print ("CALC = Run a calculator")
    print ("USR2 = change the settings for the receiver device")
    print ("*****")
    print ("The command worked!")
print (in1)
testconfirm = int(input("Did the setup look right? type 1 to confirm, type anything else and/or press enter to quit "))
if testconfirm == 1:
    print ("System setup successful!")
    print ("Shutting down, please wait")
else:
    print ("Shutting down")
    