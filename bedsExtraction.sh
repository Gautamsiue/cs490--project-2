bf="beds"

echo "Enter path of the text file containing links:"
read -r file_path
# Check if the file exists
echo "Checking..."
if [ ! -f "$file_path" ]; then
    echo "File not found: $file_path"
    exit 1
fi

mkdir $bf

echo "Reading files...."


echo "Downloading files....."
for link in "${links[@]}"; do
   
    wget "$link" -O "${link##*/}"
    mv "${link##*/}" $bf
done


echo "Unzipping files..."
for file in $bf/*; do
    gunzip "$file"
done
