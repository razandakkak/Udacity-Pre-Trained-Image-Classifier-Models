#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED:
# REVISED DATE: 
# PURPOSE: Create a function print_results that prints the results statistics
#          from the results statistics dictionary (results_stats_dic). It 
#          should also allow the user to be able to print out cases of misclassified
#          dogs and cases of misclassified breeds of dog using the Results 
#          dictionary (results_dic).  
#         This function inputs:
#            -The results dictionary as results_dic within print_results 
#             function and results for the function call within main.
#            -The results statistics dictionary as results_stats_dic within 
#             print_results function and results_stats for the function call within main.
#            -The CNN model architecture as model wihtin print_results function
#             and in_arg.arch for the function call within main. 
#            -Prints Incorrectly Classified Dogs as print_incorrect_dogs within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#            -Prints Incorrectly Classified Breeds as print_incorrect_breed within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#         This function does not output anything other than printing a summary
#         of the final results.
##
# TODO 6: Define print_results function below, specifically replace the None
#       below by the function definition of the print_results function. 
#       Notice that this function doesn't to return anything because it  
#       prints a summary of the results using results_dic and results_stats_dic
# 
def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs=False, print_incorrect_breed=False):
    """
    Prints summary results on the classification and then prints incorrectly 
    classified dogs and incorrectly classified dog breeds if user indicates 
    they want those printouts (use non-default values)
    """
    # Header for the results summary
    print("\n\n*** Results Summary for CNN Model Architecture", model.upper(), "***")
    
    # Print total counts of images, dog images, and not-dog images
    print("{:25}: {:3d}".format("# Total Images", results_stats_dic['n_images']))
    print("{:25}: {:3d}".format("# Dog Images", results_stats_dic['n_dogs_img']))
    print("{:25}: {:3d}".format("# Not-a-Dog Images", results_stats_dic['n_notdogs_img']))

    # Display metrics in a table-like format
    print("\n{:25} {:>12} {:>12} {:>12} {:>12}".format(
        "CNN Model Architecture", "% Not-a-Dog Correct", "% Dogs Correct", "% Breeds Correct", "% Match Labels"))
    
    print("{:25} {:>12.1f}% {:>12.1f}% {:>12.1f}% {:>12.1f}%".format(
        model.upper(), 
        results_stats_dic['pct_correct_notdogs'], 
        results_stats_dic['pct_correct_dogs'], 
        results_stats_dic['pct_correct_breed'], 
        results_stats_dic['pct_match']))

    # Print misclassified dogs if specified
    if print_incorrect_dogs and (results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs'] != results_stats_dic['n_images']):
        print("\nINCORRECT Dog/NOT Dog Assignments:")
        for filename, result in results_dic.items():
            if (result[3] == 1 and result[4] == 0) or (result[3] == 0 and result[4] == 1):
                print("Real: {:>26}   Classifier: {:>30}".format(result[0], result[1]))

    # Print misclassified breeds if specified
    if print_incorrect_breed and (results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed']):
        print("\nINCORRECT Dog Breed Assignment:")
        for filename, result in results_dic.items():
            if result[3] == 1 and result[4] == 1 and result[2] == 0:
                print("Real: {:>26}   Classifier: {:>30}".format(result[0], result[1]))
