/**
 * @param {string} word
 * @return {boolean}
*/
var detectCapitalUse = function(word) {
    if(word.length < 2) return true;

    var validpattern1 = new RegExp('^[A-Z]+$');
    var validpattern2 = new RegExp('^[a-z]+$');
    var isvalidChars;
    if (word.match(validpattern1) || word.substring(1).match(validpattern2))
       return true;
    else
       return false;
};

/*
Runtime: 56 ms, faster than 94.27% of JavaScript online submissions for Detect Capital.
Memory Usage: 34.2 MB, less than 48.35% of JavaScript online submissions for Detect Capital.
*/
