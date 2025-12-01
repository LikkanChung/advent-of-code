# Advent of Code 2025

TypeScript solutions for Advent of Code 2025.

## Setup

Install dependencies:
```bash
npm install
```

## Usage

### Initialize a new day

Creates the template solution file and input files for a specific day:

```bash
npm run init <day>
```

Example:
```bash
npm run init 1
```

This creates:
- `solution/day1.ts` (from template)
- `input/day1.txt` (for actual puzzle input)
- `test-input/day1.txt` (for test data)

### Solve a puzzle

Run your solution for a specific day and part:

```bash
npm run solve <day> <part> [test]
```

- `<day>`: Day number (1-25)
- `<part>`: Part 1 or 2
- `test`: Use test data instead of real input (optional)

Examples:
```bash
# Solve day 1, part 1 with real data
npm run solve 1 1

# Solve day 1, part 2 with test data
npm run solve 1 2 test
```

## Structure

```
2025/
├── aoc.ts              # Main runner script
├── package.json        # Node dependencies
├── tsconfig.json       # TypeScript configuration
├── solution/
│   ├── template.ts     # Template for new solutions
│   └── dayX.ts         # Daily solutions
├── input/
│   └── dayX.txt        # Real puzzle inputs
└── test-input/
    └── dayX.txt        # Test inputs
```
