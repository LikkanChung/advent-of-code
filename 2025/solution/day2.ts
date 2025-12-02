export function part1(inputData: string[]): void {
    let sum : number = 0;
    let input : string = inputData[0];
    for (var range of input.split(',')) {
        let [startStr, endStr] = range.split('-');
        const start : number = parseInt(startStr);
        const end : number = parseInt(endStr);
        for (let i = start; i <= end; i++) {
            const idStr : string = i.toString();
            if (idStr.length % 2 === 0) {
                const left = idStr.slice(0, idStr.length / 2);
                const right = idStr.slice(idStr.length / 2);
                sum += left === right ? i : 0;
            }
        }
    }
    console.log(`Sum of ranges: ${sum}`);
}

export function part2(inputData: string[]): void {
    let sum : number = 0;
    let input : string = inputData[0];
    for (var range of input.split(',')) {
        let [startStr, endStr] = range.split('-');
        const start : number = parseInt(startStr);
        const end : number = parseInt(endStr);
        for (let i = start; i <= end; i++) {
            sum += !isValid(i) ? i : 0;
        }
    }
    console.log(`Sum of ranges: ${sum}`);
}

function isValid(id: number) : boolean {
    const idStr : string = id.toString();

    let candidateSubstrings : Set<string> = new Set<string>();
    // construct possible substrings
    for (let i = idStr.length / 2; i > 0 ; i--) {
        candidateSubstrings.add(idStr.slice(0, i));    
    }
    for (let substring of candidateSubstrings) {
        if (idStr.length % substring.length !== 0) {
            continue;
        }
        let repeatedStr : string = substring.repeat(idStr.length / substring.length);
        if (repeatedStr === idStr) {
            return false;
        }
    }
    return true;
}