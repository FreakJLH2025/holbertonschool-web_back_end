// 10-car.js

export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  // Definir species para que subclases puedan controlar qué clase se usa al clonar
  static get [Symbol.species]() {
    return this;
  }

  // Método cloneCar que usa Symbol.species
  cloneCar() {
    const Cls = this.constructor[Symbol.species];
    return new Cls();
  }
}
