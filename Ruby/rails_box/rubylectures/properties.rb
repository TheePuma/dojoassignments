class User
  attr_accessor :first_name
  attr_accessor :last_name
  # def first_name
  #   @first_name
  # end
  #
end

user1 = User.new
user2 = User.new

user1.first_name = "Blaine"
user1.last_name = "Prather"
user2.first_name = "Michael"
# puts "#{user1.first_name} " + "#{user1.last_name}"
# puts user1.last_name
# puts user1.inspect
# puts user1.first_name
puts "#{user1.first_name} is going to help #{user2.first_name}"
