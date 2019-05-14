#!/usr/bin/node
exports.converter = function converter (base) {
  if (typeof converter.Num === 'undefined') {
    converter.Num = base;
    return converter;
  } else {
    return parseInt(converter.Num, base);
  }
};
