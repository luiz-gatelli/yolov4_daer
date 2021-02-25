cd "/gdrive/My Drive/"
echo "Copying Weigths:"
cp "yolov4-obj_best.weights" -P "/content/yolov4_daer/data/yolov4.weights"
echo "Copied YoloV4 Weigths"

echo ""

echo "Copying Videos:"

cd "/gdrive/My Drive/unprocessed_videos/"
for file in *
do 
    cp $file -P "/content/yolov4_daer/data/video/$file"
    echo "Copied file: $file"
done

echo ""
echo "Saving Model:"

cd /content/yolov4_daer/
python save_model.py --model yolov4

echo "Model Saved"