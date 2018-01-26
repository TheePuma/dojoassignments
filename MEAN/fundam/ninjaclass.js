function ninjaConstructor(name, health, speed, strength) {
    ninja.name = name;
    ninja.health = health;
    ninja.speed = speed;
    ninja.strength = strength;
    ninja.type = ninja
    ninja.punch = function(target){
      if(target.type == ninja){
        target.health -= 5;
      }
      console.log("Used attack Punch. " + target.name + "lost 5 health!")
    }
    ninja.sayname = function(){
      console.log("My name is" + ninja.name + "!")
      
    }
    ninja.showStats = function(){
      console.log("Name: " + ninja.name + ", Health: " + ninja.health + ", Speed: " + ninja.speed + ", Strength: " + ninja.strength)
    }
  }
