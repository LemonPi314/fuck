local path = assert(arg[1], "file not given")
local file = assert(io.open(path, "r"), "file not found")
local content = file:read("*all")
file:close()

local mod = require("luafuck")
mod.run(content)
