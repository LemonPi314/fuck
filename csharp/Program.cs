namespace Sharpfuck
{
    public class Program
    {
        static void Main(string[] args)
        {
            if (args.Length < 1)
            {
                throw new ArgumentException("not enough arguments");
            }
            string code = System.IO.File.ReadAllText(args[0]);
            Run(code);
        }

        static void Run(string code)
        {
            Dictionary<int, int> brackets = ParseBrackets(ref code);
            Dictionary<uint, byte> memory = new();
            uint memoryPointer = 0;
            int instructionPointer = 0;
            int codeLength = code.Length;
            byte value;
            while (instructionPointer < codeLength)
            {
                switch (code[instructionPointer])
                {
                    case '>':
                        memoryPointer++;
                        break;
                    case '<':
                        memoryPointer--;
                        break;
                    case '+':
                        value = memory.Get(memoryPointer);
                        value++;
                        memory[memoryPointer] = value;
                        break;
                    case '-':
                        value = memory.Get(memoryPointer);
                        value--;
                        memory[memoryPointer] = value;
                        break;
                    case '.':
                        Console.Write((char)memory.Get(memoryPointer));
                        break;
                    case ',':
                        memory[memoryPointer] = (byte)Console.Read();
                        break;
                    case '[':
                        if (memory.Get(memoryPointer) == 0)
                            instructionPointer = brackets[instructionPointer];
                        break;
                    case ']':
                        if (memory.Get(memoryPointer) != 0)
                            instructionPointer = brackets[instructionPointer];
                        break;
                    default:
                        break;
                }
                instructionPointer++;
            }
        }

        static Dictionary<int, int> ParseBrackets(ref string code)
        {
            Stack<int> bracketStack = new();
            Dictionary<int, int> brackets = new();
            for (int i = 0; i < code.Length; i++)
            {
                if (code[i] == '[')
                {
                    bracketStack.Push(i);
                }
                else if (code[i] == ']')
                {
                    int j = bracketStack.Pop();
                    brackets.Add(j, i);
                    brackets.Add(i, j);
                }
            }
            return brackets;
        }
    }

    static class Extensions
    {
        public static TValue? Get<TKey, TValue>(this Dictionary<TKey, TValue> dict, TKey key, TValue? defaultValue = default(TValue)) where TKey : notnull
        {
            dict.TryGetValue(key, out defaultValue);
            return defaultValue;
        }
    }
}
