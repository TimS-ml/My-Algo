for pycode in ./*.py; do
    echo "$pycode"
    yapf -i -r "$pycode"
done
