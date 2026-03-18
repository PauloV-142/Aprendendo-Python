import termios
import tty
import sys

def get_input() -> str:
    filedescriptors = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin)
    key = sys.stdin.read(1)[0]
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN,filedescriptors)
    
    return key

if __name__ == "__main__":
    inputs = []
    for i in range(1, 6):
        inputs.append(get_input())
        print(i, flush=True, end=" ")
    print("\nend:", inputs)