export function part1(inputData: string[]): void {
    console.log(`Count of accessible positions: ${findAccessiblePositions(inputData).length}`);
}

export function part2(inputData: string[]): void {
    let accessible_positions : number[][] = findAccessiblePositions(inputData);
    let totalRemoved : number = 0;
    while (accessible_positions.length > 0) {
        for (let pos of accessible_positions) {
            let x : number = pos[0];
            let y : number = pos[1];
            inputData[y] = inputData[y].substring(0, x) + '#' + inputData[y].substring(x + 1);
            totalRemoved += 1;
        }
        accessible_positions = findAccessiblePositions(inputData);
    }
    console.log(`Total accessible positions removed: ${totalRemoved}`);
}

function findAccessiblePositions(inputData: string[]): number[][] {
    let accessible_positions : number[][] = [];
    for (let y = 0 ; y < inputData.length; y++) {
        for (let x = 0; x <  inputData[y].length; x++) {
            let x0 : number = Math.max(0, x - 1);
            let x1 : number = Math.min(inputData[y].length - 1, x + 1);
            let y0 : number = Math.max(0, y - 1);
            let y1 : number = Math.min(inputData.length - 1, y + 1);
            if (inputData[y][x] === '@') {
                let sum_of_neighbors : number = 0;
                for (let yy = y0; yy <= y1; yy++) {
                    let yy_str = inputData[yy].slice(x0, x1 + 1);
                    sum_of_neighbors += yy_str.split('@').length - 1;
                }
                if (sum_of_neighbors < 5) {
                    accessible_positions.push([x, y]);
                }
            }
        }
    }
    return accessible_positions
}