/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    // return an object with 2 funcs
    return{
        // For each func, check if given value ir Equal or Not Equal to val
        toBe: function(num){
            if (num === val){
                return true;
            } else if (num !== val){
                throw "Not Equal";
            };
        },
    
        notToBe: function(num){
            if (num !== val){
                return true;
            } else{
                throw "Equal";
            }
        }
    };
    
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */
