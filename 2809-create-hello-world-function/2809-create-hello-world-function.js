/**
 * @return {Function}
 */
var createHelloWorld = function() {
    
    return function(...args) {
        return f()
    }
};


const f = function(){
    return "Hello World"
}

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */