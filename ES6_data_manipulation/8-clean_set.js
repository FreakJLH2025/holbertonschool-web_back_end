// 8-clean_set.js

export default function cleanSet(set, startString) {
  if (!(set instanceof Set) || typeof startString !== 'string' || startString.length === 0) {
    return '';
  }

  const result = [];

  set.forEach((value) => {
    if (typeof value === 'string' && value.startsWith(startString)) {
      result.push(value.slice(startString.length));
    }
  });

  return result.join('-');
}
