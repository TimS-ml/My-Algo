# Find the latest input file
latest_file=$(ls input-d*.txt | sort -t '-' -k 1.2,1n -k 2,2n | tail -n 1)

# Extract the ID from the filename
ID=$(echo $latest_file | sed -E 's/input-(d[0-9]+-[0-9]+).txt/\1/')

# Check if an ID was found
if [ -z "$ID" ]; then
    echo "No input file found."
    exit 1
fi

echo "Found ID: ${ID}"

# Find the Python script with the largest solve number for the identified ID
latest_script=$(ls ${ID}-m-*.py | sort -t '-' -k 3,3n | tail -n 1)

# Check if a script was found
if [ -z "$latest_script" ]; then
    echo "No Python script found for ID ${ID}."
    exit 1
fi

echo "Running script ${latest_script} with input file input-${ID}.txt..."
python ${latest_script} < input-${ID}.txt
