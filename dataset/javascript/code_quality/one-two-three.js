if (typeof console === 'undefined') console = {log: print};

function one(){
  console.log('a');
  return {
    get p() {
      console.log('e');
      return {
        valueOf: function(){
          console.log('g');
          return {};
        },
        toString: function(){
          console.log('h');
          return false;
        }
      };
    },
    set p(x) {
      console.log('k');
    }
  };
}

function two(){
  console.log('b');
  return {
    toString: function(){
      console.log('c');
      return {};
    },
    valueOf: function(){
      console.log('d');
      return 'p';
    }
  };
}

function three() {
  console.log('f');
  return {
    valueOf: function(){
      console.log('i');
      return {};
    },
    toString: function(){
      console.log('j');
      return false;
    }
  };
}

one()[two()] += three();