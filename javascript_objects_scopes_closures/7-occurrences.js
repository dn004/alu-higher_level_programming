#!/usr/bin/node
exports.nbOccurences = (list, searchElement) => {
    return (list.filter(elem => elem === searchElement).length);
};
