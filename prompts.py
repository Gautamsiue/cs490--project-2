def user_prompt(mean_of_means, mean_lst):
        print(f"The average for all the means of the positive and negative files is {mean_of_means}.")
        mean_lst = ", ".join([str(mean) for mean in mean_lst])
        print(f"The list of the original means is: {mean_lst}")
        user_in = input("Would you like to use the mean of the means (1) or choose your own val? (2): ")
        while True:
                if user_in == "1":
                        trim_val = mean_of_means
                        break
                elif user_in == "2":
                        trim_val = int(input("Enter the custom value > 300: ")) 
                        break
                else:
                        "Invalid Selection, Try Again."
        return trim_val

