import os, sys
import mod_seqs, FileUtils, constants


def main():
    fastaFile = sys.argv[1]
    arg2 = sys.argv[2]

    fasta = fastaFile.split('/')[-1].split('.')[0]
    neg_bed = f"{fasta}_negatives.bed"
    negFile_two = f"{fasta}_filtered_negatives.txt"
    pos_file_name = f"{fasta}_filtered_positives.txt"

   
    seq_data = FileUtils.readFile(fastaFile)
 
    if arg2 == 'pos':      #if 2nd arg is something else 
        print("Cleaning the data and finding the mean length of the accessible regions' sequences") 
        seqs, mean_seq_length = mod_seqs.clean_seq_data(seq_data)

        print("Trimming the sequences by the mean length")
        trimmed_seqs = mod_seqs.trim_sequences(seqs, mean_seq_length)

        # find the ranges between the positive/open/peak areas
        print("Finding the region between the positive ranges, which are innacessible")
        print("Additionally, chopping these regions to the length of the accessible regions' mean")
        negative_ranges = mod_seqs.grab_negative_ranges(seqs, mean_seq_length)

        neg_path = os.path.join(constants.NEG_BEDS_DIR,negFile)
        print(f"The mean of {fasta} is {mean_seq_length}\n")
        #specifically create the negative fastas file
        FileUtils.create_file(neg_path, negative_ranges)

        # cleaned positive sequences
        pos_path = os.path.join(constants.POS_CLEAN_DIR, pos_file_name)
        FileUtils.create_file(pos_path, trimmed_seqs)
        FileUtils.write_file(f"{fasta}_{constants.MEAN}", [str(mean_seq_length)])
    
    
    if arg2 == constants.MEAN:
        print("Trimming the negative sequences to the same length as the positive sequences.\n")
        mean = int(FileUtils.readFile(f"{fasta}_{constants.MEAN}")[0])
        os.remove(f"{fasta}_{constants.MEAN}")
        seqs, neg_mean_seq_length = mod_seqs.clean_seq_data(seq_data)
        trimmed_seqs = mod_seqs.trim_sequences(seqs, mean)
        clean_negs_path = os.path.join(constants.NEG_CLEAN_DIR,negFile_two)
        FileUtils.create_file(clean_negs_path, trimmed_seqs)


if __name__ == "__main__":
    main()