# -*-coding:utf-8-*-
import fnmatch
import os

from analysis_file import analysis_java


def analysis_all_files(module_root, patterns=None, match_include_folder=False):
    """
    analysis module file
    :param module_root: 
    :param patterns: 
    :param match_include_folder: match dir
    :return: 
    """
    if patterns is None:
        patterns = ["*"]
    for path, subdirs, files in os.walk(module_root):
        if match_include_folder:
            files.extend(subdirs)
        files.sort()
        for name in files:
            for pattern in patterns:
                if fnmatch.fnmatch(name, pattern):
                    yield os.path.join(path, name), name
                    break


def analysis_javas(module_root):
    for path, name in analysis_all_files(module_root, patterns=["*.java"]):
        package, imports = analysis_java(path)
        class_name = os.path.splitext(name)[0]
        yield path, package, class_name, imports
        # print "%s: [%s] , [%s] , [%s]" % (path.rjust(50), package, class_name, imports)


if __name__ == "__main__":
    analysis_javas("test")
