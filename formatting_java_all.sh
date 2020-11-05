# https://askubuntu.com/questions/343727/filenames-with-spaces-breaking-for-loop-find-command
for javacode in "`find . -type f  -name '*.java'`"; do
    echo "$javacode"
    google-java-format -r "$javacode"
done
