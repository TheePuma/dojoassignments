class Project
  attr_accessor :name, :description, :owner, :task
  def initialize name, description, owner, task
    @name = name
    @description = description
    @owner = owner
    @task = []
  end
  def elevator_pitch
    "#{@name}, #{@description}"
  end
  def print_tasks
    @tasks.each {|elem| puts elem}
  end
  def add_tasks task
    @tasks < task
  end
end