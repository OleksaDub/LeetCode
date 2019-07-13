/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    
    let test = Math.abs(x).toString().split("");
    let reversed = test.reverse().join("");
    let newInt = parseInt(reversed, 10);
    
    if(newInt > 2**31 - 1) return 0;
    else return newInt * Math.sign(x);
};

/*
	TOO SLOW!!!! NEEDS REDOING

	Runtime: 92 ms, faster than 17.72% of JavaScript online submissions for Reverse Integer.
	Memory Usage: 35.9 MB, less than 59.96% of JavaScript online submissions for Reverse Integer.
*/

var reverse2 = function(x) {
    
    let test = Math.abs(x).toString().split("");
    let reversed = test.reverse().join("");
    let newInt = parseInt(reversed, 10);
    
    if(reversed.length > 9) {
        if(newInt > 2**31 - 1) return 0;
    }
    return newInt * Math.sign(x);
    
};

/*
Runtime: 76 ms, faster than 73.20% of JavaScript online submissions for Reverse Integer.
Memory Usage: 35.9 MB, less than 59.96% of JavaScript online submissions for Reverse Integer.
*/
