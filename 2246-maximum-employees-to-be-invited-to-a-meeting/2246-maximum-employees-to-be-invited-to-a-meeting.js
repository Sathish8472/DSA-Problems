/**
 * @param {number[]} favorites
 * @return {number}
 */
var maximumInvitations = function(favorites) {
    // Helper function to calculate maximum cycle length
    const findMaxCycleLength = (favorites) => {
        const n = favorites.length;
        const visited = new Array(n).fill(false);
        let maxCycle = 0;

        for (let i = 0; i < n; i++) {
            if (visited[i]) continue;

            const cycle = [];
            let current = i;
            while (!visited[current]) {
                cycle.push(current);
                visited[current] = true;
                current = favorites[current];
            }

            // Find the cycle and its length
            for (let k = 0; k < cycle.length; k++) {
                if (cycle[k] === current) {
                    maxCycle = Math.max(maxCycle, cycle.length - k);
                    break;
                }
            }
        }

        return maxCycle;
    };

    // Helper function for topological sorting and calculating longest path
    const calculateLongestChain = (favorites) => {
        const n = favorites.length;
        const inDegrees = new Array(n).fill(0);
        const chainLengths = new Array(n).fill(1);

        // Calculate the in-degree of each node
        for (let favorite of favorites) {
            inDegrees[favorite]++;
        }

        const queue = [];
        // Collect all nodes with in-degree of 0
        for (let i = 0; i < n; i++) {
            if (inDegrees[i] === 0) {
                queue.push(i);
            }
        }

        // Perform topological sort and calculate longest chains
        while (queue.length > 0) {
            const node = queue.shift();
            const nextNode = favorites[node];
            chainLengths[nextNode] = Math.max(chainLengths[nextNode], chainLengths[node] + 1);
            inDegrees[nextNode]--;

            if (inDegrees[nextNode] === 0) {
                queue.push(nextNode);
            }
        }

        // Calculate the total contributions from topological sort
        let totalContribution = 0;
        for (let i = 0; i < n; i++) {
            if (i === favorites[favorites[i]]) {
                totalContribution += chainLengths[i];
            }
        }

        return totalContribution;
    };

    // Return the maximum value from both cycle and topological sort results
    return Math.max(findMaxCycleLength(favorites), calculateLongestChain(favorites));
};
