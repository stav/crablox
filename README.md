# README

## Install

### Clone

    ┌─[stav][legion][~/.../Python/FastHTML]
    └─▪ git clone git@github.com:stav/crablox.git

      Cloning into 'crablox'...
      remote: Enumerating objects: 4, done.
      remote: Counting objects: 100% (4/4), done.
      remote: Compressing objects: 100% (4/4), done.
      remote: Total 4 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
      Receiving objects: 100% (4/4), done.

### Virtual Environment

    ┌─[stav][legion][±][master ✓][~/.../FastHTML/crablox]
    └─▪ python  -m venv venv

    ┌─[stav][legion][±][master ✓][~/.../FastHTML/crablox]
    └─▪ . venv/bin/activate

### Dependencies

    ┌─(venv)[stav][legion][±][master ✓][~/.../FastHTML/crablox]
    └─▪ pip install python-fasthtml fh_altair requests pandas fa6-icons

      Looking in indexes: https://pypi.org/simple, https://packagecloud.io/github/git-lfs/pypi/simple
      Collecting python-fasthtml
        Downloading python_fasthtml-0.12.1-py3-none-any.whl.metadata (8.8 kB)
      Collecting fh_altair
        Using cached fh_altair-0.1.0-py2.py3-none-any.whl.metadata (1.5 kB)
      Collecting requests
        Using cached requests-2.32.3-py3-none-any.whl.metadata (4.6 kB)
      Collecting pandas
        Downloading pandas-2.2.3-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (89 kB)
        ...

    [notice] A new release of pip is available: 24.3.1 -> 25.0.1
    [notice] To update, run: pip install --upgrade pip

### Upgrade Pip

    ┌─(venv)[stav][legion][±][master ✓][~/.../FastHTML/crablox]
    └─▪ pip install --upgrade pip

      Looking in indexes: https://pypi.org/simple, https://packagecloud.io/github/git-lfs/pypi/simple
      Requirement already satisfied: pip in ./venv/lib/python3.12/site-packages (24.2)
      Collecting pip
        Using cached pip-24.3.1-py3-none-any.whl.metadata (3.7 kB)
      Using cached pip-24.3.1-py3-none-any.whl (1.8 MB)
      Installing collected packages: pip
        Attempting uninstall: pip
          Found existing installation: pip 24.2
          Uninstalling pip-24.2:
            Successfully uninstalled pip-24.2
      Successfully installed pip-24.3.1

### Structure

    ┌─(venv)[stav][legion][±][master ✓][~/.../FastHTML/crablox]
    └─▪ ls -lA

      drwxr-xr-x 2 stav stav  4096 Dec 29 17:11 crablox/
      drwxr-xr-x 9 stav stav  4096 Dec 29 17:15 .git/
      -rw-r--r-- 1 stav stav  3415 Dec 29 15:39 .gitignore
      -rw-r--r-- 1 stav stav  1211 Dec 29 15:39 LICENSE
      -rw-r--r-- 1 stav stav 12790 Dec 29 17:13 README
      -rw-r--r-- 1 stav stav   820 Dec 29 17:13 requirements.txt
      drwxr-xr-x 5 stav stav  4096 Dec 29 15:44 venv/
      drwxr-xr-x 2 stav stav  4096 Dec 29 17:13 .vscode/

## Development

Development environment is on Python version 3.12 which removed setuptools.

    ┌─(venv)[stav][legion][±][re-binding {1} U:1 ✗][~/.../FastHTML/crablox]
    └─▪ pip install pipupgrade setuptools

      Looking in indexes: https://pypi.org/simple, https://packagecloud.io/github/git-lfs/pypi/simple
      Collecting pipupgrade
        Using cached pipupgrade-1.12.0-py3-none-any.whl.metadata (11 kB)
      Collecting setuptools
        Downloading setuptools-75.8.1-py3-none-any.whl.metadata (6.7 kB)
      Requirement already satisfied: pip in ./venv/lib/python3.13/site-packages (from pipupgrade) (25.0.1)
      Collecting bpyutils (from pipupgrade)
        Using cached bpyutils-0.5.8-py3-none-any.whl.metadata (4.5 kB)
      Using cached pipupgrade-1.12.0-py3-none-any.whl (34 kB)
      Downloading setuptools-75.8.1-py3-none-any.whl (1.2 MB)

Source the virtual environment:

    ┌─[stav][legion][±][master ✓][~/.../FastHTML/crablox]
    └─▪ . venv/bin/activate

Explicit environment variables:

    ┌─(venv)[stav][legion][±][trunk {1} U:3 ✗][~/.../FastHTML/crablox]
    └─▪ export PORT=5001; export CRB=devel; python crablox/main.py

      Using "devel" environment for <fasthtml.live_reload.FastHTMLWithLiveReload object at 0x7f9dba9e5010>
      Link: http://localhost:5001
      INFO:     Will watch for changes in these directories: ['/home/stav/Work/Python/FastHTML/crablox']
      INFO:     Uvicorn running on http://0.0.0.0:5001 (Press CTRL+C to quit)
      INFO:     Started reloader process [12207] using WatchFiles
      Using "devel" environment for <fasthtml.live_reload.FastHTMLWithLiveReload object at 0x7f1bc6765550>
      Using "devel" environment for <fasthtml.live_reload.FastHTMLWithLiveReload object at 0x7f1bc5d0d590>
      INFO:     Started server process [12224]
      INFO:     Waiting for application startup.
      INFO:     Application startup complete.

## Environments

### Development

    ┌─(venv)[stav][legion][±][trunk {1} U:3 ✗][~/.../FastHTML/crablox]
    └─▪ python --version

      Python 3.13.1

    ┌─(venv)[stav][legion][±][master ?:1 ✗][~/.../FastHTML/crablox]
    └─▪ CRB=devel python crablox/main.py

### Production

Copy `config.ini`.

    [CMC]
    API_KEY = 136991d4-...
    [SPEECHIFY]
    API_KEY = zBgl5nYL3T6DHa-...
    [DEFAULT]
    AUTH_USERNAME = ...

Check Python version.

    (venv) stav@bullet:.../services.pmx.mega/crablox$ python --version

      Python 3.11.2

Start the server.

    (venv) stav@bullet:.../services.pmx.mega/crablox$ PORT=5001 python crablox/main.py

## Sites

* https://docs.fastht.ml/
* https://gallery.fastht.ml/
* https://mikelev.in/futureproof/unpacking-fasthtml-databases/
* https://github.com/AnswerDotAI/fasthtml-example
