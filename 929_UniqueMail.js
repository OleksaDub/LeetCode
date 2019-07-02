/**
 * @param {string[]} emails
 * @return {number}
 */
var numUniqueEmails = function(emails) {
    let unique = new Set();
    emails.forEach(function(mail) {
        let address = mail.replace(/\+.*@/, '@').match(/.*?(?=@|$)/i)[0].replace(/ |\./g, '');
        let domain = mail.substr(mail.lastIndexOf('@'));
        let email = address + domain;
        unique.add(email)
    });
    return unique.size;
};

numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"])
