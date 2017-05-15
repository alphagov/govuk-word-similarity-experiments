File.write(
  'output/terms.txt',
  File.read("source.txt").lines.flat_map { |l| l.split(',') }.map(&:strip).uniq.sort.join("\n")
)
