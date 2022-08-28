#![warn(clippy::nursery, clippy::pedantic)]

use std::collections::{HashMap, LinkedList};
use std::env;
use std::fs;
use std::io::Write;
use getch::Getch;

fn main() {
    let args: Vec<String> = env::args().collect();
    assert!(args.len() >= 2, "not enough arguments");
    let code: Vec<u8> = fs::read_to_string(&args[1])
        .expect("unable to read file")
        .chars()
        // .filter(|x| ['>', '<', '+', '-', '.', ',', '[', ']'].contains(x))
        .map(|x| x as u8)
        .collect();
    let code_length = code.len();
    let mut memory: HashMap<usize, u8> = HashMap::new();
    let mut memory_pointer: usize = 0;
    let mut instruction_pointer = 0;
    let brackets = parse_brackets(&code);
    while instruction_pointer < code_length {
        match code.get(instruction_pointer).unwrap() {
            b'>' => {
                memory_pointer = memory_pointer.wrapping_add(1);
            }
            b'<' => {
                memory_pointer = memory_pointer.wrapping_sub(1);
            }
            b'+' => {
                let value = memory.get(&memory_pointer).unwrap_or(&0).wrapping_add(1);
                memory.insert(memory_pointer, value);
            }
            b'-' => {
                let value = memory.get(&memory_pointer).unwrap_or(&0).wrapping_sub(1);
                memory.insert(memory_pointer, value);
            }
            b'.' => {
                print!("{}", *memory.get(&memory_pointer).unwrap_or(&0) as char);
                std::io::stdout().flush().unwrap();
            }
            b',' => {
                let getch = Getch::new();
                let input = getch.getch().unwrap();
                memory.insert(memory_pointer, input as u8);
            }
            b'[' => {
                if *memory.get(&memory_pointer).unwrap_or(&0) == 0 {
                    instruction_pointer = brackets[&instruction_pointer];
                }
            }
            b']' => {
                if *memory.get(&memory_pointer).unwrap_or(&0) != 0 {
                    instruction_pointer = brackets[&instruction_pointer];
                }
            }
            _ => {}
        }
        instruction_pointer += 1;
    }
}

fn parse_brackets(code: &[u8]) -> HashMap<usize, usize> {
    let mut bracket_stack: LinkedList<usize> = LinkedList::new();
    let mut brackets: HashMap<usize, usize> = HashMap::new();
    for (i, instruction) in code.iter().enumerate() {
        if instruction == &b'[' {
            bracket_stack.push_back(i);
        }
        else if instruction == &b']' {
            let j = bracket_stack.pop_back().unwrap();
            brackets.insert(j, i);
            brackets.insert(i, j);
        }
    }
    brackets
}
