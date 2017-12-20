require_relative 'bankaccount'
RSpec.describe BankAccount do
    before(:each) do
        @account = BankAccount.new('name 1', 200)
end