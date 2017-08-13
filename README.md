# AnalysisProjectDependencies

## QuickStart

### 0x00

- install python 2.7.x  and install bower.
- `cd AnalysisProjectDependencies`.
- run `bower install`

### 0x01

- Configure the module in the `analysis_dependencies.conf` file,under section `java_modules`,format: name = module path,name must be unique.

### 0x02

if macOS or linux,just run `source generate_and_host.sh`
for other os,follow these steps:

- run `python entrance_generate.py`,it will generate json file in output dir.
- run `python -m SimpleHTTPServer 8080`.
- open `http://localhost:8080/` in browser.

## Features

- Analysis Dependencies
- and so on...



