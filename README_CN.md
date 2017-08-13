# 项目依赖分析

## 快速开始

### 0x00

- 安装python（版本2.7.x） 和 bower
- cd到项目根目录
- 执行 `bower install`，安装所需要的js模块

### 0x01

- 在`analysis_dependencies.conf`文件中配置需要分析的项目信息，配置在`java_modules`节点下,格式为: 模块名称 = 模块路径,名称需要是唯一的

### 0x02

如果你是用macOS或者Linux,只需要执行`source generate_and_host.sh`即可。
如果不是，执行以下步骤：

- 执行 `python entrance_generate.py`,这个命令会在output路径下生成分析结果的json文件
- 执行 `python -m SimpleHTTPServer 8080`
- 浏览器打开 `http://localhost:8080/`即可

## Features

- Analysis Dependencies
- and so on...


