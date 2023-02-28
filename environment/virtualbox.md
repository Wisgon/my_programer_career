1. When installed virtualbox in ubuntu, I want to use virtualbox to run a windows10 OS. But when I created a new virtual mechine and import my windows10 iso image downloaded before and press "start" button, there was an error rise up: "blablabla modprobe vboxdrv". It tells me that I should excute command `sudo modprobe vboxdrv` to fix this. Then I opened a terminal and excuted it. But, another error rise up: `modprobe: ERROR: could not insert 'vboxdrv': Operation not permitted`. Then I found the way to fix it by internet search. The solution is:
   ```shell
    sudo apt-get update 
    sudo apt-get upgrade
    sudo apt-get install --reinstall virtualbox-dkms
   ```
   When reinstalling it, it will ask you to enter a password, then enter a password and remember it. It may rise a reboot fail error at the end of the installation, don't worry, let's manually restart our mechine.
   When rebootting, there was a little blue frame comes with three choices: first one is "reboot", do not choose it, the second one is "enroll MOK", that's it, choose it,then you will see a password entering input frame, input the password you set in the previous step, then press enter, and select reboot.
   After reboot, excute the command `sudo modprobe vboxdrv` once again, then the problem solved.
