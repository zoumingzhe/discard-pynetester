依以下步骤发布到PyPI（https://pypi.org）：
1 、修改好源代码文件
2 、修改文件“.\pynetester\__init__.py”（如有新增源代码文件）
3 、修改文件“.\setup.py”中的版本号
4 、检查是否安装twine、wheel模块（python -m pip list）
    如果未安装，请依次执行以下命令：
    >>>python -m pip install --upgrade pip
    >>>python -m pip install twine
    >>>python -m pip install wheel
5 、依次执行以下脚本文件：
    .\Step1.打包.bat
    .\Step2.上传.bat
6 、安装pynetester模块
    >>>python -m pip install pynetester
    >>>python -m pip list
7 、升级pynetester模块
    >>>python -m pip install --upgrade pynetester
    >>>python -m pip list
8 、卸载pynetester模块
    >>>python -m pip uninstall pynetester
    >>>python -m pip list
9 、删除以下目录文件：
    .\build
    .\dist
    .\pynetester.egg-info