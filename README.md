# pipelines

Test the playbook

```
ansible-playbook -i hosts playbook.yaml
```

## web.sitemap script

### to search sitemap for the specified title and description in web.sitemap file

```
python3.7 sitemap.py ./uc01/Web.sitemap "directory22" "desc directory22"
```

or
```
./sitemap.py ./uc01/Web.sitemap "directory22" "desc directory22"
```

### to search domain and name in aspx file

pre-requisite
- pip3.6 install --upgrade pip 
- pip3.6 install BeautifulSoup4

```
python3.7 aspx.py ./uc01/StaffDirectory.aspx "Domain=d1" "domain 1"
```

### backup files and rename to specify filename_YYYYMMDD.ext format
it will make a copy of the file from source folder to backup folder and rename it.

```
python3.7 bkupfiles.py "./uc01/" "./uc01/backup/" "StaffDirectory.aspx,Web.sitemap"
```

### rollback files 
rollback files in source folder to destination folder where files with "_YYYYMMDD" are removed from filename based on today's date

```
python3.7 rollbkfiles.py "./uc01/backup/" "./uc01/rollback/" "StaffDirectory_20190409.aspx,Web_20190409.sitemap"
```

# Resource

- [python packaging](https://python-packaging.readthedocs.io/en/latest/minimal.html)
- [create ssh key](https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys-on-centos7) to remote server
- [Distributing a Python command line](https://gehrcke.de/2014/02/distributing-a-python-command-line-application/) application
- [pyfiglet](https://github.com/pwaller/pyfiglet)
- [termcolor](https://pypi.org/project/termcolor/)
- [colorama](https://pypi.org/project/colorama/)
- [six](https://pypi.org/project/six/)
- [pytest](https://docs.pytest.org/en/latest/)
- [pyconfigstore](https://pypi.org/project/pyconfig/)
- [Building Beautiful Command Line Interfaces](https://codeburst.io/building-beautiful-command-line-interfaces-with-python-26c7e1bb54df) with Python
- [Install Python](https://realpython.com/installing-python/)

## CLI tools
- [click](https://palletsprojects.com/p/click/)
- [cement](https://docs.builtoncement.com/)
- [Docopt](http://docopt.org/)
- [PyInquirer](https://github.com/CITGuru/PyInquirer)
  
## deploy python app to offline server (air-gap)

to do that, [package python project](https://www.digitalocean.com/community/tutorials/how-to-package-and-distribute-python-applications) as wheels, copy the wheels to server and execute pip install

```
pip2.7 wheel --wheel-dir=/project/whls/ package
```

```
cd /projects/whls/
pip install *
```

## Install python3 in CentOS

one [method](https://janikarhunen.fi/how-to-install-python-3-6-1-on-centos-7)

```
sudo yum update
sudo yum install yum-utils
sudo yum groupinstall development

sudo yum install https://centos7.iuscommunity.org/ius-release.rpm

sudo yum install python36u

sudo yum install python36u-pip
sudo yum install python36u-devel
```

### Creating a virtualenv

```
python3.6 -m venv venv
```

### activate it

```
. venv/bin/activate

pip install [package_name]
pip install -r requirements.txt
```

