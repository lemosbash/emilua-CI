import os
import os.path
from subprocess import check_output 

path = ("emilua/", "emilua/build", "emilua/build/emilua")

def builder():
    if(os.path.exists(path[1]) == True):
        os.system("cd emilua/build && meson -D enable_tests=true -D enable_manpages=true ../")
        os.system("cd emilua/build && ninja")
        meson_tester()
    else:
        if(os.path.exists(path[0]) == True and os.path.exists(path[1]) == False):
            os.system("mkdir emilua/build && cd emilua/build && meson -D enable_tests=true -D enable_manpages = true ../")
            meson_tester()

def meson_tester():
    if (os.path.exists(path[2]) == False):
        print("build did not go well, tests cannot go further")        
    else: 
        if(os.path.exists(path[2]) == True):
            test = os.WEXITSTATUS(os.system("cd emilua/build && meson test"))
            if(test != 0):
                for x in range(5):
                    try:
                       err = check_output('cd emilua/build && meson_test')
                    except:
                        print("it wasn't possible to get the output from tests")
                       
            else:
                print("tests succeeded.")
                                
builder()



