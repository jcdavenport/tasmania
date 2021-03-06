import os
import time
import shutil
import pandas as pd

# training files
train_file = "data/train/contest-train.csv"
train_proc = "data/train/processed.csv"

# testing files
test_file = "data/test/contest-test.csv"
test_proc = "data/test/processed.csv"

# models
exp_model = "results/experiment_run_0/model"

# predictions
predict_file = "results_0/Category_predictions.csv"

# results
result_file = "results/tasmania.csv"


def train():
    df_train = pd.read_csv(train_file, encoding='iso-8859-1')

    df_train[['Consolidated Course Name', 'Category']].to_csv(train_proc, index=False)

    df_train_proc = pd.read_csv(train_proc, encoding='iso-8859-1')

    df_train_proc.columns = ['Consolidated_Course_Name', 'Category']

    df_train_proc.to_csv(train_proc, index=False)

    print("DONE")

    # remove data from previous run
    dirpath1 = "results/experiment_run_0"
    if os.path.exists(dirpath1) and os.path.isdir(dirpath1):
        shutil.rmtree(dirpath1)
    return


def ludwig():
    train_ludz = "\"{input_features: [{name: Consolidated_Course_Name, type: text}], " \
                 "output_features: [{name: Category, type: category}]}\""

    os.system("ludwig train --data_csv " + train_proc + " --model_definition " + train_ludz)

    print("\nThe machine is becoming aware...")
    time.sleep(3)
    return


def test():

    df_test = pd.read_csv(test_file, encoding='iso-8859-1')

    df_test[['Consolidated Course Name', 'Category']].to_csv(test_proc, index=False)

    df_test_proc = pd.read_csv(test_proc, encoding='iso-8859-1')

    df_test_proc.columns = ['Consolidated_Course_Name', 'Category']

    df_test_proc.to_csv(test_proc, index=False)

    # remove data from any previous runs
    dirpath2 = "results_0"
    if os.path.exists(dirpath2) and os.path.isdir(dirpath2):
        shutil.rmtree(dirpath2)

    print("DONE")
    time.sleep(2)
    return


def predict():

    # Using ludwig to predict values
    os.system("ludwig predict --data_csv " + test_proc + " --model_path " + exp_model)
    print("...DONE")

    return


if __name__ == '__main__':

    print("\nLaunching training sequence...\n")
    time.sleep(3)
    train()

    print("\nTraining the machine...\n")
    time.sleep(3)
    ludwig()

    print("\nPreparing the test data...\n")
    time.sleep(3)
    test()

    print("\nPredicting the test values...\n")
    time.sleep(2)
    predict()

    print("\n...End of Execution\n")
