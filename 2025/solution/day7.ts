export function part1(inputData: string[]): void {
    let totalSplits : number = 0;
    let beamIndexes: Set<number> = new Set([inputData[0].indexOf("S")]);
    
    for (let row = 1; row < inputData.length; row++) {
        let newBeamIndexes: Set<number> = new Set();
        for (let beamIndex of beamIndexes) {
            if (inputData[row].charAt(beamIndex) === "^") {
                newBeamIndexes.add(beamIndex -1);
                newBeamIndexes.add(beamIndex +1);
                totalSplits++;
            } else {
                newBeamIndexes.add(beamIndex);

            }
        }
        beamIndexes = newBeamIndexes;
    }
    console.log("Part 1 Total Splits:", totalSplits);
}

export function part2(inputData: string[]): void {
    let beamIndexes: Set<number> = new Set([inputData[0].indexOf("S")]);
    let visitCounts: Map<number, Map<number, number>> = new Map();
    
    for (let row = 1; row < inputData.length ; row++) {
        if (visitCounts.get(row) === undefined) {
            visitCounts.set(row, new Map());
        }
        let newBeamIndexes: Set<number> = new Set();
        for (let beamIndex of beamIndexes) {
            if (inputData[row].charAt(beamIndex) === "^") {
                newBeamIndexes.add(beamIndex -1);
                newBeamIndexes.add(beamIndex +1);
            
                let beamBeforeSplit : number = visitCounts.get(row -1)?.get(beamIndex) || 1;
                visitCounts.get(row)!.set(beamIndex -1, (visitCounts.get(row)!.get(beamIndex -1) || 0) + beamBeforeSplit);
                visitCounts.get(row)!.set(beamIndex +1, (visitCounts.get(row)!.get(beamIndex +1) || 0) + beamBeforeSplit);

            } else {
                newBeamIndexes.add(beamIndex);
                let beamFromAbove : number = visitCounts.get(row -1)?.get(beamIndex) || 1;
                visitCounts.get(row)!.set(beamIndex, (visitCounts.get(row)!.get(beamIndex) || 0) + beamFromAbove);
            }
            
        }
        beamIndexes = newBeamIndexes;
    }

    console.log("Sum of visit counts in last row:", [...(visitCounts.get(inputData.length -1)?.values() || [])].reduce((acc, val) => acc + val, 0));

}