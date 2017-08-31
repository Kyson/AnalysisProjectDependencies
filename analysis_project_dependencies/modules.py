# -*-coding:utf-8-*-
import ConfigParser
import json

from analysis_project_dependencies.analysis_module import analysis_javas


class MFile():
    def __init__(self, local_path):
        self.local_path = local_path

    def get_local_path(self):
        return self.local_path


class JavaMFile(MFile):
    def __init__(self, path, package, clz_name, imports):
        MFile.__init__(self, path)
        self.package = package
        self.clz_name = clz_name
        self.imports = imports

    def get_clz_name(self):
        return self.clz_name

    def get_pkg(self):
        return self.package

    def get_imports(self):
        return self.imports

    def __repr__(self):
        return "%s : %s (%s)" % (self.package, self.clz_name, self.imports)


class Module():
    def __init__(self, name, local_path):
        self.name = name
        self.local_path = local_path

    def get_name(self):
        return self.name

    def get_local_path(self):
        return self.local_path


class Dependency():
    def __init__(self):
        self.dependencies = []

    def append_dependencies(self, java_module):
        self.dependencies.append(java_module)

    def set_dependencies(self, java_modules):
        self.dependencies = java_modules


class JavaRootModule(Module):
    def __init__(self, name, local_path):
        Module.__init__(self, name, local_path)


class JavaModule(Module, Dependency):
    def __init__(self, name, local_path):
        Module.__init__(self, name, local_path)
        Dependency.__init__(self)
        self.java_mfiles = []

    def analysis_self(self):
        self.java_mfiles = []
        print "\n[%s] analysis_self begin >>>>>>\n" % str(self.name)
        for path, package, class_name, imports in analysis_javas(self.local_path):
            print "file path:%s" % path
            print "    class:%s.%s" % (package, class_name)
            print "  imports:%s" % imports
            self.java_mfiles.append(JavaMFile(path, package, class_name, imports))
        print "\n<<<<<< [%s] analysis_self end\n" % str(self.name)

    def get_java_mfiles(self):
        return self.java_mfiles

    def analysis_dependency(self, java_modules):
        print "\n[%s] analysis_dependency begin >>>>>>\n" % str(self.name)
        self.set_dependencies([])
        for java_module in java_modules:
            for mfile in java_module.get_java_mfiles():
                result, current_mfile = JavaModule.mfile_include_pkg(self.java_mfiles, mfile.get_pkg(),
                                                                     mfile.get_clz_name())
                if result:
                    self.append_dependencies(java_module)
                    print "File [%s.%s] is dependent on file [%s.%s] of module [%s]" % (
                        current_mfile.get_pkg(), current_mfile.get_clz_name(), mfile.get_pkg(), mfile.get_clz_name(),
                        java_module.get_name())
                    break
        print "\n<<<<<< [%s] analysis_dependency end\n" % str(self.name)

    @staticmethod
    def mfile_include_pkg(java_mfiles, pkg, java_clz):
        for mfile in java_mfiles:
            if mfile.get_imports().__contains__(pkg + "." + java_clz):
                return True, mfile
        return False, None

    def __repr__(self):
        return json.dumps(self.to_dict())

    def to_dict(self):
        dependency_repr = []
        for java_module in self.dependencies:
            dependency_repr.append(java_module.get_name())

        mfiles_repr = []
        for mfile in self.java_mfiles:
            mfiles_repr.append(mfile.get_pkg() + "." + mfile.get_clz_name())
        return {
            "name": self.name,
            "path": self.local_path,
            "includes": mfiles_repr,
            "dependencies": dependency_repr
        }

    def to_simple_dict(self):
        dependency_repr = []
        for java_module in self.dependencies:
            dependency_repr.append(java_module.get_name())
        return {
            "name": self.name,
            "path": self.local_path,
            "dependencies": dependency_repr
        }


def java_analysis():
    cp = ConfigParser.SafeConfigParser()
    cp.read('analysis_dependencies.conf')
    java_module_pairs = cp.items("java_modules")
    java_modules = []
    for modules_config_pair in java_module_pairs:
        java_modules.append(JavaModule(modules_config_pair[0], modules_config_pair[1]))

    for java in java_modules:
        java.analysis_self()

    for index, java in enumerate(java_modules):
        m = java_modules[:index]
        m.extend(java_modules[index + 1:])
        java.analysis_dependency(m)

    print "\n\nAnalysis Result >>>>>>"
    for java in java_modules:
        print java
    return java_modules


def java_output(java_modules):
    output = []
    for j_m in java_modules:
        output.append(j_m.to_simple_dict())
    with open('../output/module_dependencies_repr.json', 'w') as json_file:
        json_file.write(json.dumps(output))


if __name__ == "__main__":
    java_output(java_analysis())
