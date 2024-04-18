# Virtual Environment

## Why ?
* Dependency Management
* Project Isolation
* Consistency and Reproducibility
* Simplified Package Management
* Ease of Deployment:


## How ?
* [pyenv](https://gist.github.com/luzfcb/1a7f64adf5d12c2d357d0b4319fe9dcd) 

```shell
# DO NOT RUN THIS AS A ROOT USER
# Enter your password when prompted.
# your user must be allowed to run "sudo"
sudo bash -c "echo -e 'Starting...\n'"

sudo apt-get update;
# install most common python interpreter itself compile dependencies
sudo apt-get install aria2 build-essential curl git libbz2-dev libffi-dev liblzma-dev libncurses5-dev libncursesw5-dev libreadline-dev libsqlite3-dev libssl-dev llvm make tk-dev wget xz-utils zlib1g-dev --yes;

# install pyenv
curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash

# install a virtualenvwrapper plugin to pyenv
git clone https://github.com/pyenv/pyenv-virtualenvwrapper.git "${HOME}/.pyenv/plugins/pyenv-virtualenvwrapper"

# add pyenv required configurations on your .bashrc file
if ! grep -Eq "^[#]{4}[[:space:]]pyenv[[:space:]]config$" "${HOME}/.bashrc" ; then echo -e "\n\nsetup pyenv configuration:\nThe following content was inserted at the end of the ${HOME}/.bashrc file\n"; echo -e '\n#### pyenv config\nif [ -f "$HOME/.pyenv/bin/pyenv" ] && ! type -P pyenv &>/dev/null ; then\n  export PYTHON_CONFIGURE_OPTS="--enable-shared"\n  export PYTHON_CFLAGS="-O2"\n  export PYTHON_BUILD_ARIA2_OPTS="-x 10 -k 1M"\n  export PYENV_ROOT="${HOME}/.pyenv"\n  export PATH="${PYENV_ROOT}/bin:${PATH}"\n  eval "$(pyenv init --path)"\n  eval "$(pyenv init -)"\n  eval "$(pyenv virtualenv-init -)"\n  if [[ ! "$(pyenv which python)" == "/usr/bin/python" ]] ; then \n    pyenv virtualenvwrapper_lazy;\n  fi\nfi\n#### pyenv config end' | tee --append "${HOME}/.bashrc"; source "${HOME}/.bashrc"; else  echo -e "\n\npyenv configuration already installed in ${HOME}/.bashrc"; fi


# reload .bashrc to run pyenv configurations
source "${HOME}/.bashrc"
```

* [Conda](https://pythonforundergradengineers.com/new-virtual-environment-with-conda.html)

* lib poetry ?