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
    let points: Coordinate[] = parseInput(inputData);
    // map x to y for each point
    let fill : Map<number, Set<number>> = points.reduce((map, point) => {
        if (!map.has(point.x)) {
            map.set(point.x, new Set<number>());
        }
        map.get(point.x)!.add(point.y);
        return map;
    }, new Map<number, Set<number>>());

    for (let i = 0; i < points.length; i++) {
        let pointA = points[i];
        let pointB = points[(i + 1) % points.length];
        
        if (pointA.x === pointB.x) {
            // fill vertical line
            let [startY, endY] = pointA.y < pointB.y ? [pointA.y, pointB.y] : [pointB.y, pointA.y];
            if (!fill.has(pointA.x)) {
                fill.set(pointA.x, new Set<number>());
            }
            for (let y = startY; y <= endY; y++) {

                fill.get(pointA.x)!.add(y);
            }
        } else if (pointA.y === pointB.y) {
            // fill horizontal line
            let [startX, endX] = pointA.x < pointB.x ? [pointA.x, pointB.x] : [pointB.x, pointA.x];
            for (let x = startX; x <= endX; x++) {
                if (!fill.has(x)) {
                    fill.set(x, new Set<number>());
                }
                fill.get(x)!.add(pointA.y);
            }
        }
    }

    // Calculate largest area where the lines between points are all inside the filled shape
    let xRanges = getXRanges(fill);
    let yRanges = getYRanges(fill);
    let largestArea = 0;
    for (let i = 0; i < points.length; i++) {
        for (let j = i + 1; j < points.length; j++) {
            // calculate area for each pair i and j
            let area = (Math.abs(points[i].x - points[j].x) + 1) * (Math.abs(points[i].y - points[j].y) + 1);

            if (area <= largestArea) {
                continue; // skip if area is not larger
            }

            // check if all points on the rectangle border are on or inside the shape
            let allValidPoints = true;
            // check vertical range line 
            for (let x = Math.min(points[i].x, points[j].x); x <= Math.max(points[i].x, points[j].x); x++) {
                let minY = yRanges[0].get(x)!;
                let maxY = yRanges[1].get(x)!;
                let rectMinY = Math.min(points[i].y, points[j].y);
                let rectMaxY = Math.max(points[i].y, points[j].y);
                if (rectMinY < minY || rectMaxY > maxY) {
                    allValidPoints = false;
                    break;
                }
            }
            // check horizontal range line
            for (let y = Math.min(points[i].y, points[j].y); y <= Math.max(points[i].y, points[j].y); y++) {
                let minX = xRanges[0].get(y)!;
                let maxX = xRanges[1].get(y)!;
                let rectMinX = Math.min(points[i].x, points[j].x);
                let rectMaxX = Math.max(points[i].x, points[j].x);
                if (rectMinX < minX || rectMaxX > maxX) {
                    allValidPoints = false;
                    break;
                }
            }

            if (allValidPoints && area > largestArea) {
                largestArea = area;
            }
        }
    }
    
    console.log("Part 2 Largest Filled Area:", largestArea);
}

type Coordinate = {
    x: number;
    y: number;
};

function getYRanges(fill: Map<number, Set<number>>): [Map<number, number>, Map<number, number>] {
    let minY : Map<number, number> = new Map();
    let maxY : Map<number, number> = new Map();
    for (let [x, ys] of fill.entries()) {
        minY.set(x, Math.min(...Array.from(ys)));
        maxY.set(x, Math.max(...Array.from(ys)));
    }
    return [minY, maxY];
}

function getXRanges(fill: Map<number, Set<number>>): [Map<number, number>, Map<number, number>] {
    // the fill map is from x to set of y
    // transpose to get from y to set of x
    let transposed : Map<number, Set<number>> = new Map();
    for (let [x, ys] of fill.entries()) {
        for (let y of ys) {
            if (!transposed.has(y)) {
                transposed.set(y, new Set<number>());
            }
            transposed.get(y)!.add(x);
        }
    }

    let minX : Map<number, number> = new Map();
    let maxX : Map<number, number> = new Map();
    for (let [y, xs] of transposed.entries()) {
        minX.set(y, Math.min(...Array.from(xs)));
        maxX.set(y, Math.max(...Array.from(xs)));
    }
    return [minX, maxX];
}

function parseInput(inputData: string[]): Coordinate[] {
    let coordinates: Coordinate[] = [];
    for (let line of inputData) {
        const parts = line.split(",").map(Number);
        coordinates.push({ x: parts[0], y: parts[1] });
    }
    return coordinates;
}