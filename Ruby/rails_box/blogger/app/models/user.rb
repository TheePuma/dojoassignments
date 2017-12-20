class User < ActiveRecord::Base
    EMAIL_REGEX = /\A([^@\s]+)@((?:[-a-z0-9]+\.)+[a-z]+)\z/i
    has_many :posts
    has_many :owners
    has_many :messages

    has_many :blogs, through: :posts
    has_many :blog_posts, through: :owners

    validates :last_name, :first_name, presence: true
    validates :email, uniqueness: { case_sensitive: false }, format: { with: EMAIL_REGEX }
end
