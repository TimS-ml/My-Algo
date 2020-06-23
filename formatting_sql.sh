for sqlcode in ./*.sql; do
    echo "$sqlcode"
    sqlformat -r -k upper -i lower -o "$sqlcode" "$sqlcode"
done
