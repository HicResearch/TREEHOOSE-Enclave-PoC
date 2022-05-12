# TREEHOOSE-Enclave-PoC
Proof of concept scripts for running within the secure enclave

step 1 download the repository and unzip it. You have a folder named "TREEHOOSE-Enclave-PoC-main" in your local file system;

step 2 create a folder called "output" within the TREEHOOSE-Enclave-PoC-main/Main folder;

step 3 download the trained SVM model containing autoencoderMRI.h5 and MRI_Sequence_SVMClassifier.pkl model file into the TREEHOOSE-Enclave-PoC-main/Main/output folder, the links for the model are: https://dmail.sharepoint.com/:f:/r/sites/HICCloudTREHIC-AWScollaboration/Shared%20Documents/treehoose/Secure%20Enclave/model%20file%20for%20TREEHOOSE-Enclave-PoC?csf=1&web=1&e=vUgyg5

step 4 open the project in your IDE (PyCharm), the project folder is TREEHOOSE-Enclave-PoC-main/Main

step 5 make sure the following packages are installed for the project
      
      *tensorflow
      *sklearn
      *matplotlib
      *opencv-python
      *nibabel
      *pydicom

step 6 open file "SVM_classifier_tester.py" and edit line 27 to point to TREEHOOSE-Enclave-PoC-main/Main/ folder, and line 29 to point to REEHOOSE-Enclave-PoC-main/Data/ folder, the following is an example for those two lines. the "/" by the end of the folder is required
      
      *project_path = 'C:/Users/cgao001/OneDrive - University of Dundee/HIC research/3 hic/TreeHoose-enclave/WP3_SMI-main/'
      *path = 'C:/Users/cgao001/OneDrive - University of Dundee/HIC research/3 hic/TreeHoose-enclave/TREEHOOSE-Enclave-PoC-main/Data/'

step 7 run "SVM_classifier_tester.py", you should get a file "MRI_Sequence_Results.txt" in TREEHOOSE-Enclave-PoC-main/Main/output folder if you are successful.
