export function part1(inputData: string[]): void {
    let currentDigit : number = 50;
    let zeroCount : number = 0;
    for (const line of inputData) {
        const direction : number = line.charAt(0) === 'L' ? -1 : 1;
        const steps : number = parseInt(line.slice(1));
        currentDigit += direction * steps;
        while (currentDigit < 0 || currentDigit >= 100) {
            if (currentDigit < 0) {
                currentDigit += 100;
            } else if (currentDigit >= 100) {
                currentDigit -= 100;
            }
        }
        if (currentDigit === 0) {
            zeroCount += 1;
        }
    }   
    console.log(`Zero count: ${zeroCount}`);
}

export function part2(inputData: string[]): void {
    let currentDigit : number = 50;
    let zeroCount : number = 0;
    for (const line of inputData) {
        const direction : number = line.charAt(0) === 'L' ? -1 : 1;
        const steps : number = parseInt(line.slice(1));
        for (let i = 0; i < steps; i++) {
            currentDigit += direction;

            if (currentDigit < 0) {
                currentDigit += 100;
            } else if (currentDigit >= 100) {
                currentDigit -= 100;
            }
            if (currentDigit === 0) {
                zeroCount += 1;
            }
        }
    }   
    console.log(`Zero count: ${zeroCount}`);
}
