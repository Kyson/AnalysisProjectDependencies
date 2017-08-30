# -*-coding:utf-8-*-
import javalang


# JAVA_LEGAL_LETTER = []
#
# for i in range(32, 126):
#     if i == 32 or i == 35 or i == 36 or i == 96:
#         continue
#     JAVA_LEGAL_LETTER.append(chr(i))

# print JAVA_LEGAL_LETTER

def analysis_java(file_path):
    # kw_package = "package"
    # kw_import = "import"
    # kw_comment = ["/", "*"]
    java_package = ""
    java_imports = []
    with open(file_path, 'r') as f:
        tree = javalang.parse.parse(f.read())
        java_package = tree.package.name
        for im in tree.imports:
            java_imports.append(im.path)
            # print im.path
            # print tree
            # for line in f.readlines():
            #     line_format = str(line).strip()
            #     if line_format.startswith(kw_package):
            #         warn_line_end(file_path, line_format)
            #         package = line_format.lstrip(kw_package).strip("; ")
            #     if line_format.startswith(kw_import):
            #         warn_line_end(file_path, line_format)
            #         imports.append(line_format.lstrip(kw_import).strip("; "))
    return java_package, java_imports


# def warn_line_end(file_path, line):
#     if not line.endswith(";"):
#         print "warning!!! [%s]:[%s] does not end with [;]", file_path, line


if __name__ == "__main__":
    package, imports = analysis_java("test/test.java")
    print package, imports
