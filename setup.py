from setuptools import setup
import sys

if __name__ == "__main__":

    # check python version
    min_python_version = (3, 8, 0)  # (major,minor,micro)
    python_version = sys.version_info
    print("Running Python version %s.%s.%s" % python_version[:3])
    if python_version < min_python_version:
        sys.exit(
            "Python < %s.%s.%s is not supported, aborting setup" % min_python_version[:3]
        )
    else:
        print("Confirmed Python version %s.%s.%s or above" % min_python_version[:3])

    setup()