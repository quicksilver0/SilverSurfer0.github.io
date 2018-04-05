silversurfer0.github.io

Steps from the article:
https://www.dataquest.io/blog/how-to-setup-a-data-science-blog/
extra resources:
http://docs.getpelican.com/en/3.6.3/tips.html#publishing-to-github
https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/

cmd in E:\jupyter-blog
workon jupyter-blog  //turns on vertualenv

git remote add origin git@github.com:SilverSurfer0/SilverSurfer0.github.io.git  //adds "origin" variable

//publishing:
pelican content -o output -t "E:\Pelican\pelican-themes\voidy-bootstrap" -s publishconf.py   //prepares for publishing (i.e. primes config for usage)
ghp-import output -b master
git push origin master

//run on localhost
pelican content 
cd output
pelican -m pelican.server