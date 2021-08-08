#install acpitool on the nodes
#modify it on the result of the raspberry's

import subprocess
output1 = subprocess.check_output(["acpi"])
battery=output1.decode('utf-8')
remaining =battery.split('Battery 1:')[1].split('Discharging')[1].split('%')[0].split(',')[1].split(' ')[1] //split the words to what you need
int(remaining)