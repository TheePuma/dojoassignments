require_relative "Mammal"
class Dog < Mammal
  def initialize
    @health = 150
  end
  def pet
    @health += 5
    self
  end
  def walk
    @health -= 1
    self
  end
  def run
    @health -= 10
    self
  end
  def display_health
    puts @health
  end
end
dog1 = Dog.new
dog1.walk.walk.walk.run.run.display_health
