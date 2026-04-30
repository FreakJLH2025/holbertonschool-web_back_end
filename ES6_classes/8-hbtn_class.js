// 8-hbtn_class.js

export default class HolbertonClass {
  constructor(size, location) {
    if (typeof size !== 'number') {
      throw new TypeError('Size must be a number');
    }
    if (typeof location !== 'string') {
      throw new TypeError('Location must be a string');
    }

    this._size = size;
    this._location = location;
  }

  // Getter para size
  get size() {
    return this._size;
  }

  // Getter para location
  get location() {
    return this._location;
  }

  // Conversión a Number
  valueOf() {
    return this._size;
  }

  // Conversión a String
  toString() {
    return this._location;
  }
}
