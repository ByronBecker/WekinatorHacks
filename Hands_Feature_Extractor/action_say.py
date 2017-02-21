

import OSC
import subprocess


def handposition(addr, tags, data, client_address):
    txt = "OSCMessage '%s' from %s: " % (addr, client_address)
    txt += str(data)
    print(txt)
    fltdata = data[0]
    print(fltdata)

    if fltdata == 2.0:
        subprocess.call('say "Clap your hands!"', shell=True)
    elif fltdata == 3.0:
        subprocess.call('say "Field Goal, its good!"', shell=True)
    elif fltdata == 4.0:
        subprocess.call('say "Bring me closer you robot!"', shell=True)
    elif fltdata == 5.0:
        subprocess.call('say "Its gonna be huge!"', shell=True)

if __name__ == "__main__":

    listen = OSC.OSCServer(('127.0.0.1', 12000))
    listen.addMsgHandler('/handpos', handposition)
    listen.serve_forever()
