with open("project_twitter_data.txt", "r") as p_data:
    data_list = p_data.readlines()
    with open("project_twitter_data.csv", "w") as p_t_data:
        for item in data_list:
            if "\n" in item:
                item = item.replace("\n", "")
            s_list = item.split(",")
            for c_data1 in s_list[:2]:
                p_t_data.write(c_data1)
                p_t_data.write(",")
            for c_data2 in s_list[2:]:
                p_t_data.write(c_data2)
                p_t_data.write("\n")




