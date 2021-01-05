# example to use
import numpy as np
import argparse
from os import walk

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

def getOutputResults(path_list):
    print("get results:")
    file_cost_time_dict = {}
    
    for path in path_list:
        print("path:", path)
        gen_name_list = getGenFilesNameList(directory = path, extension = "txt")
        idx = 1
        str_gen_name_list = []
        cost_time_dict = {}
        for name in gen_name_list:
            print(name)
            #print(idx, ": ", name)
            file_name = path + "\\" + str(name)
            str_gen_name_list.append(file_name)
            idx += 1
            cost_val, time_val = readFile(file_name)
            #print("cost_val:", cost_val, "time_val:", time_val)
            cost_time_dict[str(name)] = [cost_val, time_val]
        file_cost_time_dict[path] = cost_time_dict
    
    file_cost_time_dict_sum = {}
    for key_path, value_dict in file_cost_time_dict.items():
        for key_name, value_cost_time_dict in value_dict.items():
            if key_name in file_cost_time_dict_sum.keys():
                cost_sum = value_cost_time_dict[0]
                time_sum = value_cost_time_dict[1]
                count = file_cost_time_dict_sum[key_name][2] + 1
                file_cost_time_dict_sum[key_name] = [file_cost_time_dict_sum[key_name][0] + cost_sum, file_cost_time_dict_sum[key_name][1] + time_sum, count]
            else:
                cost_sum = value_cost_time_dict[0]
                time_sum = value_cost_time_dict[1]
                file_cost_time_dict_sum[key_name] = [cost_sum, time_sum, 1]
    
    file_cost_time_dict_avg = {}
    for key, value in file_cost_time_dict_sum.items():
        count = value[2]
        if count != 0:
            file_cost_time_dict_avg[key] = [value[0]/count, value[1]/count]

    for key, value in file_cost_time_dict_avg.items():
        print("{}, avg_cost:{}, avg_time:{}".format(key, value[0], value[1]))

    output_name_list = getStandardNameList()
    simple_name_list = output_name_list.copy()
    simple_name_list_a = []
    simple_name_list_b = []
    for item in output_name_list:
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
        for item in output_name_list:
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

    for key, value in three_result_dict.items():
        cost_val = 0
        time_val = 0
        cost_val_a = 0
        time_val_a = 0
        cost_val_b = 0
        time_val_b = 0

        if (key in file_cost_time_dict_avg.keys()):
            cost_val = file_cost_time_dict_avg[key][0]
            time_val = file_cost_time_dict_avg[key][1]
        if (value[0] in file_cost_time_dict_avg.keys()):
            cost_val_a = file_cost_time_dict_avg[value[0]][0]
            time_val_a = file_cost_time_dict_avg[value[0]][1]
        if (value[1] in file_cost_time_dict_avg.keys()):
            cost_val_b = file_cost_time_dict_avg[value[1]][0]
            time_val_b = file_cost_time_dict_avg[value[1]][1]
        
        avg_cost_val = (cost_val + cost_val_a + cost_val_b) /3
        avg_time_val = (time_val + time_val_a + time_val_b) /3
        print(key, avg_cost_val, avg_time_val)


    return file_cost_time_dict_avg

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

    output_name = ""
    idx = 1
    output_name_list = []
    for order_name in order_name_list:
        for mean_name in mean_name_list:
            for sku_name in sku_name_list:
                for mixed_dedicated_name in mixed_dedicated_name_list:
                    output_name = order_name + mean_name + sku_name + mixed_dedicated_name + ".xml"
                    output_name_list.append(output_name)
                    #print(idx, ": ", output_name)
                    print(output_name)
                    idx +=1 

    diff_list = Diff(output_name_list, str_gen_name_list)
    print("#######")
    print("DIFF")
    idx = 1
    for name in diff_list:
        print(idx, ": ", name)
        idx += 1
    return diff_list

if __name__ == "__main__":
    str_path = r"C:\GitHub\cobot_shortest_path\instance_demo\test\0"
    diff_list = compareFiles(str_path)
    for item in diff_list:
        item_list = item.split('.')
        folder = "x0"
        print("python agv_routing_mixed_para_tuning.py -output " + folder + " -file " + item_list[0])

    #path_list = []
    #path_list.append(r"C:\GitHub\cobot_shortest_path\instance_demo\test\0")
    #path_list.append(r"C:\GitHub\cobot_shortest_path\instance_demo\test\1")
    #path_list.append(r"C:\GitHub\cobot_shortest_path\instance_demo\test\2")
    #path_list.append(r"C:\GitHub\cobot_shortest_path\instance_demo\test\3")
    #path_list.append(r"C:\GitHub\cobot_shortest_path\instance_demo\test\4")
    #file_cost_time_dict = getOutputResults(path_list)

    #parser = argparse.ArgumentParser()
    #parser.add_argument('-output', required=True)
    #parser.add_argument('-sku', required=True)
    #parser.add_argument('-dedicated', dest='dedicated',
    #                   action='store_true',
    #                   help='dedicated shevels')

    #args = parser.parse_args()
    #print('#################################')
    #print(f'## output path: {args.output}')
    #print(f'## sku: {args.sku}')
    #print('#################################')

