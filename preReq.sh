
bf="beds"
fastas="fastas"
positives="pos_clean"
bed_negatives="negs_beds"
fastas_negatives="negs_fastas"
negatives="negs_clean"
ref_origin="/proj/siue-cs590-490-PG0/reference_genome/"
rf="reference"
mean="mean.txt"


if [ ! -d "../miniconda3" ]; then
    echo "Running Enviorement.sh"
    source Enviorement.sh
fi

echo "Runing sudo apt-get update again to ensure bedtools and gunzip can be installed correctly"


if [ -d $rf ]; then
    rm -rf $rf
fi


echo "Attempting to either cp the reference file if it exists or to download it. This may take a while..."
if cp -r $ref_origin .; then
    echo "cp of reference worked"
else
    echo "Unable to copy reference, need to download it..."
    mkdir reference && cd $_
    wget http://hgdownload.soe.ucsc.edu/goldenPath/hg38/bigZips/hg38.fa.gz;
    gunzip hg38.fa.gz;
    cd ..;
fi



echo "Making directories..." 
mkdir $fastas $positives $bed_negatives $fastas_negatives $negatives 

if [ ! -d $bf ]; then
    echo "There is no bed files to read from, perhaps you forgot to run bedsExtraction.sh"
   # rm -rf $file $fastas/$fastaFile $bed_negatives/$bed_negs_file $fastas_negatives/$fastas_negs_file $mean
    #rm -rf $bf $fastas $bed_negatives $fastas_negatives reference
    #rm -rf $positives $negatives
   
fi

for file in $bf/*; do
   
    filename= "$file"
    echo "Working on ${filename%.*}"
    fastaFile="${filename%.*}.fa"
    touch $fastas/$fastaFile
    bed_negs_file="${filename%.*}_negatives.bed"
    
    echo "Converting bed $file to a fasta file"
    bedtools getfasta -fi $rf/hg38.fa -bed $file -fo $fastas/$fastaFile
    echo "Cleaning the $fastaFile and returning the mean"
    python3 main.py $fastas/$fastaFile pos
    fastas_negs_file="${filename%.*}.fa"
    touch $fastas_negatives/$fastas_negs_file
    echo "Running getfasta on $bed_negs_file and sending to $fastas_negatives/$fastas_negs_file"
    bedtools getfasta -fi $rf/hg38.fa -bed $bed_negatives/$bed_negs_file -fo $fastas_negatives/$fastas_negs_file
    echo "Cleaning the $fastas_negs_file"
    python3 main.py $fastas_negatives/$fastas_negs_file $mean
rm -rf $file $fastas/$fastaFile $bed_negatives/$bed_negs_file $fastas_negatives/$fastas_negs_file $mean
done
rm -rf $bf $fastas $bed_negatives $fastas_negatives $rf
