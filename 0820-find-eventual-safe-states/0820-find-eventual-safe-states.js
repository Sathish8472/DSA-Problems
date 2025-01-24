/**
 * @param {number[][]} graph
 * @return {number[]}
 */
var eventualSafeNodes = function (graph) {
    const n = graph.length;
    const reverseGraph = Array.from({ length: n }, () => []);
    const inDegree = Array(n).fill(0);

    
    for (let u = 0; u < n; u++) {
        for (const v of graph[u]) {
            reverseGraph[v].push(u);
            inDegree[u]++;
        }
    }

    const queue = [];
    for (let i = 0; i < n; i++) {
        if (inDegree[i] === 0) queue.push(i);
    }

    // Process nodes in topological order
    const safeNodes = [];
    while (queue.length > 0) {
        const node = queue.shift();
        safeNodes.push(node);

        for (const neighbor of reverseGraph[node]) {
            inDegree[neighbor]--;
            if (inDegree[neighbor] === 0) queue.push(neighbor);
        }
    }

    return safeNodes.sort((a, b) => a - b);
};