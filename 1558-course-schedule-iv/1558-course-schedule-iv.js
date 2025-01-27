/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @param {number[][]} queries
 * @return {boolean[]}
 */


// Floyd-Warshall Implementation
var checkIfPrerequisite = function (numCourses, prerequisites, queries) {

    const reachable = Array.from({length: numCourses}, () => new Array(numCourses).fill(false));

    // Set direct prerequisites
    for(const [u, v] of prerequisites){
        reachable[u][v] = true;
    }

    // Set indirect prerequisities
    for(let k = 0; k < numCourses; k++){
        for(let i = 0; i < numCourses; i++){
            for(let j = 0; j < numCourses; j++){
                if(reachable[i][k] && reachable[k][j]){
                    reachable[i][j] = true;
                }
            }
        }
    }

    console.log(reachable);

    return queries.map(([u, v]) => reachable[u][v]);
}


var checkIfPrerequisite1 = function (numCourses, prerequisites, queries) {
    const reachable = Array.from({ length: numCourses }, () => new Array(numCourses).fill(false));

    // Set direct prerequisites
    for (const [u, v] of prerequisites) {
        reachable[u][v] = true;
    }

    // Floyd-Warshall: Check indirect prerequisites
    for (let k = 0; k < numCourses; k++) {
        for (let i = 0; i < numCourses; i++) {
            for (let j = 0; j < numCourses; j++) {
                if (reachable[i][k] && reachable[k][j]) {
                    reachable[i][j] = true;
                }
            }
        }
    }

    // Answer the queries
    return queries.map(([u, v]) => reachable[u][v]);
};
