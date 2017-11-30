class Attacked
  def initialize
    @health = 50
  end
  def attack
    @health -= 5
  end
  def display_health
    puts "Attacked health: "
    puts @health
  end
end
