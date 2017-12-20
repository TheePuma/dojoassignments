class Message < ActiveRecord::Base
    belongs_to :post
    validates :author, :message, length: { minimum: 15 }
end
