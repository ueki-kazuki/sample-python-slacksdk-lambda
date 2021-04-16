# Abstract
This is a sample slack bot app written in Python.
You can deploy this app usign serverless framework.

## how to setup
1. Install python modules with Pipenv. And switch into the virtual environment.

```bash
$ pipenv install
$ pipenv shell
```

2. Install serverless framework at first. https://www.serverless.com/framework/docs/getting-started/
3. Install plugins.

```bash
$ sls plugin install -n serverless-wsgi
$ sls plugin install -n serverless-dotenv-plugin
$ sls plugin install -n serverless-python-requirements
```

4. Copy the Signing Secret and Event Token from your slack app configuration and save it in .env file.

## how to deploy
```bash
$ sls deploy
```
