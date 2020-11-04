for pycode in ./Educative/*.py; do
    echo "$pycode"
    yapf -i -r "$pycode"
done
