
import os, random
import FileUtils, mod_seqs, prompts, constants


def prep_seqs():
        positiveData = []
        negativeData = []
        positiveDir = os.listdir(os.path.join(os.getcwd(), constants.POS_CLEAN_DIR))
        negativeDir = os.listdir(os.path.join(os.getcwd(), constants.NEG_CLEAN_DIR))

        mean_lst = [] 

       
        mean_sum = 0 
        num_files = 0 

        print("Loading...")
        for file in positiveDir:
                pos_from_file = FileUtils.readFile(os.path.join(constants.POS_CLEAN_DIR, file))
                mean_of_file = len(pos_from_file[0])      
                mean_sum += mean_of_file 
                mean_lst.append(mean_of_file) 
                num_files += 1 

                positiveData.extend(pos_from_file)   

        for file in negativeDir:
                negativeData.extend(FileUtils.readFile(os.path.join(constants.NEG_CLEAN_DIR, file)))
      
        mean_of_means = int(mean_sum / num_files)

        trim_val = prompts.user_prompt(mean_of_means, mean_lst)
        print(f"Trimming sequences: {trim_val}")
        
        #  positive trimming
        positiveData = mod_seqs.trim_composite(positiveData, trim_val)

       
        positiveData = mod_seqs.add_labels(positiveData, positive=True)

        #  negative trimming
        negativeData = mod_seqs.trim_composite(negativeData, trim_val)

      
        negativeData = mod_seqs.add_labels(negativeData, positive=False)

        
        positiveData, negativeData = mod_seqs.equalize_lengths(positiveData, negativeData)
        print(f"Length of positive and negative data{len(positiveData), len(negativeData)}")
        
        
        validation_pos = positiveData[int(.95 * len(positiveData)) : ]
        validation_neg = negativeData[int(.95 * len(negativeData)) : ]
        print(f" % positive data the validation pos is: {len(validation_pos) / len(positiveData)}")
        print(f" % negative data the validation neg is: {len(validation_pos) / len(negativeData)}")
        validation_pos.extend(validation_neg)

        print("Shuffling validation data")
        random.shuffle(validation_pos)

        to_write_valid = mod_seqs.str_join(validation_pos)
        
        print(f"deleting validation data from test and train data")
        positiveData = positiveData[: int(.95 * len(positiveData))]
        negativeData = negativeData[: int(.95 * len(negativeData))]


       
        positiveData.extend(negativeData)
        
        

        print("Shuffling data")
     
        random.shuffle(positiveData)
  

        to_write = mod_seqs.str_join(positiveData)

        train_data_amt = int(len(to_write) * .70)
        test_data_amt = int(len(to_write) * .25)
        validation_amt = int(len(to_write) * .5)

        print("Deviding data into training  and testing split")
        train_data = to_write[ : train_data_amt]
        test_data = to_write[train_data_amt : ]

     

        print("Writing the train, test, and validation files.")
        
        FileUtils.write_file(constants.TRAIN, train_data)
        FileUtils.write_file(constants.TEST, test_data)
        FileUtils.write_file(constants.VALID, to_write_valid)

        print(f"Done. Training data in {constants.TRAIN}. Testing data in {constants.TEST}. Validation data in {constants.VALID}")


prep_seqs()
