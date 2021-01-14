# example to use
import numpy as np
import argparse
from os import walk
import os

def getGenFilesNameList(directory, extension):
    for (dirpath, dirnames, filenames) in walk(directory):
        return (f for f in filenames if f.endswith('.' + extension))

def Diff(li1, li2):
    x = set(li1)
    y = set(li2)
    z = x.difference(y)

    return z

def readFile(file_name):
    # Using readlines() 
    file1 = open(file_name, 'r') 
    Lines = file1.readlines() 
  
    count = 0
    time_val = 0
    cost_val = 0
    # Strips the newline character 
    for line in Lines: 
        if count == 0:
            str_text = line.strip()
            first_val = str_text.split(',')
            str_time_val_list = first_val[0].split('(')
            cost_val = float(str_time_val_list[1])
        if count == 1:
            time_val = float(line.strip())

        #print("Line{}: {}".format(count, line.strip()))
        count += 1
    return cost_val, time_val

def getStandardNameList():
    order_name_list = []
    order_name_list.append("orders_10_")
    order_name_list.append("orders_20_")

    mean_name_list = []
    mean_name_list.append("mean_1x6_")
    mean_name_list.append("mean_5_")

    sku_name_list = []
    sku_name_list.append("sku_24_")
    sku_name_list.append("sku_24_a_")
    sku_name_list.append("sku_24_b_")
    sku_name_list.append("sku_360_")
    sku_name_list.append("sku_360_a_")
    sku_name_list.append("sku_360_b_")

    mixed_dedicated_name_list = []
    mixed_dedicated_name_list.append("dedicated_no_improve_100")
    mixed_dedicated_name_list.append("dedicated_no_improve_200")
    mixed_dedicated_name_list.append("dedicated_no_improve_300")
    mixed_dedicated_name_list.append("dedicated_no_improve_400")
    mixed_dedicated_name_list.append("mixed_no_improve_100")
    mixed_dedicated_name_list.append("mixed_no_improve_200")
    mixed_dedicated_name_list.append("mixed_no_improve_300")
    mixed_dedicated_name_list.append("mixed_no_improve_400")

    output_name = ""
    idx = 1
    output_name_list = []
    for order_name in order_name_list:
        for mean_name in mean_name_list:
            for sku_name in sku_name_list:
                for mixed_dedicated_name in mixed_dedicated_name_list:
                    output_name = order_name + mean_name + sku_name + mixed_dedicated_name + "_result.txt"
                    output_name_list.append(output_name)
                    #print(idx, ": ", output_name)
                    print(output_name)
                    idx +=1 
    return output_name_list

def compareFiles(str_path):
    print("compare files:")
    gen_name_list = getGenFilesNameList(directory = str_path , extension = "xml")
    idx = 1
    str_gen_name_list = []
    for name in gen_name_list:
        #print(idx, ": ", name)
        str_gen_name_list.append(str(name))
        idx += 1

    order_name_list = []
    order_name_list.append("orders_10_")
    order_name_list.append("orders_20_")

    mean_name_list = []
    mean_name_list.append("mean_1x6_")
    mean_name_list.append("mean_5_")

    sku_name_list = []
    sku_name_list.append("sku_24_")
    sku_name_list.append("sku_24_a_")
    sku_name_list.append("sku_24_b_")
    sku_name_list.append("sku_360_")
    sku_name_list.append("sku_360_a_")
    sku_name_list.append("sku_360_b_")

    mixed_dedicated_name_list = []
    mixed_dedicated_name_list.append("dedicated_no_improve_100")
    mixed_dedicated_name_list.append("dedicated_no_improve_200")
    mixed_dedicated_name_list.append("dedicated_no_improve_300")
    mixed_dedicated_name_list.append("dedicated_no_improve_400")
    mixed_dedicated_name_list.append("mixed_no_improve_100")
    mixed_dedicated_name_list.append("mixed_no_improve_200")
    mixed_dedicated_name_list.append("mixed_no_improve_300")
    mixed_dedicated_name_list.append("mixed_no_improve_400")

    kmax_list = []
    kmax_list.append("_kmax_3")
    kmax_list.append("_kmax_4")

    output_name = ""
    idx = 1
    output_name_list = []
    for order_name in order_name_list:
        for mean_name in mean_name_list:
            for sku_name in sku_name_list:
                for mixed_dedicated_name in mixed_dedicated_name_list:
                    for kmax in kmax_list:
                        output_name = order_name + mean_name + sku_name + mixed_dedicated_name + kmax + ".xml"
                        output_name_list.append(output_name)
                        print(idx, ": ", output_name)
                        #print(output_name)
                        idx +=1 

    diff_list = Diff(output_name_list, str_gen_name_list)
    print("#######")
    print("DIFF")
    idx = 1
    for name in diff_list:
        print(idx, ": ", name)
        idx += 1
    return diff_list


def addName(str_name_list):
    #orders_10_mean_1x6_sku_360_a_mixed_no_improve_100_kmax_3_result.txt
    new_name_list = []
    str_add = "_m10_"
    for item in str_name_list:
        str_list = item.split("_")
        str_first = ""
        str_new_name = ""
        for idx in range(len(str_list) - 1):
            if idx == 0:
                str_first = str_first + str_list[idx]
            else:
                str_first = str_first + "_" +str_list[idx]
        idx = len(str_list)
        str_new_name = str_first + str_add + str_list[len(str_list) - 1]
        new_name_list.append(str_new_name)
    
    for item in new_name_list:
        print(item)
    return new_name_list

def changeName(path):
    print("change name")
    gen_name_list = getGenFilesNameList(directory = path, extension = "xml")
    gen_name_result_list = getGenFilesNameList(directory = path, extension = "txt")

    str_name_list = []
    str_name_result_list = []
    for item in gen_name_list:
        str_name_list.append(str(item))
    for item in gen_name_result_list:
        str_name_result_list.append(str(item))
        
    new_name_list = addName(str_name_list)
    new_result_name_list = addName(str_name_result_list)

    for idx in range(len(str_name_list)):
        str_a = path + "\\" + str_name_list[idx]
        str_b = path + "\\" + new_name_list[idx]
        print(str_a)
        print(str_b)
        os.rename(str_a, str_b)

    for idx in range(len(str_name_result_list)):
        str_a = path + "\\" + str_name_result_list[idx]
        str_b = path + "\\" + new_result_name_list[idx]
        print(str_a)
        print(str_b)
        os.rename(str_a, str_b)

def getSingleCostTimeAvgDict(path):
    print("get results:")

    #[A]
    #sigle folder
    #'' _a _b -> avg
    #get avg in a folder
    
    #[B]
    # x5 folders
    #get avg
    #get max avg from single
    #get mix avg from single

    # [1] get file_cost_time_dict
    print("path:", path)
    gen_name_list = getGenFilesNameList(directory = path, extension = "txt")
    idx = 1
    str_gen_name_list = []
    str_gen_name_list_no_path = []
    cost_time_dict = {}
    for name in gen_name_list:
        print(name)
        str_gen_name_list_no_path.append(name)
        #print(idx, ": ", name)
        file_name = path + "\\" + str(name)
        str_gen_name_list.append(file_name)
        idx += 1
        cost_val, time_val = readFile(file_name)
        #print("cost_val:", cost_val, "time_val:", time_val)
        cost_time_dict[str(name)] = [cost_val, time_val]
    cost_time_dict
    
    # [2] get three_result_dict key: "", value: ["_a", "_b"]
    simple_name_list = str_gen_name_list_no_path.copy()
    simple_name_list_a = []
    simple_name_list_b = []
    for item in simple_name_list:
        str_list = item.split("_")
        print(str_list)
        for ele in str_list:
            if 'a' == ele:
                simple_name_list_a.append(item)
            if 'b' == ele:
                simple_name_list_b.append(item)

    for item_a in simple_name_list_a:
        simple_name_list.remove(item_a)

    for item_b in simple_name_list_b:
        simple_name_list.remove(item_b)

    for item in simple_name_list:
        print(item)
    
    three_result_dict = {}
    for item_simple in simple_name_list:
        three_result_dict[item_simple] = []
        str_list_simple = item_simple.split("_")
        for item in str_gen_name_list_no_path:
            str_list = item.split("_")
            diff_list = Diff(str_list, str_list_simple)
            if len(diff_list) == 1:
                if 'a' in diff_list:
                    #print("diff: ", diff_list)
                    #print(item)
                    three_result_dict[item_simple].append(item)
                if 'b' in diff_list:
                    #print("diff: ", diff_list)
                    #print(item)
                    three_result_dict[item_simple].append(item)
    
    # [3] get single_cost_time_avg_dict
    single_cost_time_avg_dict = {}
    for key, value in three_result_dict.items():
        cost_val = 0
        time_val = 0
        cost_val_a = 0
        time_val_a = 0
        cost_val_b = 0
        time_val_b = 0

        if (key in cost_time_dict.keys()):
            cost_val = cost_time_dict[key][0]
            time_val = cost_time_dict[key][1]
        if (value[0] in cost_time_dict.keys()):
            cost_val_a = cost_time_dict[value[0]][0]
            time_val_a = cost_time_dict[value[0]][1]
        if (value[1] in cost_time_dict.keys()):
            cost_val_b = cost_time_dict[value[1]][0]
            time_val_b = cost_time_dict[value[1]][1]
        
        avg_cost_val = (cost_val + cost_val_a + cost_val_b) /3
        avg_time_val = (time_val + time_val_a + time_val_b) /3
        print(key, avg_cost_val, avg_time_val)
        single_cost_time_avg_dict[key] = [avg_cost_val, avg_time_val]

    return single_cost_time_avg_dict

def genOutput(path_list, output_file):
    multi_cost_time_dict_list = []
    for path in path_list:
        single_cost_time_dict = getSingleCostTimeAvgDict(path)
        multi_cost_time_dict_list.append(single_cost_time_dict)

    single_cost_time_dict0 = multi_cost_time_dict_list[0]
    single_cost_time_dict1 = multi_cost_time_dict_list[1]
    single_cost_time_dict2 = multi_cost_time_dict_list[2]
    single_cost_time_dict3 = multi_cost_time_dict_list[3]
    single_cost_time_dict4 = multi_cost_time_dict_list[4]

    output_results_dict = {}
    for key, value in single_cost_time_dict0.items():
        proc_avg_cost_list = []
        proc_avg_cost_list.append(single_cost_time_dict0[key][0])
        proc_avg_cost_list.append(single_cost_time_dict1[key][0])
        proc_avg_cost_list.append(single_cost_time_dict2[key][0])
        proc_avg_cost_list.append(single_cost_time_dict3[key][0])
        proc_avg_cost_list.append(single_cost_time_dict4[key][0])

        avg_cost_val = (single_cost_time_dict0[key][0] + single_cost_time_dict1[key][0] + \
            single_cost_time_dict2[key][0]+ single_cost_time_dict3[key][0] +single_cost_time_dict4[key][0]) / 5

        max_cost_val = max(proc_avg_cost_list)
        min_cost_val = min(proc_avg_cost_list)

        avg_time_val = (single_cost_time_dict0[key][1] + single_cost_time_dict1[key][1] + \
            single_cost_time_dict2[key][1]+ single_cost_time_dict3[key][1] +single_cost_time_dict4[key][1]) / 5

        output_results_dict[key] = [avg_cost_val, max_cost_val, min_cost_val, avg_time_val]

    print("RESULTS OUTPUT:")
    sourceFile = open(output_file, 'w')
    for key, value in output_results_dict.items():
        print(key, value)
        print(key, value, file = sourceFile)
    sourceFile.close()
if __name__ == "__main__":
    #str_path = r"C:\GitHub\cobot_shortest_path\instance_demo\results_rafs\3"
    #diff_list = compareFiles(str_path)

    #str_path = r"C:\GitHub\cobot_shortest_path\instance_demo\results_rafs\4z"
    #changeName(str_path)
    #for item in diff_list:
    #    item_list = item.split('.')
    #    folder = "x0"
    #    print("python agv_routing_mixed_para_tuning.py -output " + folder + " -file " + item_list[0])


    path_list = []
    path_list.append(r"C:\GitHub\cobot_shortest_path\instance_demo\results_rafs\0")
    path_list.append(r"C:\GitHub\cobot_shortest_path\instance_demo\results_rafs\1")
    path_list.append(r"C:\GitHub\cobot_shortest_path\instance_demo\results_rafs\2")
    path_list.append(r"C:\GitHub\cobot_shortest_path\instance_demo\results_rafs\3")
    path_list.append(r"C:\GitHub\cobot_shortest_path\instance_demo\results_rafs\4")
    
    genOutput(path_list, 'output_results_2021.1.14.txt')

    path_list_m10 = []
    path_list_m10.append(r"C:\GitHub\cobot_shortest_path\instance_demo\results_rafs\0\m10")
    path_list_m10.append(r"C:\GitHub\cobot_shortest_path\instance_demo\results_rafs\1\m10")
    path_list_m10.append(r"C:\GitHub\cobot_shortest_path\instance_demo\results_rafs\2\m10")
    path_list_m10.append(r"C:\GitHub\cobot_shortest_path\instance_demo\results_rafs\3\m10")
    path_list_m10.append(r"C:\GitHub\cobot_shortest_path\instance_demo\results_rafs\4\m10")

    genOutput(path_list_m10, 'output_results_m10_2021.1.14.txt')
