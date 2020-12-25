import os
from datetime import datetime
from pygame import mixer
import time
import shutil
from tkinter import *
from tkinter.filedialog import askopenfilename
from colorama import init, Fore, Style

init(autoreset=True)
print(
    Fore.LIGHTGREEN_EX + "\nHealthy Reminder and log System by ddevil13.\n\nThis Program will remind you to Drink "
                         "water every 30 minutes, to do Eye exercise every 40 minutes and any physical exercise every "
                         "hour.\n\nIt will also keep log of your "
                         "activity so that you can check your activity later.\nYou can change interval time as per "
                         "your need.\n\nIn case of any error close and re-open or re-run program\n\nPlease!! Read all "
                         "the instructions and follow strictly.")

# This will run a clock
# while True:
#     localtime = time.localtime()
#     result = time.strftime("%I:%M:%S %p", localtime)
#     print(result,end="",flush=True)
#     print("\r",end="",flush=True)
#     time.sleep(1)
#
#
# water.mp3
# eyes.mp3
# physical.mp3
# WATER.txt
# PHYSICAL.txt
# EYE.txt
keyword = ""
music = ""
fname = ""
root = ""


def start_necessary_file_check():
    if os.path.exists("./res/ring/water.mp3"):
        pass
    else:
        init(autoreset=True)
        print(Fore.LIGHTRED_EX + "\nAlarm for Drink water not Exists. Try Data Reset option.\nIf problem persist "
                                 "contact developer.")
        main()
    if os.path.exists("./res/ring/eye.mp3"):
        pass
    else:
        init(autoreset=True)
        print(
            Fore.LIGHTRED_EX + "\nAlarm for Drink water not Exists. Try Data Reset option.\nIf problem persist "
                               "contact developer.")
        main()
    if os.path.exists("./res/ring/physical.mp3"):
        pass
    else:
        init(autoreset=True)
        print(
            Fore.LIGHTRED_EX + "\nAlarm for Drink water not Exists. Try Data Reset option.\nIf problem persist "
                               "contact developer.")
        main()
    if os.path.exists("./res/interval/interval.txt"):
        pass
    else:
        init(autoreset=True)
        print(
            Fore.LIGHTRED_EX + "\nDetails about Interval time not Exists. Set Interval Time First or Try Data Reset "
                               "option.\nIf problem persist contact developer.")
        main()


def getint(massage):
    try:
        x = int(input(massage))
    except ValueError:
        init(autoreset=True)
        print(Fore.LIGHTRED_EX + "\nGive Proper Input!")
        x = getint(massage)
    return x


def logappend(logof, log):
    """ This will create a file with name of activity and take logs of activity after checkcondition function
    :param logof: Type of activity for what log is written.
    :param log: What log to be entered.
    :return: none
    """
    with open(f"./res/log/{logof}.txt", "a") as f:
        f.write(f"At {datetime.now()} i {log}\n")


def logread(logof):
    """
    This will read written logs for particular activity
    :param logof: Activity for which log is to be read
    :return: none
    """
    with open(f"./res/log/{logof}.txt") as f:
        init(autoreset=True)
        print(Fore.LIGHTYELLOW_EX + str(f.readlines()))


def cnr(src_filepath, nfname):
    """
    Will copy music file from specified path to ./res/ring.
    :param src_filepath: Path specified by user of music file.
    :param nfname: file name that we need for our purpose
    :return: none
    """
    ofname = src_filepath.split("/")  # ofname: Old file name is the name of music file in path specified by user
    ofname = ofname[len(ofname) - 1]
    filename = ofname.split(".")
    filetype = filename[len(filename) - 1]
    if filetype != "mp3":
        init(autoreset=True)
        print(Fore.LIGHTRED_EX + "File Type not suported please select another file.(Only .mp3 allowed.)")
        changering()
    else:
        pass
    dst_dir = os.path.join(os.curdir, "res/ring")
    shutil.copy(src_filepath, dst_dir)
    dst_file = os.path.join(dst_dir, ofname)
    new_dest_fname = os.path.join(dst_dir, nfname)
    try:
        os.rename(dst_file, new_dest_fname)
    except FileExistsError:
        os.remove(new_dest_fname)
        os.rename(dst_file, new_dest_fname)


def play_music(music1):
    """
    Will load music to play as alarm
    :param music1: name of music file you want to play
    :return: none
    """
    mixer.init()
    mixer.music.load(music1)
    mixer.music.set_volume(0.7)
    mixer.music.play(10)


def stop_music():
    """
    Stops the music
    :return: none
    """
    mixer.music.stop()


def check_condition(code, que):
    """
    This will ask user wheather activity is completed or not and if completed will stop music
    :param code: Key word to stop already running alarm
    :param que: Question to be asked to user about activity
    :return: none
    """
    while True:
        global keyword
        codevar = input(f"Had you {que} ? Enter 'Done' if completed: ").upper()
        if codevar == code:
            stop_music()
            init(autoreset=True)
            print(Fore.LIGHTGREEN_EX + "Very Good.")
            keyword = ""
            break
        elif codevar == "EXIT":
            keyword = "EXIT"
            mixer.music.stop()
            mixer.quit()
            init(autoreset=True)
            print(Fore.LIGHTRED_EX + "\nTimer Stoped.")
            break
        else:
            init(autoreset=True)
            print(Fore.LIGHTBLUE_EX + "\nWhat did you said?\nI'm unable to understand that.")


def openfile():
    global root, fname
    root = Tk()
    fname = askopenfilename()
    root.destroy()
    return fname


def changering():
    while True:
        ringnum = getint(
            "\nFor what activity you want to change Alarm Ring? (1):Drink Water,(2):Eye Exercise,(3):Physical Exercise,"
            "(4):Main Menu: ")
        if ringnum == 1:
            try:
                openfile()
                cnr(fname, "water.mp3")
                init(autoreset=True)
                print(Fore.LIGHTGREEN_EX + "\nAlarm Ring changed Successfully.")
                break
            except FileNotFoundError:
                init(autoreset=True)
                print(Fore.LIGHTRED_EX + "\nPlease Select a file.")
            except Exception as e:
                init(autoreset=True)
                print(Fore.LIGHTRED_EX + str(e))
                main()
        elif ringnum == 2:
            try:
                openfile()
                cnr(fname, "eye.mp3")
                init(autoreset=True)
                print(Fore.LIGHTGREEN_EX + "\nAlarm Ring changed Successfully.")
                break
            except FileNotFoundError:
                init(autoreset=True)
                print(Fore.LIGHTRED_EX + "\nPlease Select a file.")
            except Exception as e:
                init(autoreset=True)
                print(Fore.LIGHTRED_EX + str(e))
                main()
        elif ringnum == 3:
            try:
                openfile()
                cnr(fname, "physical.mp3")
                init(autoreset=True)
                print(Fore.LIGHTGREEN_EX + "\nAlarm Ring changed Successfully.")
                break
            except FileNotFoundError:
                init(autoreset=True)
                print(Fore.LIGHTRED_EX + "\nPlease Select a file.")
            except Exception as e:
                init(autoreset=True)
                print(Fore.LIGHTRED_EX + str(e))
                main()
        elif ringnum == 4:
            main()
        else:
            init(autoreset=True)
            print(Fore.LIGHTRED_EX + "\nWrong Input!. Give input from given options.")


def changeinterval():
    """
    This will change interval time by taking user input and save it to interval file
    :return: none
    """
    while True:
        init(autoreset=True)
        print(
            Fore.LIGHTGREEN_EX + "\nSet Interval Time in Minutes. In case you not want to set particular alarm type"
                                 " '0'")
        a = getint("Enter Time Interval for Drinking Water(In Miunutes): ")
        b = getint("Enter Time Interval for Eye Exercise(In Miunutes): ")
        c = getint("Enter Time Interval for Physical Exercise(In Miunutes): ")
        if a == 0 and b == 0 and c == 0:
            init(autoreset=True)
            print(Fore.LIGHTRED_EX + "\nYou have not set any alarm. Set at least one to continue timer!!")
            changeinterval()
        else:
            pass
        with open("./res/interval/interval.txt", "w") as f:
            f.write(f"{a}\n")
            f.write(f"{b}\n")
            f.write(f"{c}\n")
        init(autoreset=True)
        print(Fore.LIGHTGREEN_EX + "\nTime Interval Changed Succesfully.")
        break


def datareset():
    while True:
        init()
        print(Fore.LIGHTRED_EX)
        resetflag = getint("\nAre you sure your all data will be removed?(1):Yes,(0):No: ")
        init(Style.RESET_ALL)
        if resetflag == 1:
            with open("./res/interval/interval.txt", "w") as f:
                f.write(f"30\n")
                f.write(f"40\n")
                f.write(f"60\n")
            init(autoreset=True)
            print(Fore.LIGHTGREEN_EX + "\nInterval Time set to Default.")
            try:
                cnr("./res/backup/water.mp3", "water.mp3")
                cnr("./res/backup/eye.mp3", "eye.mp3")
                cnr("./res/backup/physical.mp3", "physical.mp3")
            except FileNotFoundError:
                init(autoreset=True)
                print(
                    Fore.LIGHTRED_EX + "\nResources of software is corrupted. Reinstall software or contact developer "
                                       "for fast solution.")
                main()
            except Exception as e:
                init(autoreset=True)
                print(Fore.LIGHTRED_EX + str(e))
            if os.path.exists("./res/log/PHYSICAL.txt"):
                os.remove("./res/log/PHYSICAL.txt")
                init(autoreset=True)
                print(Fore.LIGHTGREEN_EX + "\nData of Physical Exercise deleted successfully.")
            else:
                init(autoreset=True)
                print(Fore.LIGHTRED_EX + "\nNo data of Physical Exercise available to delete.")
            if os.path.exists("./res/log/EYE.txt"):
                os.remove("./res/log/EYE.txt")
                init(autoreset=True)
                print(Fore.LIGHTGREEN_EX + "\nData of Eye Exercise deleted successfully.")
            else:
                init(autoreset=True)
                print(Fore.LIGHTRED_EX + "\nNo data of Eye Exercise available to delete.")
            if os.path.exists("./res/log/WATER.txt"):
                os.remove("./res/log/WATER.txt")
                init(autoreset=True)
                print(Fore.LIGHTGREEN_EX + "\nData of Drink Water deleted successfully.")
            else:
                init(autoreset=True)
                print(Fore.LIGHTRED_EX + "\nNo data of Drink Water available to delete.")
            break
        elif resetflag == 0:
            break
        else:
            init(autoreset=True)
            print(Fore.LIGHTRED_EX + "\nWrong Input. Try from Given options.")
    return resetflag


def getinterval():
    """
    This will load interval time from interval file
    :return: lst1: list of interval time that will be loaded to main function
    """
    with open("./res/interval/interval.txt") as f:
        lst0 = f.readlines()
        str1 = "".join(lst0)
        lst1 = str1.split("\n")
        return lst1


def main():
    """
    Main function of code that will do the main work of program every function will be executed within this
    :return: none
    """
    while True:  # making a while loop of activities so that it keeps on continue unless stoped.
        logof = ["WATER", "EYE", "PHYSICAL"]
        print(
            "\nOptions: (1):Start timer (2):Show Log (3):Change Interval Time (4):Set Custom Alarm Ring (5): Reset "
            "Data(Log and Interval Time)  (6):Exit")
        todo = getint("Enter what you want to do: ")
        if todo == 1:
            global keyword, music
            start_necessary_file_check()
            try:
                interval = getinterval()  # Get the interval time
            except FileNotFoundError:
                init(autoreset=True)
                print(Fore.LIGHTRED_EX + "\nNo record of Time intervals found.")
                print(Fore.LIGHTGREEN_EX + "\nFirst goto Change Interval section and set interval time.")
                break
            except Exception as e:
                init(autoreset=True)
                print(Fore.LIGHTRED_EX + str(e))
                break
            waterinterval = int(interval[0]) * 60  # Converted minutes in seconds
            eyeinterval = int(interval[1]) * 60
            physicalinterval = int(interval[2]) * 60
            init(autoreset=True)
            print(
                Fore.LIGHTGREEN_EX + "\nRemember! This timer will continue till you close the window or Type 'Exit' at "
                                     "any reminder to go back to main menu.")
            init_water = time.time()  # Initiated current time.
            init_eye = time.time()
            init_physical = time.time()
            while True:
                if waterinterval != 0 and time.time() - init_water > waterinterval:
                    init(autoreset=True)
                    print(Fore.LIGHTGREEN_EX + "\n\nTime's up now Drink Water.")
                    # TO find time elapsed from
                    # initiated time so that
                    # alarm can be rang if interval isexceeded
                    try:
                        music = "./res/ring/water.mp3"
                        play_music(music)
                    except FileNotFoundError:
                        init(autoreset=True)
                        print(
                            Fore.LIGHTRED_EX + f"\nFile {music}.mp3 does not exist. It maybe due to broken package "
                                               f"contact developer to resolve the issue.")
                        break
                    except ModuleNotFoundError:
                        init(autoreset=True)
                        print(Fore.LIGHTRED_EX + "\nFile type not supported. Supported FileType: .mp3, .wav")
                        break
                    except Exception as e:
                        init(autoreset=True)
                        print(Fore.LIGHTRED_EX + str(e))
                        break
                    check_condition("DONE", "drink your water")
                    if keyword == "EXIT":
                        break
                    else:
                        pass
                    init_water = time.time()  # To reinitiate time for next interval of time
                    logappend("WATER", "Drank Water")
                if eyeinterval != 0 and time.time() - init_eye > eyeinterval:  # same thing for eye activity
                    init(autoreset=True)
                    print(Fore.LIGHTGREEN_EX + "\nTime's up now do Some Eye Exercises.")
                    try:
                        music = "./res/ring/eye.mp3"
                        play_music(music)
                    except FileNotFoundError:
                        init(autoreset=True)
                        print(
                            Fore.LIGHTRED_EX + f"\nFile {music}.mp3 does not exist. It maybe due to broken package "
                                               f"contact developer to resolve the issue.")
                        break
                    except ModuleNotFoundError:
                        init(autoreset=True)
                        print(Fore.LIGHTRED_EX + "\nFile type not supported. Supported FileType: .mp3, .wav")
                        break
                    except Exception as e:
                        init(autoreset=True)
                        print(Fore.LIGHTRED_EX + str(e))
                        break

                    check_condition("DONE", "completed your eye exercise")
                    if keyword == "EXIT":
                        break
                    init_eye = time.time()
                    logappend("EYE", "Did Eye exercises")
                if physicalinterval != 0 and time.time() - init_physical > physicalinterval:  # for physical activity
                    init(autoreset=True)
                    print(Fore.LIGHTGREEN_EX + "\nTime's up now do some Physical Exercises.")
                    try:
                        music = "./res/ring/physical.mp3"
                        play_music(music)
                    except FileNotFoundError:
                        init(autoreset=True)
                        print(
                            Fore.LIGHTRED_EX + f"\nFile {music}.mp3 does not exist. It maybe due to broken package "
                                               f"contact developer to resolve the issue.")
                        break
                    except ModuleNotFoundError:
                        init(autoreset=True)
                        print(Fore.LIGHTRED_EX + "\nFile type not supported. Supported FileType: .mp3, .wav")
                        break
                    except Exception as e:
                        init(autoreset=True)
                        print(Fore.LIGHTRED_EX + str(e))
                        break

                    check_condition("DONE", "completed your physical exercise")
                    if keyword == "EXIT":
                        break
                    init_physical = time.time()
                    logappend("PHYSICAL", "Did Physcial Exercise")

                localtime = time.localtime()  # TO run an infinite clock when timer runs
                result = time.strftime("%I:%M:%S %p", localtime)
                init()
                print(result, end="", flush=True)
                print("\r", end="", flush=True)
                init(Style.RESET_ALL)
                time.sleep(1)
            # code to be executed when start alarm
        elif todo == 2:  # Activity of reading logs
            while True:
                logofinput = input("\nWhat log you want to open: \nWATER/EYE/PHYSICAL or Exit for main menu: ").upper()
                if logofinput in logof:
                    try:
                        logread(logofinput)
                    except FileNotFoundError:
                        init(autoreset=True)
                        print(
                            Fore.LIGHTRED_EX + "\nNo Log found. First make some log by doing activity than come "
                                               "again to check log.")
                    except Exception as e:
                        init(autoreset=True)
                        print(Fore.LIGHTRED_EX + str(e))

                elif logofinput == "EXIT":
                    print("Back to Main Menu")
                    break
                else:
                    init(autoreset=True)
                    print(Fore.LIGHTRED_EX + "\nWrong Input. Try from Given options.")
        elif todo == 3:  # set interval time
            changeinterval()
        elif todo == 4:
            changering()
        elif todo == 5:
            resetflag = datareset()
            if resetflag == 0:
                break
            elif resetflag == 1:
                init(autoreset=True)
                print(Fore.LIGHTGREEN_EX + "\nData Reset Successful.")
        elif todo == 6:
            init(autoreset=True)
            print(
                Fore.LIGHTGREEN_EX + "\nHealthy Reminder and log System by ddevil13.\n\nThank you for using the program."
                                     "\n\nType exit to close Terminal Window. ")
            sys.exit(0)
        else:
            init(autoreset=True)
            print(Fore.LIGHTRED_EX + "\nWrong Input. Try from Given options.")
    main()  # Recursion of main function


if __name__ == '__main__':  # file run when executed
    main()  # main function called
