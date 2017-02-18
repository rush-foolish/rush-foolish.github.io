################################################################
#   Copyright (C) 2017 All rights reserved.
#   
#   Filename：gen_index.rb
#   Creator：Mark Luo
#   Created Date：02/15/2017
#   Description：
#       generate an index.md according to repository hierarchy 
#   Modified History：
#
################################################################

INDEX_HEAD = <<HEAD
## Welcome to My Blog ...  

> Actually, miscellaneous notes rather than blog ...  

## Index

HEAD

INDEX_END = <<END
> Thanks to Markdown and Jekyll.
END

BASE_URL = "rush-foolish.github.io"

def walk(dir,depth)
    if depth > 0
        depth = depth - 1
        Dir.foreach(dir) do |x|
            path = File.join(dir,x)
            if x =~ /^[\.,_].*$/ # skip dir which start with . and _
                next
            elsif File.directory?(path)
                puts "#"*(depth+2) + " " + File.basename(path) if depth == 1
                walk(path,depth)
            else
                puts "- [%s](#{BASE_URL}/%s/%s)" % [File.basename(x,".md"),File.basename(dir),File.basename(x,".md")] if depth == 0
            end
        end
        puts
    end
end


    
$stdout.reopen("index.md","w")

puts INDEX_HEAD
walk(".",2)
puts INDEX_END

