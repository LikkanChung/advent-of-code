export function part1(inputData: string[]): void {
    let problemNumbers: string[][] = [];
    for (let i = 0; i < inputData.length - 1; i++) {
        let numbers = inputData[i].trim().split(/\s+/);
        for (let j = 0; j < numbers.length; j++) {
            if (problemNumbers[j] === undefined) {
                problemNumbers[j] = [];
            }
            problemNumbers[j].push(numbers[j]);
        }
    }
    let problemOperation = inputData[inputData.length - 1].trim().split(/\s+/);
    let total : number = 0;
    for (let i = 0; i < problemNumbers.length; i++) {
        let operation = problemOperation[i];
        let numbers = problemNumbers[i].map(Number);
        if (operation === "+") {
            total += numbers.reduce((a, b) => a + b, 0);
        } else if (operation === "*") {
            total += numbers.reduce((a, b) => a * b, 1);
        } 
    }
    console.log("Part 1 Total:", total);
}

export function part2(inputData: string[]): void {
    let maxRowLength: number = inputData[0].length;
    for (let i = 1; i < inputData.length; i++) {
        if (inputData[i].length > maxRowLength) {
            maxRowLength = inputData[i].length;
        }
    }
    let operatorRow: number = inputData.length - 1;
    
    let total: number = 0;

    let currentOperator: string = inputData[operatorRow][0];
    let currentNumber: number = (currentOperator === "+") ? 0 : 1;

    let i : number = 0;
    while (i < maxRowLength) {
        // check if it's a new problem
        if (isSeparatorCol(inputData, i)) {
            // handle the old number 
            console.log(`Problem done: ${currentOperator} ${currentNumber}`);
            total += currentNumber;

            // start new problem
            currentOperator = inputData[operatorRow][i+1];
            if (currentOperator === "+") {
                currentNumber = 0;
            } else if (currentOperator === "*") {
                currentNumber = 1;
            }
        } else {

            //read this nummber
            let numberStr: string = "";
            for (let j = 0; j < operatorRow; j++) {
                numberStr += inputData[j][i];
            }

            let number: number = Number(numberStr);
            if (currentOperator === "+") {
                currentNumber += number;
            } else if (currentOperator === "*") {
                currentNumber *= number;
            }
        }
        i++;
    }

    total += currentNumber;
    console.log("Part 2 Total:", total);
}

function isSeparatorCol(inputData: string[], colIndex: number): boolean {
    for (let i = 0; i < inputData.length; i++) {
        if (inputData[i][colIndex] !== " ") {
            return false;
        }
    }
    return true;    
}