import subprocess
import sys

def getServerList(serverListPathFile):
    serverList = []
    file = open(serverListPathFile, 'r')

    for registro in file.readlines():
        serverList.append(registro.rstrip("\n\r"))
        #print('Server:' + registro)
    file.close
    return serverList


def main(username, userpassword, serverListPathFile):
    for i in getServerList(serverListPathFile):
        cmdStringCreateUser = "ssh user@"+i+" ' echo password | sudo useradd -g sudoers -p" + userpassword + " " + username+"'"
        cmdStringEnableFirtsPasswordChange = "ssh user@"+i+" 'echo password | sudo chage -d 0 " + username + "'"
        linuxcmdAdduser = subprocess.Popen(cmdStringCreateUser, shell = True)
        linuxcmdFirstPassword = subprocess.Popen(cmdStringEnableFirtsPasswordChange, shell = True)
        outputAdduser = linuxcmdAdduser.communicate()
        outputFirstPassword = linuxcmdFirstPassword.communicate()
        print(outputAdduser)
        print(outputFirstPassword)



if __name__ == "__main__":
    main(sys.argv[1],sys.argv[2],sys.argv[3])