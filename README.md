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
    └─▪ pip install python-fasthtml fh_altair requests pandas

      Looking in indexes: https://pypi.org/simple, https://packagecloud.io/github/git-lfs/pypi/simple
      Collecting python-fasthtml
        Downloading python_fasthtml-0.10.3-py3-none-any.whl.metadata (6.5 kB)
      Collecting fh_altair
        Using cached fh_altair-0.1.0-py2.py3-none-any.whl.metadata (1.5 kB)
      Collecting requests
        Using cached requests-2.32.3-py3-none-any.whl.metadata (4.6 kB)
      Collecting pandas
        Using cached pandas-2.2.3-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (89 kB)
        ...

    [notice] A new release of pip is available: 24.2 -> 24.3.1
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
      Collecting setuptools
        Downloading setuptools-75.7.0-py3-none-any.whl.metadata (6.7 kB)
      Downloading setuptools-75.7.0-py3-none-any.whl (1.2 MB)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 4.5 MB/s eta 0:00:00
      Installing collected packages: setuptools
      Successfully installed setuptools-75.7.0

Source the virtual environment:

    ┌─[stav][legion][±][master ✓][~/.../FastHTML/crablox]
    └─▪ . venv/bin/activate

Explicit environment variables:

    $ export PORT=5001; export CRB=devel; python crablox/main.py

      Using "devel" environment for <fasthtml.live_reload.FastHTMLWithLiveReload object at 0x7f61c44c7d40>
      Link: http://localhost:5001
      INFO:     Will watch for changes in these directories: ['FastHTML/crablox']
      INFO:     Uvicorn running on http://0.0.0.0:5001 (Press CTRL+C to quit)
      INFO:     Started reloader process [1235952] using WatchFiles
      Using "devel" environment for <fasthtml.live_reload.FastHTMLWithLiveReload object at 0x7ff8def092b0>
      Using "devel" environment for <fasthtml.live_reload.FastHTMLWithLiveReload object at 0x7ff8afae18e0>
      INFO:     Started server process [1235969]
      INFO:     Waiting for application startup.
      INFO:     Application startup complete.

## Environments

### Development

    ┌─(venv)[stav][legion][±][master ↑3 {1} U:1 ?:1 ✗][~/.../FastHTML/crablox]
    └─▪ python --version
    Python 3.12.7

    ┌─(venv)[stav][legion][±][master ?:1 ✗][~/.../FastHTML/crablox]
    └─▪ CRB=devel python crablox/main.py

### Production

Copy `config.ini`.

    (venv) stav@bullet:.../services.pmx.mega/crablox$ python --version
    └─▪ Python 3.11.2

    (venv) stav@bullet:.../services.pmx.mega/crablox$
    └─▪ PORT=5001 python crablox/main.py

## Sites

* https://docs.fastht.ml/
* https://gallery.fastht.ml/
* https://mikelev.in/futureproof/unpacking-fasthtml-databases/
* https://github.com/AnswerDotAI/fasthtml-example
