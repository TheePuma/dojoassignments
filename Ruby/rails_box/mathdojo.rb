class Library
  attr_reader :amount
  def initialize
    # puts "this i s caled when somebody writer library.new"

    @amount = 0
  end
  def add number
    @amount += number
    self
  end
  def subtract number
    @amount -= number
    self
  end
  def multiply a, b
    @amount += a * b
    self
  end
  def divide a,b
    @amount += a / b
    self
  end
end

library1 = Library.new
# library1.add
# library1.subtract
# library1.add(100).add(100)
# library1.subtract(100)
# library1.multiply(50, 5)
# library1.divide(20, 4)
puts library1.amount
