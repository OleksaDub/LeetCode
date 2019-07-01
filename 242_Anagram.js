/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if(s.length != t.length) return false;

    const sDict = {};
    const tDict = {};

    for(let char of s){
        sDict[char] = (sDict[char] || 0) + 1;
    }

    for(let char of t){
        tDict[char] = (tDict[char] || 0) + 1;
    }
    
    for(let key in sDict){
        if(!(sDict[key] == tDict[key])) return false;
    }
    
    return true;
};
