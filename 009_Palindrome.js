/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    if(x < 0) return false;
    
    let str = x.toString();
    while (str.length > 1){
        if(str[0] != str[str.length-1]) return false;
        else str = str.substring(1, str.length-1);
    }
    return true;    
};

/*
Runtime: 184 ms, faster than 87.17% of JavaScript online submissions for Palindrome Number.
Memory Usage: 45.6 MB, less than 66.56% of JavaScript online submissions for Palindrome Number.
*/
