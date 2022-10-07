#!/usr/bin/python
import os
import re
import subprocess
import sys

def main():
    for line in sys.stdin:
        m = re.match('^\s*#.*$',line)
        print(m)
        fields = line.strip().split(':')
        if m or len(fields) != 5:
            continue
        username = fields[0]
        password = fields[1]
        gecos = fields[3] + " " + fields[2] + ",,,"
        groups = fields[4].split(',')
        print ("Creating account for " +  username)
        cmd = ("/usr/sbin/adduser --disabled-password --gecos " + "'" +  gecos +  "'"  + " " + "'" +  username + "'")
        #print cmd
        os.system(cmd)
        print ("Setting the password for " +  username +"..." )
        cmd = ("/bin/echo -ne " + "'" +  password + "\n" +  password + "'" +  " | /usr/bin/sudo /usr/bin/passwd " + username)
        #print cmd
        os.system(cmd)
        for group in groups:
            if group != '-':
                print ("Assigning " + username + "  to the " +  group + "...")
                cmd = ("/usr/sbin/adduser " + username + " " +  group)
                #print cmd
                os.system(cmd)

if __name__ == '__main__':
    main()
        
