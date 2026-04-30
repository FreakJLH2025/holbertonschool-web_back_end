// 10-car.js

const _cloneSymbol = Symbol('cloneCar');

export default class Car {
  constructor(brand, motor, color) {
    if (typeof brand !== 'string') {
      throw new TypeError('Brand must be a string');
    }
    if (typeof motor !== 'string') {
      throw new TypeError('Motor must be a string');
    }
    if (typeof color !== 'string') {
      throw new TypeError('Color must be a string');
    }

    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  // Método cloneCar usando Symbol
  [_cloneSymbol]() {
    const Cls = this.constructor; // referencia dinámica a la clase actual
    return new Cls(this._brand, this._motor, this._color);
  }

  // Exponer cloneCar como método público
  cloneCar() {
    return this[_cloneSymbol]();
  }
}
