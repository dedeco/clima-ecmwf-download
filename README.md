
Just a script 

## Create a virtualenv
```console
$ cd ~/envs/
$ pip3 install virtualenv 
$ virtualenv -p python3 climaecwfenv
$ source ~/envs/climaecwfenv/bin/activate
```
_This commands above are for linux and macOsx_

## Create an api key

### Install ECMWF KEY

- Login into https://apps.ecmwf.int/auth/login/ using the provided username and password.

- Retrieve your key at https://api.ecmwf.int/v1/key/

 - Note that the key expires in 1 year. You will receive an email to the registered email address 1 month before the expiration date with the renewal instructions.

- Copy the information in this page and paste it in the file $HOME/.ecmwfapirc You will get something similar to
    ```
    $HOME/.ecmwfapirc
    {
        "url"   : "https://api.ecmwf.int/v1",
        "key"   : "XXXXXXXXXXXXXXXXXXXXXX",
        "email" : "john.smith@example.com"
    }
    ```
## Install and run script
```console
(climaecwfenv) $ cd ~/projects
(climaecwfenv) $ git clone https://github.com/dedeco/clima-ecmwf-download.git
(climaecwfenv) $ pip install https://software.ecmwf.int/wiki/download/attachments/56664858/ecmwf-api-client-python.tgz
(climaecwfenv) $ ptyhon request_files.py
```

