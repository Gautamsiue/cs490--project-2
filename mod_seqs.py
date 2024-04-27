import tqdm
import constants
import numpy 
import FileUtils


def trim_sequences(seqs, mean_seq_length):
    trimmed_seqs = []
 
    for seq in seqs:
        if seq[3] < mean_seq_length:
            continue
        if seq[3] >= mean_seq_length:
            if seq[3] == mean_seq_length:
                trimmed_seqs.append(seq)
                continue
            seq[3] = mean_seq_length
            seq[4] = seq[4][:mean_seq_length]
            trimmed_seqs.append(seq)

    return trimmed_seqs


def grab_negative_ranges(seqs, pos_mean):
    ranges = []
    for i in range(1, len(seqs)):
        
        if seqs[i - 1][0] != seqs[i][0]:
            continue
        
        start = seqs[i - 1][2] + 1
        end = seqs[i][1] - 1
        if start >= end: 
            continue
        
        if end > start + pos_mean:
            end = start + pos_mean
        ranges.append([seqs[i][0], start, end])
        
    return ranges


def clean_seq_data(lines):
    seqs = [None]
    line_count = 0
    seq_count = 0
    
    length_sum = 0
    for line in lines:
        if line_count % 2 == 0:
            seq_info, length_sum = grab_seq_info(line, length_sum)
            if line_count == 0:
                seqs[line_count] = seq_info
            else:
                seqs.append(seq_info)
            seq_count += 1
        else: 
            seqs[seq_count - 1].append(line)
        line_count += 1
    return seqs, length_sum // seq_count    



def grab_seq_info(line, length_sum):
    line = line.split(':')
    chromosome_num = line[0].replace('>', '') 
    region = line[1].split('-') 
    start = int(region[0]) 
    end = int(region[1]) 
    length = end - start 
    length_sum += length 
    return [chromosome_num, start, end, length], length_sum


def trim_composite(seqs, mean_of_means):   
        trimmed_seqs = []
        for seq in seqs:
            if len(seq) < mean_of_means:
                continue
            if len(seq) > mean_of_means:
                seq = seq[:mean_of_means]
                trimmed_seqs.append(seq)
        
        return trimmed_seqs


def str_join(seqs):
        to_write = []
        [to_write.append("\t".join(seq)) for seq in seqs]

        return to_write



def add_labels(sequences, positive=True):
        if positive:
            return [["1", seq] for seq in sequences]
        
        return [["0", seq] for seq in sequences]


def equalize_lengths(lst1, lst2):
        if len(lst1) > len(lst2):
            lst1 = lst1[:len(lst2)]
        else: 
            lst2 = lst2[:len(lst1)]
        return lst1, lst2



def one_hot_encode(file):
    data= FileUtils
    seq_length = len(data[0][1])
    seqs_len = len(data)
    new_sequences = numpy.empty(shape=(seqs_len, 2), dtype=object) 
    for idx, seq in tqdm(enumerate(data)):
        new_sequence = numpy.empty(shape=(4, seq_length), dtype=numpy.float32)  #memory issue (hard disk) with float64
        for nidx, n in enumerate(constants.NUCLEOS):
            for cnt, nucleo in enumerate(seq[1]):
                if nucleo.casefold() == n.casefold():
                    new_sequence[nidx][cnt] = 1
                else:
                    new_sequence[nidx][cnt] = 0
        new_sequences[idx] = [numpy.float32(seq[0]), new_sequence]
    return new_sequences


def percentage(idx, length):
    print(f"{round((idx / length) * 100, 2)}%")
   
    