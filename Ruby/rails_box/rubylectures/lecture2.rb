# string1 = "hello"
# string2 = "hello"
#
# symbol1 = :hello
# symbol2 = :hello
#
# my_hash = { first_name: "Eduardo", last_name: "Baik"}
# puts symbol1.equal?(symbol2)
# puts my_hash
# puts my_hash("first_name")

# print [1,2,3].class?.ancestors
# module Ninja
#   def throw_stars
#     puts "i am throwing stars"
#   end
# end
class Student
  # attr_reader :first_name
  attr_accessor :first_name, :last_name, :age

  def initialize f_name, l_name, age
    @first_name = f_name
    @last_name = l_name
    @age = age
  end
end

s = Student.new("Bryan", "R", 30)
s.first_name = "Lucio"
s.last_name = "Rodriguez"
s.age = 23

puts s.first_name
puts s.last_name
puts s.age
#
# class String
#   def who_am_i
#     puts self
#   end
#
# 10.who_am_i
