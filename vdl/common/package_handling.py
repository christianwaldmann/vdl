import subprocess
import logging
import sys
import platform
import stdlib_list
import pkg_resources


"""
Collection of functions for package handling.

Most useful function:
- upgrade_import_all(): Upgraded alle importierten packages.
"""


class PackageManager:

    def __init__(self):
        self.logger = logging.getLogger(__file__)

    def UpgradeAllImportPackages(self, verbose=False):
        """
        Upgrade all imported packages.

        :return:
        """
        packages_imported = self.GetAllImportedPackages(exclude_standardlib=True)
        self.UpgradeMultiplePackages(packages_imported, verbose)

    def GetAllImportedPackages(self, exclude_standardlib=False):
        """
        Get all imported packages as list.

        :param exclude_standardlib: Flag for excluding standard modules
        :return: List of imported packages
        """
        # 1. Get python version (only major and minor, e.g. 3.7 not 3.7.4)
        python_version_tuple = platform.python_version_tuple()
        python_version_major_minor = python_version_tuple[0] + "." + python_version_tuple[1]

        # 2. Get list of all standard modules
        modules_standardlib = stdlib_list.stdlib_list(python_version_major_minor)
        modules_standardlib.append(
            "pkg_resources"
        )  # ist aus irgendeinem Grund nicht in der Liste

        # 3. Get list of all imported packages
        packages_imported = list(set(sys.modules) & set(globals()))

        # 4. Exclude standard packages from list if flag is set
        if exclude_standardlib:
            packages_imported_excluding_standardlib = []
            for pack in packages_imported:
                if pack not in modules_standardlib:
                    packages_imported_excluding_standardlib.append(pack)
            packages_imported = packages_imported_excluding_standardlib

        return packages_imported

    def UpgradeMultiplePackages(self, package_names, verbose=False):
        """
        Install and upgrade multiple pip packages.

        :param package_names: List of pip package names
        :param verbose: verbosity flag setting the loglevel to DEBUG if set to true
        :return:
        """
        if type(package_names) != list:
            raise ValueError("Parameter package_names must be a list.")
        for package_name in package_names:
            self.Upgrade(package_name, verbose)

    def Upgrade(self, package_name, verbose=False):
        """
        Install and upgrade a pip package.

        :param package_name: pip package name
        :param verbose: verbosity flag setting the loglevel to DEBUG if set to true
        :return:
        """
        # Change loglevel if verbosity flag is set
        if verbose:
            self.logger.setLevel(logging.DEBUG)

        # Try upgrading via pip
        try:
            command = "pip install --upgrade " + package_name
            self.logger.info('Execute command "' + command + '"')
            stdoutput = subprocess.check_output(command)
        except:
            try:
                # If couldnt be installed or upgraded, try again with slightly different package_name (all '_' replaced by '-')
                command = "pip install --upgrade " + package_name.replace("_", "-")
                self.logger.info('Execute command "' + command + '"')
                stdoutput = subprocess.check_output(command)
            except:
                # If couldnt be installed or upgraded, try again with slightly different package_name (all '_' replaced by '')
                command = "pip install --upgrade " + package_name.replace("_", "")
                self.logger.info('Execute command "' + command + '"')
                stdoutput = subprocess.check_output(command)

        stdoutput = stdoutput.decode("utf-8")

        # Log output
        self.logger.info(stdoutput)

    def GetInstalledVersionOfPackage(self, package_name):
        """
        Get installed version of pip package.

        :param package_name: pip package name
        :return: version of the pip package
        """
        return pkg_resources.get_distribution(package_name).version
