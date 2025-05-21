class Greeter {
    constructor(name, greeting) {
      this.name = name;
      this.greeting = greeting;
    }
      
    greet() {
      const name = this.name;
      const greeting = this.greeting;
      
      if (!name) {
        name = "Anonymous";
      }
      if (greeting = undefined) {
        greeting = "Hello";
      }
      
      return "${greeting}, ${name}!";
    }
  }
   
  g = new Greeter("Hi")
  g.greet()