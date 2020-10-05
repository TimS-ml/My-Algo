# https://askubuntu.com/questions/343727/filenames-with-spaces-breaking-for-loop-find-command
for pycode in "`find . -type f  -name '*.py'`"; do
    echo "$pycode"
    yapf -i -r "$pycode"
done
