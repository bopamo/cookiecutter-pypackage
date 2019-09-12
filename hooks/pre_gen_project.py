import re
import sys

PRETTY_HEADER = "*****************************"
PRE_GEN_HOOK_MESSAGE = PRETTY_HEADER + " PRE GEN HOOK RUNNING " + PRETTY_HEADER


def test_module_name():
    MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

    module_name = "{{ cookiecutter.project_slug}}"

    if not re.match(MODULE_REGEX, module_name):
        print(
            "ERROR: The project slug (%s) is not a valid Python module name. Please do not use a - and use _ instead" % module_name)

        # Exit to cancel project
        sys.exit(1)


def test_village_name():
    village_name = "{{ cookiecutter.village_name}}"

    assert village_name == "Koluama 2"


def run_pre_gen_project_hooks():
    print(PRE_GEN_HOOK_MESSAGE)

    test_module_name()
    test_village_name()


if __name__ == '__main__':
    run_pre_gen_project_hooks()
