require_relative "human"
class samurai
    def initialize
        super
            @health = 200
    end
    def death_blow
        if obj.class.ancestors.include?(Human)
            obj.health = 0
            true
        else
            false
        end
    end
    def meditate
        health = 200
    end
    def self.count
        @@count
    end
end