# pipelines

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

```
python3.7 aspx.py ./uc01/StaffDirectory.aspx "Domain=d1" "domain 1"
```

### backup files and rename to specify filename_YYYYMMDD.ext format
it will make a copy of the file from source folder to backup folder and rename it.

```
python3.7 bkupfiles.py "./uc01/" "./uc01/backup/" "StaffDirectory.aspx,Web.sitemap"
```

# Resource

- [create ssh key](https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys-on-centos7) to remote server
- [Distributing a Python command line](https://gehrcke.de/2014/02/distributing-a-python-command-line-application/) application

## deploy python app to offline server (air-gap)

to do that, [package python project](https://www.digitalocean.com/community/tutorials/how-to-package-and-distribute-python-applications) as wheels, copy the wheels to server and execute pip install

```
pip2.7 wheel --wheel-dir=/project/whls/ package
```

```
cd /projects/whls/
pip install *
```