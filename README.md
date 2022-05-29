# Moodless Cry
It is a script designed to make brute force attacks on Moodle platforms, where the attacker is allowed to make requests for the authentication of a user through a tor circuit, largely guaranteeing their anonymity.

The use of this tool is as simple as assigning a user and a text document with possible passwords, this file of possible passwords could be generated with another program called ***[CUUP](https://github.com/Mebus/cupp "CUUP")***.

## Requirements
***The requirements are in the file [requirements.txt](requirements.txt)***
```bash
sudo pip3 install -r requirements.txt
```
```bash
sudo apt install tor -y
sudo systemctl start tor && service tor status
```
## Quick Start
```bash
python3 moodless-cry.py
```
## Example (Fast forwarded)
<img src="screenshots/gotit.gif" width="500" height="700">

## License
This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA

See './LICENSE' for more information.
