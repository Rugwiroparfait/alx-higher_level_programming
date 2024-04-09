#!/usr/bin/node

const { dict } = require('./101-data');


function invertDictionary(originalDict) {
  const invertedDict = {};

 
  for (const userId in originalDict) {
    const occurrences = originalDict[userId];
    
    
    if (!invertedDict[occurrences]) {
      invertedDict[occurrences] = [];
    }
    
   
    invertedDict[occurrences].push(userId);
  }

  return invertedDict;
}


const newDict = invertDictionary(dict);


console.log(newDict);
