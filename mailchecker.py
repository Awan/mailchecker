#!/usr/bin/env/python3

#  ▓▓▓▓▓▓▓▓▓▓ 
# ░▓ Author ▓ Abdullah <https://abdullah.today/> 
# ░▓▓▓▓▓▓▓▓▓▓ 
# ░░░░░░░░░░ 

import subprocess as sp
import imaplib
import time
import socket





msgs_were = 0
password_store = sp.check_output(['which', 'pass'])
""" For DWM bar, you can create a directory and then if you get a mail,
you will get a file created by python. You can use slstatus's module 'run_command' to show if a new mail has arrived.
Example for slstatus:
    { run_command, "%s   ", "cat /tmp/newmails/newmails" },
"""
sp.os.makedirs('/tmp/newmails', exist_ok=True)

def update(msgs_were):
    user = 'abdullah@abdullah.today'
    completed_process = sp.run(['gpg', '-dq', '/home/ak/.config/mutt/credentials/abdullah.gpg'], check=True, stdout=sp.PIPE, stderr=sp.PIPE, encoding='utf-8')
    password = completed_process.stdout[:-1]
    box = imaplib.IMAP4_SSL('imap.abdullah.today', 993)
    box.login(user, password)
    box.select()
    msgs = len(box.search(None, 'UnSeen')[1][0].split())
    if msgs > 0:
        print(msgs)
    else:
        print(0)

    if msgs_were < msgs and msgs > 0:
        sp.run(['mpv', '--no-video', '/home/ak/music/mailtune.aac'])
    if msgs > 0:
        with open('/tmp/newmails/newmails', 'w+') as f:
           f.write(str(msgs) + ' new mails arrived!') 
    elif msgs == 0:
        with open('/tmp/newmails/newmails', 'w+') as f:
            f.write('no mails!')

    return msgs

while True:
    try:
        if b'/usr/bin/pass\n' in password_store:
            msgs_were = update(msgs_were)
            time.sleep(10)
        else:
            print('error')
            time.sleep(2)
    except (socket.gaierror, ConnectionAbortedError, ConnectionError, ConnectionRefusedError, ConnectionResetError) as error:
        print('No Network')
        with open('/tmp/newmails/newmails', 'w+') as f:
            f.write('no network!')
        time.sleep(5)
