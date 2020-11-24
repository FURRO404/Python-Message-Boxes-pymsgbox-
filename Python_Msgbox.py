#The specific program that I made, allowing the user to make their own pymsgbox
#It takes the original functions and implemenets user interactions

#PyMsgBox can be installed from PyPI with pip:
#pip install PyMsgBox

#OS X and Linux may require sudo to install the module:
#sudo pip install PyMsgBox


#=======================#
import pymsgbox
#Python_Msgbox.py
#=======================#

s=str(input("Pop-up box type (Alert, Confirm, Prompt, Password): "))

if s == "Alert":
    title1=str(input("Title here: "))
    text1=str(input("Text here: "))
    button1=str(input("Button here: "))
    pymsgbox.alert(text=text1, title=title1, button=button1)

elif s == "Confirm":
    title1=str(input("Title here: "))
    text1=str(input("Text here: "))
    button1=str(input("Button here: "))
    button2=str(input("Button here: "))
    pymsgbox.confirm(text=text1, title=title1, buttons=[button1, button2])

elif s == "Prompt":
    title1=str(input("Title here: "))
    text1=str(input("Text here: "))
    default1=str(input("Default: "))
    pymsgbox.prompt(text=text1, title=title1, default=default1)

elif s == "Password":
    title1=str(input("Title here: "))
    text1=str(input("Text here: "))
    default1=str(input("Default: "))
    mask1=str(input("Mask: "))
    pymsgbox.password(text=text1, title=title1, default=default1, mask=mask1)

else:
    print("Invalid dummy")
#===========FURRO404============#
