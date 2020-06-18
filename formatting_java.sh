for javacode in ./*.java; do
    echo "$javacode"
    google-java-format -r "$javacode"
done
