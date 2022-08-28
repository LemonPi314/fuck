try:
    import msvcrt
except ImportError:
    import sys
    import tty
    import termios
    windows = False
finally:
    windows = True


def getch() -> str:
    if windows:
        return msvcrt.getwche()
    else:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
