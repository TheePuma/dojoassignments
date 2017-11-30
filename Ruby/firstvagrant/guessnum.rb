def guessnum guess
  number = 25
  if guess < 25
    puts "Too low"
  elsif guess > 25
    puts "Too high"
  else
    puts "You got it!"
  end
end
guessnum(27)
