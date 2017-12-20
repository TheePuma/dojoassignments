require_relative "human"
class Wizard
    def initialize
        super
            @health = 50
            @intelligence = 25
    end
    def heal
        @health += 10
    end
    def fireball
        if obj.class.ancestors.include?(Human)
            obj.health -= 20
            true
        else
            false
        end
    end
end