export function part1(inputData: string[]): void {
    
    let coordinates: Coordinate[] = parseInput(inputData);
    let largestArea = 0;
    for (let i = 0; i < coordinates.length; i++) { 
        for (let j = i + 1; j < coordinates.length; j++) {
            let area = (Math.abs(coordinates[i].x - coordinates[j].x) + 1) * (Math.abs(coordinates[i].y - coordinates[j].y) + 1);
            if (area > largestArea) {
                largestArea = area;
            }
        }
    }
    console.log("Part 1 Largest Area:", largestArea);
}

export function part2(inputData: string[]): void {
    // TODO: Implement part 2
}

type Coordinate = {
    x: number;
    y: number;
};

function parseInput(inputData: string[]): Coordinate[] {
    let coordinates: Coordinate[] = [];
    for (let line of inputData) {
        const parts = line.split(",").map(Number);
        coordinates.push({ x: parts[0], y: parts[1] });
    }
    return coordinates;
}