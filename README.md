# Mail checker for DWM


** Installation

```
git clone https://gitlab.com/Abdullah/mailchecker ~/bin      # Create ~/bin directory if its not already there.
cd ~/bin/mailchecker  # change username and passwords for your account. I'm using gpg to store them 
cp mailchecker.py ~/bin/mailchecker
cd systemd # change username there too and path to where you stored the mailchecker script as well.
cp systemd/mailcheck.service ~/.config/systemd/user/
systemctl enable --user mailcheck.service
systemctl start --user mailcheck.service
```
