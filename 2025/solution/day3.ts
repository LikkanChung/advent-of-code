export function part1(inputData: string[]): void {
    let bankTotals : number = 0;
    for (let line of inputData) {
        let max : number = parseInt(line[0]);
        console.log(`Processing line: ${line}`);
        for (let i = 0; i < line.length - 1; i++) {
            const firstDigit : number = parseInt(line[i]);
            for (let j = i + 1; j < line.length; j++) {
                const secondDigit : number = parseInt(line[j]);
                const number : number = (10 * firstDigit) + secondDigit;
                if (number > max) {
                    max = number;
                }
            }
        }
        console.log(`Max number for line: ${max}`);
        bankTotals += max;
    }
    console.log(`Total of all max numbers: ${bankTotals}`);
}

export function part2(inputData: string[]): void {
    let bankTotals : number = 0;
    for (let line of inputData) { 
        let numberLength : number = 12; 
        let numberBuilder: string = "";
        let windowStartIndex : number = 0;
        while (numberBuilder.length < numberLength) {
            // create a slice window where the max digit can be found, 
            // if the remaining digits are 12, then the last 11 digits can be skipped
            let windowEndIndex : number = line.length - (numberLength - numberBuilder.length) + 1;
            let searchWindow : string = line.slice(windowStartIndex, windowEndIndex);
            let maxSubIndex : number = searchWindow.indexOf(Math.max(...searchWindow.split('').map(Number)).toString());

            numberBuilder += searchWindow[maxSubIndex];
            windowStartIndex += maxSubIndex + 1;
            
        }
        bankTotals += parseInt(numberBuilder);
    }
    console.log(`Total of all constructed numbers: ${bankTotals}`);
}
