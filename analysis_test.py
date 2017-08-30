# -*-coding:utf-8-*-

# 获取每行的首字母
from analysis_module import analysis_all_files


def analysis_letter(file_path):
    first_letters = []
    last_letters = []
    with open(file_path, 'r') as f:
        for line in f.readlines():
            line_format = str(line).strip()
            first_letters.append(line_format[:1])
            last_letters.append(line_format[-1:])
    return first_letters, last_letters


def letters(module_root):
    first_letter_all = []
    last_letter_all = []
    for path, name in analysis_all_files(module_root, patterns=["*.java"]):
        first_letters, last_letters = analysis_letter(path)
        print "File:%s , First Letter:%s , Last Letter:%s" % (path, first_letters, last_letters)
        first_letter_all.extend(first_letters)
        last_letter_all.extend(last_letters)

    return set(first_letter_all), set(last_letter_all)


def parseJavaFile():
    with open("ProjectForAnalysis/main/java/cn/hikyson/projectforanalysis/business/fight/FlightBookActivity.java", 'r') as f:
        fileStr = f.read()
        import javalang
        tree = javalang.parse.parse(fileStr)
        print tree.package.name
        for im in tree.imports:
            print im.path
        print tree



if __name__ == "__main__":
    # first_letter_all, last_letter_all = letters("/Users/kysonchao/AndroidStudioProjects/ctripen2")
    # print "First Letter:%s\nLast Letter:%s" % (first_letter_all, last_letter_all)
    parseJavaFile()
