cd "tracks/"

for file in *
do
    cp $file  -P "/../gdrive/My Drive/daer_output_data/$file"
    echo "Copied file: $file"
done

cd ..

cd "outputs/"
for file in *
do
    cp $file  -P "/../gdrive/My Drive/daer_output_data/$file"
    echo "Copied file: $file"
done