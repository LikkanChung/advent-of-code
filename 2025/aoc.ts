import * as fs from 'fs';
import * as path from 'path';

const USAGE = `
Advent of Code Utility:
To start a new day:
 > npm run init <day>
 Where <day> is the calendar day (1, 2, ... 25)
 This will create the template solution file and test/real data files 

To test a solution:
 > npm run solve <day> <part> [test]
 Where <part> is either \`1\` or \`2\`
 If \`test\` flag is used then the solution is tested with the test data set, otherwise the real data is used
`;

function init(day: string, realDataDir: string, testDataDir: string, solutionDir: string, templateFile: string): void {
    console.log(`Initialising Day ${day} solution files`);
    
    // Create data files
    const realDataPath = path.join(realDataDir, `day${day}.txt`);
    const testDataPath = path.join(testDataDir, `day${day}.txt`);
    
    if (!fs.existsSync(realDataPath)) {
        fs.writeFileSync(realDataPath, '');
    }
    if (!fs.existsSync(testDataPath)) {
        fs.writeFileSync(testDataPath, '');
    }
    
    // Copy template to solution file if it doesn't exist
    const solutionPath = path.join(solutionDir, `day${day}.ts`);
    if (!fs.existsSync(solutionPath)) {
        const templatePath = path.join(solutionDir, templateFile);
        fs.copyFileSync(templatePath, solutionPath);
        console.log(`Created ${solutionPath}`);
    } else {
        console.log(`${solutionPath} already exists`);
    }
}

async function solve(day: string, part: string, dataDir: string): Promise<void> {
    // Import the solution module dynamically
    const solutionPath = path.join(__dirname, 'solution', `day${day}.ts`);
    
    if (!fs.existsSync(solutionPath)) {
        console.error(`Error: Solution file ${solutionPath} does not exist`);
        return;
    }
    
    const module = await import(solutionPath);
    
    // Read the data file
    const dataFile = path.join(dataDir, `day${day}.txt`);
    const data = fs.readFileSync(dataFile, 'utf-8').split('\n');
    
    // Call the appropriate part function
    if (part === '1') {
        module.part1(data);
    } else if (part === '2') {
        module.part2(data);
    } else {
        console.error('Error: Solution must be part 1 or 2');
    }
}

function main(): void {
    const args = process.argv.slice(2);
    
    if (args.length === 0) {
        console.log(USAGE);
        return;
    }
    
    const utility = args[0]; // init or solve
    const day = args[1]; // 1 to 25
    
    const TEST_DATA_DIR = 'test-input';
    const REAL_DATA_DIR = 'input';
    const SOLUTION_DIR = 'solution';
    const TEMPLATE_SOLUTION = 'template.ts';
    
    if (utility === 'init') {
        if (!day) {
            console.error('Error: Please provide a day number');
            return;
        }
        init(day, REAL_DATA_DIR, TEST_DATA_DIR, SOLUTION_DIR, TEMPLATE_SOLUTION);
    } else if (utility === 'solve') {
        let part : string | undefined = args.at(2);
        let useTestData : boolean = args.at(3) === 'test';
        
        if (!day || !part) {
            console.error('Error: Please provide both day and part arguments');
            return;
        }
        
        const dataDir = useTestData ? TEST_DATA_DIR : REAL_DATA_DIR;
        solve(day, part, dataDir);
    } else {
        console.error('Error: argument must be init or solve');
        console.log(USAGE);
    }
}

main();
