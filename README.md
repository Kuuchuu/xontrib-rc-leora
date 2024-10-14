[Run Control File](https://xon.sh/xonshrc.html). You should know about what RC files are used in interactive and non-interactive sessions.

### Install

    ```xonsh
    pip install -U git+https://github.com/kuuchuu/xontrib-rc-leora
    # pip install -U "git+https://github.com/kuuchuu/xontrib-rc-leora.git#egg=xontrib-rc-leora[xxh]" # Include xxh package 

    # Only for interactive mode:
    # (You can also create autoloadable xontrib using xontrib-template.)
    echo 'xontrib load rc_leora' >> ~/.xonshrc
    echo "aliases['cheatsheet'] = 'frogmouth gh anki-code/xonsh-cheatsheet'" >> ~/.xonshrc

    # For interactive or non-interactive (https://xon.sh/xonshrc.html):
    # mkdir -p ~/.config/xonsh/rc.d/
    # echo 'xontrib load rc_leora' > ~/.config/xonsh/rc.d/rc_leora.xsh

    xonsh
    ```

### See also
* [xonsh-cheatsheet](https://github.com/anki-code/xonsh-cheatsheet/blob/main/README.md) - cheat sheet for xonsh shell with copy-pastable examples.
* [xontrib-template](https://github.com/xonsh/xontrib-template) - Full-featured template for building extension (xontrib) for the xonsh shell.
