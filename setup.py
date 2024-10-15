#!/usr/bin/env python
import setuptools
from setuptools.command.install import install
import os
import shutil

class PostInstallCommand(install):
    def run(self):
        install.run(self)

        user_bin = os.path.expanduser('~/.local/bin')
        user_home = os.path.expanduser('~')

        os.makedirs(user_bin, exist_ok=True)

        script_src = os.path.join('scripts', 'systemSummary.sh')
        script_dest = os.path.join(user_bin, 'systemSummary.sh')
        shutil.copy2(script_src, script_dest)
        print(f"Copied {script_src} to {script_dest}")

        xonshrc_src = os.path.join('scripts', '.xonshrc')
        xonshrc_dest = os.path.join(user_home, '.xonshrc')
        shutil.copy2(xonshrc_src, xonshrc_dest)
        print(f"Copied {xonshrc_src} to {xonshrc_dest}")

try:
    with open('README.md', 'r', encoding='utf-8') as fh:
        long_description = fh.read()
except (IOError, OSError):
    long_description = ''

setuptools.setup(
    name='xontrib-rc-leora',
    version='0.15.0.1',
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
