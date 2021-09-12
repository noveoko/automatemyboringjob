# Search for Files

## Find all files over 500 MB

find . -size +500M

## Find files by permission (777) 

find . -perm 777

## Find empty files

find -empty

# Search for files by contents

## Search for all files recursively, case-insensitive, with location line number > containing the string Miraszewski 
grep "Miraszewski" -rin .

## Find every image regardless of filename

find . -name '*' -exec file {} \; | grep -o -P '^.+: \w+ image'


