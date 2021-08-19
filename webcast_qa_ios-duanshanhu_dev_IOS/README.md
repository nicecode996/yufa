# Quick Start

## Install your app

### Repack your app

refer [shoots-ios Reapck app](https://code.byted.org/automation/shoots-ios#2%E9%87%8D%E6%89%93%E5%8C%85app)

### Install repacked app

```shell
idb install --udid <udid> <repacked-ipa>
``` 

## Running case under the command line

cd to your project root and execute:

```shell
cd /path/to/your/project
pip install -r requirements.txt
python manage.py runtest douyintest.demo
```

## Editing case under IDE

cd to your project root and install requirements for project:

```shell
cd /path/to/your/project
pip install -r requirements.txt
```

Import your project to IDE and the IDE will create the corresponding files.

Here, you can edit case under IDE now and commit your testcases to repository.

## Reference

Docs of shoots-ios: https://code.byted.org/automation/shoots-ios.git

