class BankAccount
  def initialize name, balance
    @name = name
    @balance = balance
  end
  def showbalance
    "Your balance is $#{@balance},"
  end
  def withdraw
    if amount > balance
        error
        puts "You have overdrawn your balance!"
  end
end