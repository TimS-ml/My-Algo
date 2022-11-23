#!/usr/bin/bash

# https://askubuntu.com/questions/343727/filenames-with-spaces-breaking-for-loop-find-command
lc="./LeetCode/"
lc_sql="./LeetCode/SQL/"
edu="./Educative/"
hack="./HackerRank/"

if [ $1 == 'py' ]
then
    if [ $2 == 'all' ]
    then
        for pycode in $(find . -type f -name '*.py'); do
            echo "$pycode"
            yapf -i -r "$pycode"
        done
    elif [ $2 == 'lc' ]
    then
        for pycode in "$lc"*.py; do
            echo "$pycode"
            yapf -i -r "$pycode"
        done
    elif [ $2 == 'edu' ]
    then
        # for pycode in "`find . -type f -name '*.py'`"; do
        for pycode in "$edu"*.py; do
            echo "$pycode"
            yapf -i -r "$pycode"
        done
    elif [ $2 == 'hack' ]
    then
        # # find ./HackerRank -name '*.py' -print0 | xargs -0 yapf -i
        # for pycode in "`find ./HackerRank -type f -name '*.py'`"; do
        #     echo "$pycode"
        #     yapf -i -r "$pycode"
        # done
        # for pycode in ./HackerRank/Statistics/*.py; do
        for pycode in "$hack"*.py; do
            echo "$pycode"
            yapf -i -r "$pycode"
        done
    fi    
elif [ $1 == 'java' ]
then
    if [ $2 == 'all' ]
    then
        for javacode in $(find . -type f -name '*.java'); do
            echo "$javacode"
            google-java-format -r "$javacode"
        done
    elif [ $2 == 'lc' ]
    then
        for javacode in "$lc"*.java; do
            echo "$javacode"
            google-java-format -r "$javacode"
        done
    elif [ $2 == 'edu' ]
    then
        # for pycode in "`find . -type f -name '*.py'`"; do
        for javacode in "$edu"*.java; do
            echo "$javacode"
            google-java-format -r "$javacode"
        done
    fi        
elif [ $1 == 'sql' ]
then
    for sqlcode in "$lc_sql"*.sql; do
        echo "$sqlcode"
        sqlformat -r -k upper -i lower -o "$sqlcode" "$sqlcode"
    done
fi
