export function part1(inputData: string[]): void {
    let points : Coordinate[] = parseInput(inputData);
    let connections: Connection[] = [];

    // calculate all pairwise distances
    for (let i = 0; i < points.length; i++) {
        for (let j = i + 1; j < points.length; j++) {
            let dist = euclideanDistance(points[i], points[j]);
            connections.push({ a: points[i], b: points[j], distance: dist });
        }
    }

    // sort connections ascending by euclidian distance
    connections.sort(connectionComparator);

    // seed circuits (each node starts in its own circuit)
    let connectedPoints: Set<Coordinate>[] = points.map(point => new Set([point]));

    // while less than 1000 connections in connectedPoints across all sets
    // N.B. The test scenario is <10
    for (let i = 0; i < 1000; i++) {
        connectedPoints = addConneciton(connectedPoints, connections[i]);
    }

    let setSizes : number[] = connectedPoints.map(set => set.size).sort((a, b) => b - a);
    console.log("Product of 3 largest: ", setSizes[0] * setSizes[1] * setSizes[2]);


}

export function part2(inputData: string[]): void {
    let points : Coordinate[] = parseInput(inputData);
    let connections: Connection[] = [];

    // calculate all pairwise distances
    for (let i = 0; i < points.length; i++) {
        for (let j = i + 1; j < points.length; j++) {
            let dist = euclideanDistance(points[i], points[j]);
            connections.push({ a: points[i], b: points[j], distance: dist });
        }
    }

    // sort connections ascending by euclidian distance
    connections.sort(connectionComparator);

    // seed circuits (each node starts in its own circuit)
    let connectedPoints: Set<Coordinate>[] = points.map(point => new Set([point]));

    while (connectedPoints.length !== 1) {
        connectedPoints = addConneciton(connectedPoints, connections[0]);

        if (connectedPoints.length === 1) {
            console.log("x prodduct:", connections[0].a.x * connections[0].b.x);
        }

        connections.shift();
    }
    
}

type Coordinate = {
    x: number;
    y: number;
    z: number;
}; 

function parseInput(inputData: string[]): Coordinate[] {
    return inputData.map(line => stringToCoordinate(line));
}

function stringToCoordinate(coordStr: string): Coordinate {
    const parts = coordStr.split(",").map(Number);
    return { x: parts[0], y: parts[1], z: parts[2] };
}

function euclideanDistance(a: Coordinate, b: Coordinate): number {
    return Math.sqrt(Math.pow(a.x - b.x, 2) + Math.pow(a.y - b.y, 2) + Math.pow(a.z - b.z, 2));
}

type Connection = {
    a: Coordinate;
    b: Coordinate;
    distance: number;
}

function connectionComparator(d1: Connection, d2: Connection): number {
    return d1.distance - d2.distance;
}

function addConneciton(connectedPoints: Set<Coordinate>[], connection: Connection): Set<Coordinate>[] {
    // merge the two sets containing connection.a and connection.b
    let setAIndex = -1;
    let setBIndex = -1;

    for (let i = 0; i < connectedPoints.length; i++) {
        if (connectedPoints[i].has(connection.a)) {
            setAIndex = i;
        }
        if (connectedPoints[i].has(connection.b)) {
            setBIndex = i;
        }
    }

    if (setAIndex !== -1 && setBIndex !== -1 && setAIndex !== setBIndex) {
        // merge sets
        let setA = connectedPoints[setAIndex];
        let setB = connectedPoints[setBIndex];

        setB.forEach(point => setA.add(point));
        connectedPoints.splice(setBIndex, 1); // remove setB
    }

    return connectedPoints;
}
