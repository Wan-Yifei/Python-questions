# author: Yifei.wan

# Extract and process the content from the annotation table

import sys
import argparse

def ParseArg():
    '''
    This function is used to set, accept and store argus.
    '''
    p = argparse.ArgumentParser(description="Parse the annotation table: reformate the indication and calculate the frequence for the indication, the gene and the variant respectively.")
    p.add_argument('-i', "--input", metavar = "<input txt table>", type=str, help = "the pathway of input flat table")
    p.add_argument("-o", "--output", metavar = "<output folder>", type = str, help = "the pathway of output folder")
    if len(sys.argv) < 2:
        print(p.print_help())
        sys.exit(0)
    return p.parse_args()

def indication_level(dict_ind, dict_sample, output):
    """
    indication_level = Gene and variant/ sample count
    """
    sample_count = len(dict_sample) 
    ind_level_cal = {k : len(v) / sample_count for k, v in dict_ind.items()}
    with open(output, "w+") as ind_level:
        print("Indication\tFrequency", file = ind_level)
        for k, v in ind_level_cal.items():
            print("%s\t%s"%(k, v), file = ind_level)

def gene_level(dict_gene, dict_sample, output):
    """
    gene_level = gene/sample count
    """
    sample_count = len(dict_sample)
    gene_level_cal = {k : len(v) / sample_count for k, v in dict_gene.items()} 
    with open(output, "w+") as gene_level:
        print("Gene\tFrequency", file = gene_level)
        for k, v in gene_level_cal.items():
            print("%s\t%s"%(k, v), file = gene_level)

def variant_level(sample_dict, output):
    """
    gene_level = variant/ gene for distinct sample 
    """
    gene_level_cal = {k : len(v) / len(set([i.split("\t", 1)[0] for i in v])) for k, v in  sample_dict.items()}
    with open(output, "w+") as var_level:
        print("Variant\tFrequency", file = var_level)
        for k, v in gene_level_cal.items():
            print("%s\t%s"%(k, v), file = var_level)

def main():
    args = ParseArg()
    input_table = args.input
    output_folder = args.output
    output_table = output_folder + "/" + input_table.split("/")[-1].replace(".txt", "_split.txt")
    output_ind_level = output_folder + "/" + "ind_level.txt"
    output_gene_level = output_folder + "/" + "gene_level.txt"
    output_variant_level = output_folder + "/" + "variant_level.txt"
    dict_indication = {}
    dict_sample = {}
    dict_gene = {}
    with open(input_table, "r") as table, open(output_table, "w+") as output:
        line = table.readline()
        while line:
            if "SAMPLE" in line :
                header = line.strip().split("\t") 
                header_new = header[0:-1] + ["VARIANT", "Result"]
                print("\t".join(header_new), file = output)
            elif "Anno" not in line and len(line) > 2:
                cols = line.strip().split("\t")
                gene_variant = cols.pop(-2) 
                dict_indication[gene_variant] = dict_indication.get(gene_variant, []) + [cols[0]]
                dict_sample[cols[0]] = dict_sample.get(cols[0], []) + [gene_variant]
                dict_gene[gene_variant.split("_", 1)[0]] = dict_gene.get(gene_variant.split("_", 1)[0], []) + [cols[0]]
                cols = cols[0:-1] + gene_variant.split("_", 1) + [cols[-1]]
                print("\t".join(cols), file = output)
            else:
                pass
            line = table.readline() 

    indication_level(dict_indication, dict_sample, output_ind_level)
    gene_level(dict_gene, dict_sample, output_gene_level)
    variant_level(dict_sample, output_variant_level)

if __name__ == "__main__":
    main()
