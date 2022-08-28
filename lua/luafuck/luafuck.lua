local ret = {}

local ioRead = io.read
local ioWrite = io.write
local stringByte = string.byte
local stringChar = string.char
local stringSub = string.sub
local tablePop = table.remove

function ret.parseBrackets(code)
    local brackets = {}
    local bracketStack = {}
    for i = 1, #code do
        local chr = stringSub(code, i, i)
        if chr == '[' then
            bracketStack[#bracketStack + 1] = i
        elseif chr == ']' then
            local j = tablePop(bracketStack)
            brackets[i], brackets[j] = j, i
        end
    end
    return brackets
end

local function wrap(value, min, max)
    if value < min then
        return max
    elseif value > max then
        return min
    end
    return value
end

function ret.run(code)
    local data = setmetatable({}, {
        __index = function(self, x)
            local thing = rawget(self, x)
            if thing == nil then
                rawset(self, x, 0)
                return 0
            end
            return thing
        end
    })
    local dataPointer = 1
    local instructionPointer = 1
    local length = #code
    local brackets = ret.parseBrackets(code)
    repeat
        local instr = stringSub(code, instructionPointer, instructionPointer)
        if instr == '>' then
            dataPointer = dataPointer + 1
        elseif instr == '<' then
            dataPointer = dataPointer - 1
        elseif instr == '+' then
            data[dataPointer] = wrap(data[dataPointer] + 1, 0, 255)
        elseif instr == '-' then
            data[dataPointer] = wrap(data[dataPointer] - 1, 0, 255)
        elseif instr == '.' then
            ioWrite(stringChar(data[dataPointer]))
        elseif instr == ',' then
            data[dataPointer] = stringByte(ioRead(1))
        elseif (instr == '[' and data[dataPointer] == 0
                or instr == ']' and data[dataPointer] ~= 0) then
            instructionPointer = brackets[instructionPointer]
        end
        instructionPointer = instructionPointer + 1
    until instructionPointer > length
end

return ret
