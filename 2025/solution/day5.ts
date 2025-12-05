export function part1(inputData: string[]): void {
    let input : Input = parseInput(inputData);
    console.log(`Total IDs out of range: ${input.outOfRangeIds}`);
}

export function part2(inputData: string[]): void {
    let input : Input = parseInput(inputData);
    
    // keep a list of optimised ranges
    // iterate over the input ranges, and merge them where they overlap
    let optimizedRanges : Range[] = [];
    for (let range of input.ranges) {
        optimizedRanges = mergeRange(range, optimizedRanges);  
    }
    console.log(`Optimized Ranges: ${JSON.stringify(optimizedRanges)}`);
    let totalCoveredIds : number = 0;
    for (let range of optimizedRanges) {
        totalCoveredIds += (range.end - range.start + 1);
    }
    console.log(`Total IDs covered by ranges: ${totalCoveredIds}`);
}

interface Input {
    ranges: Range[];
    outOfRangeIds: number;
}

interface Range {
    start: number;
    end: number;
}

function parseInput(inputData: string[]): Input {
    let input : Input = {ranges: [], outOfRangeIds: 0};
    for (let line of inputData) {
        input = parseLine(line, input);
    }
    return input;
}

function parseLine(line: string, input: Input): Input {
    if (line.includes('-')) {
        let [startStr, endStr] = line.split('-');
        const start : number = parseInt(startStr);
        const end : number = parseInt(endStr);
        input.ranges.push({start: start, end: end});
    } else if (line.length > 0) {
        const id : number = parseInt(line);
        input.outOfRangeIds += isInRange(id, input.ranges) ? 1 : 0;
    }
    return input;
}

function isInRange(id: number, ranges: Range[]): boolean {
    for (let range of ranges) {
        if (id >= range.start && id <= range.end) {
            return true;
        }
    }
    return false;
}

function mergeRange(newRange: Range, ranges: Range[]): Range[] {
    // add the new range to the list, merging where necessary
    // return the new list of ranges when there are no overlaps
    let mergedRanges : Range[] = [...ranges, newRange];
    let sortedRanges : Range[] = sortRangesByStart(mergedRanges);
    while (rangesHaveOverlap(sortedRanges)) {
        let tempRanges : Range[] = [];
        let i : number = 0;
        while (i < sortedRanges.length) {
            let currentRange : Range = sortedRanges[i];
            if (i < sortedRanges.length - 1 && rangesOverlap(currentRange, sortedRanges[i + 1])) {
                let mergedRange : Range = mergeTwoRanges(currentRange, sortedRanges[i + 1]);
                tempRanges.push(mergedRange);
                i += 2; // skip the next range as it has been merged
            } else {
                tempRanges.push(currentRange);
                i += 1;
            }
        }
        sortedRanges = tempRanges;
    }
    return sortedRanges;

}

function rangesHaveOverlap(ranges: Range[]): boolean {
    for (let i = 0; i < ranges.length; i++) {
        for (let j = i + 1; j < ranges.length; j++) {
            if (rangesOverlap(ranges[i], ranges[j])) {
                return true;
            }
        }
    }
    return false;
}

function rangesOverlap(range1: Range, range2: Range): boolean {
    return range1.start <= range2.end && range2.start <= range1.end;
}

function mergeTwoRanges(range1: Range, range2: Range): Range {
    return {
        start: Math.min(range1.start, range2.start),
        end: Math.max(range1.end, range2.end)
    };
}

function sortRangesByStart(ranges: Range[]): Range[] {
    return ranges.sort((a, b) => a.start - b.start);
}

