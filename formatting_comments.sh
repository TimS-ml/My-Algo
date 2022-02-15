# !/usr/bin/fish

if [[ $1 == "all" ]]
then
    formatdir="./"
else
    formatdir="./"
fi

# find "$formatdir" -iname '*.py' -type f -exec sed -i -e \
#     "s/\，/, /g;\
#     s/\。/. /g;\
#     s/\：/: /g;\
#     s/\、/, /g;\
#     s/\—/-/g;\
#     s/“/\"/g;\
#     s/”/\"/g;\
#     s/【/ \[/g;\
#     s/】/\]/g;\
#     s/「/ \[/g;\
#     s/」/\]/g;\
#     s/《/ \[/g;\
#     s/》/\] /g;\
#     s/（/(/g;\
#     s/）/)/g;\
#     s/！/\! /g;\
#     s/？/\? /g;\
#     s/；/\; /g" {} \;

BEFORE="# Pros and Cons and Notation:"
AFTER=""
find "$formatdir" -iname '*.py' -type f -exec sed -i -e \
    "s/${BEFORE}/${AFTER}/g" {} \;

# find "$formatdir" -iname '*.md' -type f -exec sed -i -e \
#     "s/\，/, /g;\
#     s/\。/. /g;\
#     s/\：/: /g;\
#     s/\、/, /g;\
#     s/\—/-/g;\
#     s/“/\"/g;\
#     s/”/\"/g;\
#     s/【/ \[/g;\
#     s/】/\]/g;\
#     s/「/ \[/g;\
#     s/」/\]/g;\
#     s/《/ \[/g;\
#     s/》/\] /g;\
#     s/（/(/g;\
#     s/）/)/g;\
#     s/！/\! /g;\
#     s/？/\? /g;\
#     s/；/\; /g" {} \;
