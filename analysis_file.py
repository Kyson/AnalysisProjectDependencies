# -*-coding:utf-8-*-


def analysis_java(file_path):
    kw_package = "package"
    kw_import = "import"
    package = ""
    imports = []
    with open(file_path, 'r') as f:
        for line in f.readlines():
            line_format = str(line).strip()
            if line_format.startswith(kw_package):
                warn_line_end(file_path, line_format)
                package = line_format.lstrip(kw_package).strip("; ")
            if line_format.startswith(kw_import):
                warn_line_end(file_path, line_format)
                imports.append(line_format.lstrip(kw_import).strip("; "))
    return package, imports


def warn_line_end(file_path, line):
    if not line.endswith(";"):
        print "warning!!! [%s]:[%s] does not end with [;]", file_path, line


if __name__ == "__main__":
    package, imports = analysis_java("test/test.java")
    print package, imports
