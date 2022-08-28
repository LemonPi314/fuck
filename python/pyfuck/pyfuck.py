from collections import defaultdict

from .utils import getch


class Brainfuck:
    def __init__(self):
        """A Brainfuck interpreter."""
        self.data = defaultdict(lambda: 0)
        self.data_pointer = 0
        self.instruction_pointer = 0

    def run(self, code: str):
        """Execute Brainfuck code.

        Args:
            code (str): Brainfuck code.
        """
        code = ''.join(c for c in code if c in '<>+-.,[]')  # faster filter smth?
        code_length = len(code)
        brackets = self.parse_brackets(code)
        while self.instruction_pointer < code_length:
            match code[self.instruction_pointer]:
                case '>':
                    self.data_pointer += 1
                case '<':
                    self.data_pointer -= 1
                case '+':
                    self.data[self.data_pointer] = self._wrap(self.data[self.data_pointer] + 1, 0, 255)
                case '-':
                    self.data[self.data_pointer] = self._wrap(self.data[self.data_pointer] - 1, 0, 255)
                case '.':
                    print(chr(self.data[self.data_pointer]), end='', flush=True)
                case ',':
                    self.data[self.data_pointer] = ord(getch())
                case '[':
                    if not self.data[self.data_pointer]:
                        self.instruction_pointer = brackets[self.instruction_pointer]
                case ']':
                    if self.data[self.data_pointer]:
                        self.instruction_pointer = brackets[self.instruction_pointer]
            self.instruction_pointer += 1

    def _wrap(self, value: int, min: int, max: int) -> int:
        """Constrain a value between a minimum and maximum such that overflow and underflow wraps around.

        Args:
            value (int): The value to constrain.
            min (int): The minimum value.
            max (int): The maximum value.

        Returns:
            int: The constrained value.
        """
        if value < min:
            return max
        elif value > max:
            return min
        else:
            return value

    def parse_brackets(self, code: str) -> dict[int, int]:
        """Match bracket indices to their matching indices.

        Args:
            code (str): The code to parse.

        Returns:
            dict[int, int]: A dictionary mapping bracket indices to their matching indices.
        """
        bracket_stack = []
        brackets = {}
        for i in range(len(code)):
            if code[i] == '[':
                bracket_stack.append(i)
            elif code[i] == ']':
                j = bracket_stack.pop()
                brackets[j] = i
                brackets[i] = j
        return brackets
