import os
import sys
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
result_file = "results/tasmania.csv"
exp_model = "results/experiment_run_0/model"

# predictions
predict_file = "results_0/Category_predictions.csv"

# df_train = pd.read_csv(train_file, encoding='iso-8859-1')
#
# print("Processing the csv file...\n")
#
# df_train[['Consolidated Course Name', 'Category']].to_csv(train_proc, index=False)
#
# df_train_proc = pd.read_csv(train_proc, encoding='iso-8859-1')
#
# df_train_proc.columns = ['Consolidated_Course_Name', 'Category']
#
# df_train_proc.to_csv(train_proc, index=False)
#
# print("DONE")
#
# # remove data from previous run
# dirpath1 = "results/experiment_run_0"
# if os.path.exists(dirpath1) and os.path.isdir(dirpath1):
#     shutil.rmtree(dirpath1)
#
# train_ludz = "\"{input_features: [{name: Consolidated_Course_Name, type: text}], " \
#              "output_features: [{name: Category, type: category}]}\""
#
# print("\nTraining the machine...")
# time.sleep(3)
#
# os.system("ludwig train --data_csv " + train_proc + " --model_definition " + train_ludz)
#
# print("\nThe machine is becoming aware...")
# time.sleep(3)
#
# print("Preparing the test data...")
#
# df_test = pd.read_csv(test_file, encoding='iso-8859-1')
#
# df_test[['Consolidated Course Name', 'Category']].to_csv(test_proc, index=False)
#
# df_test_proc = pd.read_csv(test_proc, encoding='iso-8859-1')
#
# df_test_proc.columns = ['Consolidated_Course_Name', 'Category']
#
# df_test_proc.to_csv(test_proc, index=False)
#
# print("DONE")
#
# time.sleep(2)
#
# print("\nPredicting the test values...\n")
#
# time.sleep(2)
#
# # remove data from previous run
# dirpath2 = "results_0"
# if os.path.exists(dirpath2) and os.path.isdir(dirpath2):
#     shutil.rmtree(dirpath2)
#
# os.system("ludwig predict --data_csv " + test_proc + " --model_path " + exp_model)
#
# print("...DONE")

dfr = pd.read_csv("results/con-test.csv", encoding='iso-8859-1')
dataf = pd.read_csv(predict_file, encoding='iso-8859-1')

dataf.to_csv("results/dataf.csv", index=False)

li = ''

with open(predict_file, 'r') as f:
    li = f.read().splitlines()

col = 'Category'
# li.insert(0, "Category")

new_df = pd.DataFrame(li, columns=['Category'])

for line in range(0, 10+1):
    if line >= 0:
        print(li[line])

print()
print(new_df)
dfr[col] = new_df
new_df.to_csv("results/new.csv", index=False)

dfr.to_csv("results/results.csv", index=False)

df_new = pd.read_csv("results/results.csv", encoding='iso-8859-1')

print(df_new['Category'].head())

# row = []
#
# for row in dfr[col].head():
#     findL = li[]
#     print(findL)








