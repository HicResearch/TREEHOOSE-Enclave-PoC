# TREEHOOSE-Enclave-PoC
Proof of concept scripts for running within the secure enclave

step 1 download the repository and unzip it. You have a folder named `TREEHOOSE-Enclave-PoC` in your local file system;

step 2 create a folder called `output` within the `TREEHOOSE-Enclave-PoC/Main` folder;

step 3 download the trained SVM model containing autoencoderMRI.h5 and MRI_Sequence_SVMClassifier.pkl model file into the `TREEHOOSE-Enclave-PoC/Main/output` folder, the links for the model files are on [Teams](https://dmail.sharepoint.com/:f:/r/sites/HICCloudTREHIC-AWScollaboration/Shared%20Documents/treehoose/Secure%20Enclave/model%20file%20for%20TREEHOOSE-Enclave-PoC?csf=1&web=1&e=vUgyg5).

step 4 open the project in your IDE (PyCharm), the project folder is `TREEHOOSE-Enclave-PoC/Main`

step 5 make sure the following packages are installed for the project
      
  * tensorflow
  * sklearn
  * opencv-python
  * nibabel
  * pydicom

step 6 run the script `python Main/SVM_classifier_tester.py`, you should get a file `MRI_Sequence_Results.txt` in `TREEHOOSE-Enclave-PoC/Main/output` folder if you are successful.

**Optional** 

To change the default paths use the script's arguments:

    optional arguments:
      -h, --help            show this help message and exit
      -m MODEL, --model MODEL
                            path to trained autoencoder
      -s SVM, --SVM SVM     path to SVM index file
      -d DATA, --data DATA  path image data
      -o OUT, --out OUT     output path

The defaults are:

    python Main/SVM_classifier_tester.py -m Main/output/autoencoderMRI.h5 \\
    -s Main/output/MRI_Sequence_SVMClassifier.pkl -d Data/ -o Main/output/


