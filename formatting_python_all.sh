for pycode in $(find ./ -name '*.py'); do
    echo "$pycode"
    yapf -i -r "$pycode"
done
