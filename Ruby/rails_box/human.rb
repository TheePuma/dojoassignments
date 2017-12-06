class Human
  attr_accessor :strength, :intelligence, :stealth, :health
  def initialize
    @health = 100
    @strength = 3
    @intelligence = 3
    @stealth = 3
  end
  def attack(obj)
    if obj.class.ancestors.include?(Human)
      obj.health -= 10
      true
    else
      false
    end
  end
end

hum1 = Human.new
hum2 = Human.new

puts hum1.attack(hum2)
puts hum1.attack("Not a Human")
puts hum2.health
