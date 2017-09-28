import subprocess

def tmux_execute(session_name, command):

    proc = subprocess.Popen(['tmux', 'new-session', '-d', '-s', '{}'.format(session_name),\
     '{}'.format(command)], stdout=subprocess.PIPE)
    (out, err) = proc.communicate()
