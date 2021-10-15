
### Deploy Easy Way:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/lawleitekken/gofls)

### Deploy Hard Way: 

Create **config.py** with variables as given below (Refer sample.config):

```
class Config(object):
    TG_BOT_TOKEN = "134448596:AAEIyo3EBVCN3qdd3TfrmQUxoI-eZVGvmI"
    APP_ID = int(123635)
    API_HASH = "1a417dd4fdf3ead2819ff35641daa16b"
    TG_USER_SESSION = "BQDGRUC0_qw2GVQ2gpLFaXOt0mrWg16cBZPATQvR8KThDzi-NRE1I9DB......"
    CHANNELS = [-10012233245, -100883635533]
    AUTH_USERS = [1134455567, 9244566948]
    
# ------------- Optional ------------- #
    GROUP_U_NAME = "@my_group_name"

```
Run the following:

```
virtualenv -p python3 venv
. ./venv/bin/activate
pip3 install -r requirements.txt
python3 main.py
```
