#!/usr/bin/env python
import setuptools
from setuptools.command.install import install
import os
import shutil
import stat
import subprocess

class PostInstallCommand(install):
    def run(self):
        install.run(self)

        self.install_system_packages()

        user_bin = os.path.expanduser('~/.local/bin')
        user_home = os.path.expanduser('~')

        os.makedirs(user_bin, exist_ok=True)

        script_src = os.path.join('scripts', 'systemSummary.sh')
        script_dest = os.path.join(user_bin, 'systemSummary.sh')
        shutil.copy2(script_src, script_dest)
        print(f"Copied {script_src} to {script_dest}")

        st = os.stat(script_dest)
        os.chmod(script_dest, st.st_mode | stat.S_IEXEC)
        print(f"Set executable flag on {script_dest}")

        xonshrc_src = os.path.join('scripts', '.xonshrc')
        xonshrc_dest = os.path.join(user_home, '.xonshrc')
        shutil.copy2(xonshrc_src, xonshrc_dest)
        print(f"Copied {xonshrc_src} to {xonshrc_dest}")

    def install_system_packages(self):
        distro_install_commands = {
            "solus": [
                "sudo eopkg install -y fzf onefetch zoxide starship"
            ],
            "ubuntu": [
                "sudo apt update && sudo apt install -y fzf onefetch zoxide starship"
            ],
            "debian": [
                "sudo apt update && sudo apt install -y fzf onefetch zoxide starship"
            ],
            "rocky": [
                "sudo dnf install -y fzf onefetch zoxide starship"
            ],
            "fedora": [
                "sudo dnf install -y fzf onefetch zoxide starship"
            ],
            "arch": [
                "sudo pacman -Syu --noconfirm fzf onefetch zoxide starship"
            ],
            "manjaro": [
                "sudo pacman -Syu --noconfirm fzf onefetch zoxide starship"
            ],
            "opensuse": [
                "sudo zypper refresh && sudo zypper install -y fzf onefetch zoxide starship"
            ],
            "gentoo": [
                "sudo emerge --ask app-shells/fzf app-shells/starship dev-vcs/onefetch sys-apps/zoxide"
            ],
            "alpine": [
                "sudo apk add fzf onefetch zoxide starship -y"
            ],
            "termux": [
                "pkg install fzf onefetch zoxide starship git -y && cd /tmp && git clone https://github.com/notflawffles/termux-nerd-installer.git && cd termux-nerd-installer && make install && termux-nerd-installer i mononoki && termux-nerd-installer set mononoki && cd ~"
            ],
        }

        distro = self.detect_linux_distro()

        if distro == None:
            return

        if distro in distro_install_commands:
            for command in distro_install_commands[distro]:
                self.run_shell_command(command)

        config_dir = os.path.expanduser("~/.config")
        os.makedirs(config_dir, exist_ok=True)
        # if not os.path.exists(config_dir):
        #     os.makedirs(config_dir)
        #     print(f"Created directory {config_dir}")
        self.run_shell_command("starship preset pastel-powerline -o ~/.config/starship.toml")
        self.run_shell_command("sed -i -e 's/#FCA17D/#cc99ff/g' ~/.config/starship.toml")

    def detect_linux_distro(self):
        # import distro # Does not work fully automated. distro must be pre-installed
        # distro_id = distro.id()

        # if distro_id is None and "TERMUX_VERSION" in os.environ:
        #     print("Detected Termux environment")
        #     return "termux"
        # if distro_id in ["ubuntu", "debian", "solus", "rocky", "fedora", "arch", "manjaro", "opensuse", "gentoo", "alpine"]:
        #     return distro_id
        # else:
        #     print(f"Unsupported Linux distribution: {distro_id}")
        #     return None
        try:
            with open("/etc/os-release") as f:
                os_release = f.read().lower()
                for distro_id in ["ubuntu", "debian", "solus", "rocky", "fedora", "arch", "manjaro", "opensuse", "gentoo", "alpine"]:
                    if distro_id in os_release:
                        return distro_id
        except FileNotFoundError:
            if "TERMUX_VERSION" in os.environ:
                print("Detected Termux environment")
                return "termux"
            pass

        return None

    def run_shell_command(self, command):
        try:
            print(f"Running: {command}")
            result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Error running command: {command}")
            print(f"stderr: {e.stderr}")

try:
    with open('README.md', 'r', encoding='utf-8') as fh:
        long_description = fh.read()
except (IOError, OSError):
    long_description = ''

setuptools.setup(
    name='xontrib-rc-leora',
    version='0.15.2.0',
    license='MIT',
    author='anki-code',
    author_email='no@no.no',
    description="Awesome snippets of code for xonshrc in xonsh shell.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.6',
    install_requires=[
        'xonsh[full]', # The awesome shell.
        'xontrib-spec-mod', # Library of xonsh subprocess specification modifiers e.g. `$(@json echo '{}')`.
        'xontrib-prompt-bar', # The bar prompt for xonsh shell with customizable sections and Starship support. 
        'xontrib-back2dir', # Return to the most recently used directory when starting the xonsh shell. 
        'xontrib-sh', # Paste and run commands from bash, zsh, fish, tcsh in xonsh shell. 
        'xontrib-pipeliner', # Let your pipe lines flow thru the Python code in xonsh. 
        'xontrib-output-search', # Get identifiers, names, paths, URLs and words from the previous command output and use them for the next command in xonsh. 
        'xontrib-argcomplete', # Argcomplete support to tab completion of python and xonsh scripts in xonsh shell. 
        'xontrib-cmd-durations', # Show long running commands durations in prompt with option to send notification when terminal is not focused. 
        'xontrib-jedi', # Jedi - an awesome autocompletion, static analysis and refactoring library for Python
        'xontrib-jump-to-dir', # Jump to used before directory by part of the path. Lightweight zero-dependency implementation of autojump or zoxide projects functionality. 
        'xontrib-clp', # Copy output to clipboard. URL: https://github.com/anki-code/xontrib-clp
        'xontrib-vox', # Python virtual environment manager for xonsh
        'xontrib-bashisms', # Bash-like interface extensions for xonsh
        # 'xontrib-fzf-completions', # Provides fzf completions into your xonsh shell
        'xontrib-gitinfo', # Displays git information on entering a repository folder
        # 'xontrib-history-encrypt', # Encrypts the commands history file to prevent leaking sensitive data
        'frogmouth', # Markdown viewer
        
        # Get more xontribs:
        #  * https://github.com/topics/xontrib
        #  * https://github.com/xonsh/awesome-xontribs
        #  * https://xon.sh/api/_autosummary/xontribs/xontrib.html

        'HyFetch',
    ],
    extras_require={
        "xxh": [
            "xxh-xxh" # Using xonsh wherever you go through the ssh.
        ],
    },
    packages=['xontrib'],
    package_dir={'xontrib': 'xontrib'},
    package_data={'xontrib': ['*.py', '*.xsh']},
    cmdclass={
        'install': PostInstallCommand,
    },
    platforms='any',
)
