# requirements
pytube repository

# how to install it 
type `pip install pytube` in the terminal
# with git clone
or you can either clone the repository from github  `git clone git://github.com/pytube/pytube.git`
# download the tarball
`curl -OL https://github.com/pytube/pytube/tarball/master` (zipball on windows)

`cd pytube`

`python -m pip install`
# notification implementation (just linux)
if you are using any linux distro you can get a notification once the video is succesfully downloaded

` sudo apt-get install libnotify-dev ` install the required libraries

then open the code and uncomment (delete the # in front) line 2,12,13
# how to use it 
open the terminal, move to the directory where the script is located and run this command

`python3 main.py [link]`
