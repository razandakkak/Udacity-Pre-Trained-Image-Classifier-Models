# Udacity-Pre-Trained-Image-Classifier-Models
This Project involves the using of the three pre-trained models **Alexnet**, **VGG**, **Resnet** to identify a dog breed and classify it as a dog/or not.

## Project Structure
This repository contains several files that work together, starting from the most important one, *check_images.py* which is the main program to run the three models on the dataset.
Along with the neccessary scipts that are defined within it such as; *classify_images.py*, *classifier.py*, *get_input_args.py*, *get_pet_labels* and so on. I will leave you the curiostiy to discover each one alone.

To run the project on 'pet_images' folder you need to use 
```
sh run_models_batch.sh
```

while to run it on the uploaded images folder you need to use
```
sh run_models_batch_uploaded.sh
```

## Project Result
As you will see in each of the model's output metrics, on the pet images and on the uploaded images, the best model with these parameters

*pct_correct_dogs    : 100.00%*

*pct_correct_breed   : 93.33%*

*pct_correct_notdogs : 100.00%*

*pct_match           : 87.50%*

which is VGG, is the best model.

### Note: it is better to create a virtual environment using anaconda or a python venv for installing the requirements.
