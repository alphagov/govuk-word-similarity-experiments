require 'fuzzy_match'

WORDS = File.read("output/terms.txt").lines.map(&:chomp)

WORDS.each do |word|
  matches = FuzzyMatch.new(WORDS - [word]).find(word)
  puts "'#{word}' looks like '#{matches}'"
end
