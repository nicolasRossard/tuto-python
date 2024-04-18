# Tuto to start Python project

# Summary
* Think before to do
* Prepare your environment
* Example of projects
* Plugins, libs and links interesting 


# Ask yourself the appropriate questions :mortar_board:
- [ ] Which Python version should I use ?
- [ ] What kind of project, I will do ? (POC, Data analysis, API ?)
- [ ] How I will work for my project and which tools I should use
- [ ] Which libraries I will use ? 


# Start your project

- [ ] Prepare your repo [GIT](docs/Git.md)
- [ ] Install your IDE (Pycharm, VSCode, Sublime etc.)
- [ ] Create your [Python Environment](docs/Virtual_environment.md) (Conda, pyenv etc.)
- [ ] Start your project :fire:

# Plugins, libs or links interesting
## Plugins
* Sonarlint https://www.sonarsource.com/products/sonarlint/
* Mypy https://plugins.jetbrains.com/plugin/11086-mypy

## Libraries
* flake8 (inform) :star: :star: :star:
* black (automatic)


# Examples
- [ ] Use notebook -> [fake_notebook/](fake_notebook/README.md)
- [ ] Use IDE Pycharm -> [fake_project/](fake_project/README.md)

## Start only one project
On this repo you have two use cases :
* A notebook
* An application with gradio

To start properly and save into your git
* Git clone repo
* Go to the directory (_fake\_{name}/_) of the project you want to do
* Make commands to init [git](docs/Git.md) (check image second part)
* Open your IDE and go to your directory (_fake\_{name}/_) 
* Create your virtual environment and implement into your IDE
* Install requirements


## Links
* Good practices : [PEP 8](https://peps.python.org/pep-0008/) / typing / docstrings
* Python Lessons with [Openclassroom](https://openclassrooms.com/fr/courses/7168871-apprenez-les-bases-du-langage-python)
* Data [Kaggle](https://www.kaggle.com/)


## Useful Python commands

* Checking version
```shell
python --version 
```

* Install libraries
```shell
pip install {lib_name}=={lib_version} 
```

```shell
pip install -r requirements.txt
```


* Check all libs
```shell
pip freeze
```

* Uninstall all libs
```shell
pip uninstall -y -r <(pip freeze)
```

# Machine learning libraries

* [scikit-learn](https://pypi.org/project/scikit-learn/)
* [transformers](https://pypi.org/project/transformers/) [HuggingFace](https://huggingface.co/spaces)